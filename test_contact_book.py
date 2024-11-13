# test_contact_book.py
import pytest
from contact_book import ContactBook

def test_add_contact():
    contact_book = ContactBook()
    
    # Test valid contact
    result = contact_book.add_contact("Alice", "123-456-7890")
    assert result == "Contact 'Alice' added with phone number 123-456-7890."
    assert contact_book.view_contacts() == {"Alice": "123-456-7890"}

    # Intentional failure: Expecting a wrong phone number to simulate a failure
    assert contact_book.view_contacts() == {"Alice": "999-999-9999"}  # This will fail

    # Test adding a contact with invalid data

    # Test with empty name
    result = contact_book.add_contact("", "987-654-3210")
    assert result == "Contact '' added with phone number 987-654-3210."
    assert contact_book.view_contacts() == {"Alice": "123-456-7890", "": "987-654-3210"}  # Empty name should be accepted

    # Test with empty phone number
    result = contact_book.add_contact("Bob", "")
    assert result == "Contact 'Bob' added with phone number ."
    assert contact_book.view_contacts() == {"Alice": "123-456-7890", "": "987-654-3210", "Bob": ""}  # Empty phone number should be accepted

    # Test with None as name
    result = contact_book.add_contact(None, "111-222-3333")
    assert result == "Contact 'None' added with phone number 111-222-3333."
    assert contact_book.view_contacts() == {"Alice": "123-456-7890", "": "987-654-3210", "Bob": "", None: "111-222-3333"}  # None as name should be accepted

    # Test with None as phone number
    result = contact_book.add_contact("Charlie", None)
    assert result == "Contact 'Charlie' added with phone number None."
    assert contact_book.view_contacts() == {"Alice": "123-456-7890", "": "987-654-3210", "Bob": "", None: "111-222-3333", "Charlie": None}  # None as phone number should be accepted

def test_view_contacts_empty():
    contact_book = ContactBook()
    # Expect an empty dictionary when no contacts are added
    assert contact_book.view_contacts() == {}

def test_view_contacts():
    contact_book = ContactBook()
    contact_book.add_contact("Bob", "234-567-8901")
    contact_book.add_contact("Charlie", "345-678-9012")
    contacts = contact_book.view_contacts()
    assert contacts == {
        "Bob": "234-567-8901",
        "Charlie": "345-678-9012"
    }

def test_delete_contact():
    contact_book = ContactBook()
    contact_book.add_contact("Dave", "456-789-0123")
    
    # Delete existing contact
    result = contact_book.delete_contact("Dave")
    assert result == "Contact 'Dave' deleted."
    assert contact_book.view_contacts() == {}

    # Try deleting a contact that doesn't exist
    result = contact_book.delete_contact("Eve")
    assert result == "Contact 'Eve' not found."
