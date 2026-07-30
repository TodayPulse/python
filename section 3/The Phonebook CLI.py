# The "Phonebook" CLI: 
# Create a small program that uses a dictionary to store contact names and phone numbers. 
# Allow the user to "Add" a contact, "Delete" a contact, and "Lookup" a contact. 
# Use a list to store the names in order of addition.


def phonebook_cli():
    """
    A command-line interface (CLI) phonebook program that uses a dictionary 
    for storage and a list to maintain the order of added contacts.
    """
    phonebook = {}
    contact_order = []
    
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Lookup Contact")
        print("3. Delete Contact")
        print("4. View All Contacts (In Order of Addition)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            
            if not name or not phone:
                print("Name and phone number cannot be empty.")
                continue
                
            # If the contact is completely new, add name to our order list
            if name not in phonebook:
                contact_order.append(name)
                
            # Add or update the dictionary
            phonebook[name] = phone
            print(f"Successfully added/updated: {name}")
            
        elif choice == "2":
            name = input("Enter name to lookup: ").strip()
            
            if name in phonebook:
                print(f"Found! {name}: {phonebook[name]}")
            else:
                print(f"Contact '{name}' not found in the phonebook.")
                
        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            
            if name in phonebook:
                del phonebook[name]
                contact_order.remove(name)
                print(f"Successfully deleted: {name}")
            else:
                print(f"Contact '{name}' not found.")
                
        elif choice == "4":
            if not contact_order:
                print("The phonebook is currently empty.")
            else:
                print("\nPhonebook Contacts:")
                for name in contact_order:
                    print(f"  - {name}: {phonebook[name]}")
                    
        elif choice == "5":
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# --- How to Run ---
# To run the interactive CLI program, simply uncomment the line below:
phonebook_cli()