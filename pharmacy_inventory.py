import csv
import os

CSV_FILE = "medicines.csv"
FIELDS = ["ID", "Name", "Quantity", "Price"]


def load_medicines():
    """Load medicine records from the CSV file into a list of dictionaries."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

    medicines = []
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not row:
                continue
            try:
                medicines.append({
                    "ID": row["ID"].strip(),
                    "Name": row["Name"].strip(),
                    "Quantity": int(row["Quantity"]),
                    "Price": float(row["Price"])
                })
            except (KeyError, ValueError):
                print("Warning: A row in medicines.csv is invalid and was skipped.")
    return medicines


def save_medicines(medicines):
    """Write all medicine records back to the CSV file."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for medicine in medicines:
            writer.writerow(medicine)


def find_medicine(medicines, medicine_id):
    for medicine in medicines:
        if medicine["ID"].lower() == medicine_id.lower():
            return medicine
    return None


def next_medicine_id(medicines):
    numbers = []
    for medicine in medicines:
        medicine_id = medicine["ID"]
        if medicine_id.startswith("M") and medicine_id[1:].isdigit():
            numbers.append(int(medicine_id[1:]))
    return f"M{max(numbers, default=0) + 1}"


def add_medicine(medicines):
    print("\n--- Add Medicine ---")
    name = input("Enter medicine name: ").strip()
    if not name:
        print("Medicine name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Please enter a valid number for quantity and price.")
        return

    if quantity < 0 or price < 0:
        print("Negative quantity or price is not allowed.")
        return

    medicine = {
        "ID": next_medicine_id(medicines),
        "Name": name,
        "Quantity": quantity,
        "Price": price
    }
    medicines.append(medicine)
    save_medicines(medicines)
    print(
        f"Medicine added. ID: {medicine['ID']} | {medicine['Name']} | "
        f"Qty: {medicine['Quantity']} | Price: {medicine['Price']:.2f}"
    )


def view_medicines(medicines):
    print("\n--- Medicine List ---")
    if not medicines:
        print("No medicines found.")
        return

    print(f"{'ID':<8}{'Name':<22}{'Quantity':<12}{'Price':>10}")
    print("-" * 52)
    for medicine in medicines:
        print(
            f"{medicine['ID']:<8}{medicine['Name']:<22}"
            f"{medicine['Quantity']:<12}{medicine['Price']:>10.2f}"
        )


def sell_medicine(medicines):
    print("\n--- Sell Medicine ---")
    medicine_id = input("Enter medicine ID: ").strip()
    medicine = find_medicine(medicines, medicine_id)

    if medicine is None:
        print("Medicine not found.")
        return

    try:
        quantity_to_sell = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if quantity_to_sell <= 0:
        print("Selling quantity must be greater than zero.")
        return

    if quantity_to_sell > medicine["Quantity"]:
        print(f"Insufficient stock. Available: {medicine['Quantity']}")
        return

    bill = quantity_to_sell * medicine["Price"]
    medicine["Quantity"] -= quantity_to_sell
    save_medicines(medicines)

    print(f"Sold {quantity_to_sell} units. Bill: {bill:.2f}")
    print(f"Stock left: {medicine['Quantity']}")
    if medicine["Quantity"] == 0:
        print("Out of stock!")


def delete_medicine(medicines):
    print("\n--- Delete Medicine ---")
    medicine_id = input("Enter medicine ID to delete: ").strip()
    medicine = find_medicine(medicines, medicine_id)

    if medicine is None:
        print("Medicine not found.")
        return

    medicines.remove(medicine)
    save_medicines(medicines)
    print(f"Medicine {medicine_id.upper()} deleted.")


def low_stock_report(medicines):
    print("\n--- Low Stock Report ---")
    low_stock = [medicine for medicine in medicines if medicine["quantity"] < 10]

    if not low_stock:
        print("No low-stock medicines.")
        return

    for medicine in low_stock:
        print(
            f"{medicine['ID']} | {medicine['Name']} | "
            f"Qty: {medicine['Quantity']} (Low stock)"
        )


def inventory_value(medicines):
    total = sum(medicine["Quantity"] * medicine["Price"] for medicine in medicines)
    print(f"Total inventory value: {total:.2f}")


def main():
    medicines = load_medicines()

    while True:
        print("\n========== PHARMACY INVENTORY SYSTEM ==========")
        print("1. Add")
        print("2. View")
        print("3. Sell")
        print("4. Delete")
        print("5. Low stock report")
        print("6. Inventory value")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_medicine(medicines)
        elif choice == "2":
            view_medicines(medicines)
        elif choice == "3":
            sell_medicine(medicines)
        elif choice == "4":
            delete_medicine(medicines)
        elif choice == "5":
            low_stock_report(medicines)
        elif choice == "6":
            inventory_value(medicines)
        elif choice == "0":
            print("Thank you for using Pharmacy Inventory System!")
            break
        else:
            print("Invalid option. Please select 0 to 6.")


if __name__ == "__main__":
    main()