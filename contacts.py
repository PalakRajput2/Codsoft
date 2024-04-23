class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def display_contact(contact):
    print("\nContact Details:")
    print("Name:", contact.name)
    print("Phone:", contact.phone)
    print("Email:", contact.email)
    print("Address:", contact.address)

def main():
    contact_book = ContactBook()

    while True:
        print("*********************************")
        print("\nWelcome to the Contact Book!")
        print("Press 1. to Add Contact")
        print("Press 2. to View Contact List")
        print("Press 3. to Search Contact")
        print("Press 4. to Update Contact")
        print("Press 5. to Delete Contact")
        print("Press 6. to Exit")

        choice = input("Enter your choice to check details: ")

        if choice == '1':
            print("\nEnter contact details:")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if not results:
                print("No matching contacts found.")
            else:
                print("Matching Contacts:")
                for contact in results:
                    print(contact.name, "-", contact.phone)

        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("Enter index of contact to update: ")) - 1
                if index < 0 or index >= len(contact_book.contacts):
                    print("Invalid index!")
                    continue
                print("\nEnter updated contact details:")
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                new_contact = Contact(name, phone, email, address)
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid index.")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("Enter index of contact to delete: ")) - 1
                if index < 0 or index >= len(contact_book.contacts):
                    print("Invalid index!")
                    continue
                contact_book.delete_contact(index)
                print("Contact deleted successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid index.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
