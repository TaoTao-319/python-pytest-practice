from collections.abc import Iterable, Mapping
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN


def calculate_cart_total(items: Iterable[Mapping[str, object]]) -> Decimal:
    total = Decimal("0.00")

    for index, item in enumerate(items, start=1):
        try:
            unit_price = Decimal(str(item["unit_price"]))


        except (KeyError, InvalidOperation, TypeError) as error:
            raise ValueError(f"第 {index} 个商品的 unit_price 无效") from error


        if not unit_price.is_finite() or unit_price < 0:
            raise ValueError(f"第 {index} 个商品的 unit_price 必须是非负数")

        quantity = item.get("quantity")


        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            raise ValueError(f"第 {index} 个商品的 quantity 必须是非负整数")

        total += unit_price * quantity


    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
