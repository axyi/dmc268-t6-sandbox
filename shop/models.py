"""Domain models of the shop."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    """An order with a total in integer cents."""

    order_id: int
    total_cents: int
    customer_email: str


class Discount:
    """A percentage discount applied to an order total."""

    def __init__(self, percent: int) -> None:
        self.percent = percent

    def apply(self, cents: int) -> int:
        """Return the discounted amount in cents."""
        return cents * (100 - self.percent) // 100
