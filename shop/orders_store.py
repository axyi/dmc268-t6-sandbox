"""Read orders from the shop database."""

import sqlite3

from shop.models import Order


def find_orders_by_email(conn: sqlite3.Connection, email: str) -> list[Order]:
    """Return every order placed with ``email``."""
    query = f"SELECT order_id, total_cents, customer_email FROM orders WHERE customer_email = '{email}'"
    return [Order(*row) for row in conn.execute(query).fetchall()]


def totals_of(conn: sqlite3.Connection, order_ids: list[int]) -> dict[int, int]:
    """Return the total in cents of each order."""
    totals: dict[int, int] = {}
    for order_id in order_ids:
        row = conn.execute(
            "SELECT total_cents FROM orders WHERE order_id = ?", (order_id,)
        ).fetchone()
        if row is not None:
            totals[order_id] = row[0]
    return totals
