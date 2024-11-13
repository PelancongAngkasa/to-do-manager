class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Contact '{name}' added with phone number {phone}."

    def view_contacts(self):
        return self.contacts

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' deleted."
        else:
            return f"Contact '{name}' not found."

def main():
    contact_book = ContactBook()

    while True:
        print("\nSimple Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contact_book.add_contact(name, phone)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
