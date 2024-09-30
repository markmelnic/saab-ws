class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # Use AI code completion to implement this method
        pass

    def remove_contact(self, name):
        # Use AI code completion to implement this method
        pass

    def find_contact(self, name):
        # Use AI code completion to implement this method
        pass

# Example usage
contact_list = ContactList()
contact_list.add_contact(Contact("Alice", "123-456-7890"))
contact_list.add_contact(Contact("Bob", "987-654-3210"))
print("Contacts after adding Alice and Bob:")
for contact in contact_list.contacts:
    print(f"{contact.name}: {contact.phone}")

contact_list.remove_contact("Alice")
print("Contacts after removing Alice:")
for contact in contact_list.contacts:
    print(f"{contact.name}: {contact.phone}")

found_contact = contact_list.find_contact("Bob")
if found_contact:
    print(f"Found contact: {found_contact.name}: {found_contact.phone}")
else:
    print("Contact not found.")
