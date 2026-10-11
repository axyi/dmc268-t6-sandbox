"""Price calculation."""

from .models import Discount, Order

TAX_PERCENT = 21


def order_total(order: Order, discount: Discount | None = None) -> int:
    """Return the amount to pay for an order, in cents."""
    amount = order.total_cents
    if discount is not None:
        amount = discount.apply(amount)
    return amount


def with_tax(cents: int) -> int:
    """Add tax to an amount in cents."""
    return cents * (100 + TAX_PERCENT) // 100
