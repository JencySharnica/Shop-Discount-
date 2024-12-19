# Shop Discount Program
purchase_amount = float(input("Enter purchase amount: $"))

if purchase_amount > 1000:
    discount = 0.20
    print(f"You get a 20% discount")
    print(f"Final amount: ${purchase_amount * (1 - discount):.2f}")
elif 500 <= purchase_amount <= 1000:
    discount = 0.10
    print(f"You get a 10% discount")
    print(f"Final amount: ${purchase_amount * (1 - discount):.2f}")
else:
    print(f"No discount")
    print(f"Final amount: ${purchase_amount:.2f}")