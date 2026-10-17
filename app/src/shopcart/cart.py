from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    name: str
    price_cents: int
    quantity: int = 1

    def __post_init__(self) -> None:
        if self.price_cents < 0:
            raise ValueError("price_cents must be >= 0")
        if self.quantity < 1:
            raise ValueError("quantity must be >= 1")


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:
        self.items.append(item)

    def subtotal_cents(self) -> int:
        return sum(i.price_cents * i.quantity for i in self.items)

    def total_cents(self, discount_percent: int = 0) -> int:
        if not 0 <= discount_percent <= 100:
            raise ValueError("discount_percent must be between 0 and 100")
        subtotal = self.subtotal_cents()
        return subtotal - (subtotal * discount_percent) // 100
