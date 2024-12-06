class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")

    def search_contact(self):
        name = input("Enter the name of the contact to search: ")
        if name in self.contacts:
            details = self.contacts[name]
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
        else:
            print(f"Contact with the name {name} not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact with the name {name} not found.")

    def menu(self):
        while True:
            print("\n--- Contact Book Menu ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice. Please try again.")

# Driver code
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
