from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice


def main():
    while True:
        print("\n========== Coffee Shop ==========")
        print("1. نمایش منوی کافه")
        print("2. ثبت سفارش")
        print("3. نمایش سفارش‌ها")
        print("4. محاسبه مبلغ کل")
        print("5. چاپ فاکتور")
        print("6. خروج")
        choice = input("انتخاب شما: ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            print(f"مبلغ کل: {calculate_total():,} تومان")
        elif choice == "5":
            print_invoice()
        elif choice == "6":
            print("خدانگهدار!")
            break
        else:
            print("گزینه نامعتبر است، دوباره تلاش کنید.")


if __name__ == "__main__":
    main()
