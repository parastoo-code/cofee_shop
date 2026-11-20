from Order import orders


def calculate_total():
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total


def calculate_discount(total):
    if total > 1000000:
        return total * 10 // 100
    return 0


def print_invoice():
    if len(orders) == 0:
        print("هنوز سفارشی ثبت نشده است؛ فاکتوری وجود ندارد.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount

    print("\n========== فاکتور ==========")
    for order in orders:
        print(f"{order['name']:<10} × {order['quantity']}")
    print("----------------------------")
    print(f"مبلغ کل       : {total:,} تومان")
    print(f"تخفیف         : {discount:,} تومان")
    print(f"مبلغ قابل پرداخت: {final_amount:,} تومان")
    print("============================")
