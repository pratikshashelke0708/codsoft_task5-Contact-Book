# Simple Contact Book in Python with Update Feature

# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()
    else:
        print("No contacts found.\n")

# Function to search for a contact
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}\n")
    else:
        print(f"Contact '{name}' not found.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"Contact '{name}' not found.\n")

# Function to update a contact
def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        new_phone = input(f"Enter new phone number for '{name}': ")
        contacts[name] = new_phone
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print(f"Contact '{name}' not found.\n")

# Main program loop
while True:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        update_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1-6.\n")
