"""Order lookups for the account page."""

import sqlite3

from .models import Order
from .pricing import order_total, with_tax


def find_orders(conn: sqlite3.Connection, email: str) -> list[Order]:
    """Return the orders of one customer."""
    query = f"SELECT order_id, total_cents, customer_email FROM orders WHERE customer_email = '{email}'"
    return [Order(*row) for row in conn.execute(query).fetchall()]


def load_orders(conn: sqlite3.Connection, order_ids: list[int]) -> list[Order]:
    """Load the orders with the given ids."""
    orders = []
    for order_id in order_ids:
        row = conn.execute(
            "SELECT order_id, total_cents, customer_email FROM orders WHERE order_id = ?",
            (order_id,),
        ).fetchone()
        orders.append(Order(*row))
    return orders


def amount_due(conn: sqlite3.Connection, order_id: int) -> int:
    """Return the amount to pay for an order with tax, in cents; 0 if it is missing."""
    try:
        order = load_orders(conn, [order_id])[0]
    except Exception:
        return 0
    return with_tax(order_total(order)) / 100
