from Menu import menu

orders = []


def add_order():
    name = input("نام محصول: ").strip().lower()

    if name not in menu:
        print("این محصول در منوی کافه وجود ندارد.")
        return

    try:
        quantity = int(input("تعداد: "))
    except ValueError:
        print("تعداد باید یک عدد صحیح باشد.")
        return

    if quantity <= 0:
        print("تعداد باید بیشتر از صفر باشد.")
        return

    orders.append({"name": name, "price": menu[name], "quantity": quantity})
    print(f"{quantity} عدد {name} به سفارش‌ها اضافه شد.")


def show_orders():
    if len(orders) == 0:
        print("هنوز سفارشی ثبت نشده است.")
        return

    print("\n------ سفارش‌ها ------")
    for i, order in enumerate(orders, start=1):
        print(f"{i}. {order['name']} | قیمت: {order['price']:,} | تعداد: {order['quantity']}")
    print("----------------------")
