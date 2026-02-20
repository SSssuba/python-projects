import csv
import os

FILENAME = "contacts.csv"

# Create file if not exists
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])

# Add new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("✅ Contact added successfully!\n")

# View all contacts
def view_contacts():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

        if len(contacts) <= 1:
            print("📂 No contacts found.\n")
            return

        print("\n📒 Contact List:")
        print("-" * 40)
        for row in contacts[1:]:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
        print()

# Search contact
def search_contact():
    search_term = input("Enter Name or Phone to search: ")
    found = False

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            if search_term.lower() in row[0].lower() or search_term in row[1]:
                print(f"\n🔎 Found: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}\n")
                found = True

    if not found:
        print("❌ Contact not found.\n")

# Update contact
def update_contact():
    search_name = input("Enter Name to update: ")
    updated = False
    rows = []

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for i in range(1, len(rows)):
        if rows[i][0].lower() == search_name.lower():
            print("Enter new details:")
            rows[i][0] = input("New Name: ")
            rows[i][1] = input("New Phone: ")
            rows[i][2] = input("New Email: ")
            updated = True
            break

    if updated:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("✅ Contact updated successfully!\n")
    else:
        print("❌ Contact not found.\n")

# Delete contact
def delete_contact():
    search_name = input("Enter Name to delete: ")
    deleted = False
    rows = []

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]  # Keep header

    for row in rows[1:]:
        if row[0].lower() != search_name.lower():
            new_rows.append(row)
        else:
            deleted = True

    if deleted:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
        print("🗑️ Contact deleted successfully!\n")
    else:
        print("❌ Contact not found.\n")

# Menu
def menu():
    initialize_file()

    while True:
        print("===== CONTACT BOOK MANAGER =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book Manager...")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

# Run program
if __name__ == "__main__":
    menu()