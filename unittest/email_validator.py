import re
import unittest

def validate_email(email):
    """
    Validate the given email address based on the following rules:
    1. Proper email format such as presence of "@" and absence of spaces in the address.
    2. Presence of valid email providers such as yahoo, gmail, and outlook.
    3. Ensure the email address is not from disposable email providers such as yopmail.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    ###regular expressionfor valid email format
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    ##if email matches the pattern
    if not email_pattern.match(email):
        return False
    
    #if email provider is valid (yahoo, gmail, outlook)
    valid_providers = ['yahoo.com', 'gmail.com', 'outlook.com']
    provider = email.split('@')[1]
    if provider not in valid_providers:
        return False
    
    # Check if email is from a valid provider
    disposable_providers = ['yopmail.com']
    if provider in disposable_providers:
        return False
    
    return True



class TestEmailValidation(unittest.TestCase):
    """Test cases for email address validation."""
    
    def test_valid_emails(self):
        """Test valid email addresses."""
        self.assertTrue(validate_email('example@gmail.com'))
        self.assertTrue(validate_email('test@outlook.com'))
        self.assertTrue(validate_email('user@yahoo.com'))
        
    def test_invalid_emails(self):
        """Test invalid email addresses."""
        self.assertFalse(validate_email('invalid.email'))
        self.assertFalse(validate_email('invalid@yopmail.com'))
        self.assertFalse(validate_email('user@example.com '))
        self.assertFalse(validate_email('user@@gmail.com'))
        
if __name__ == '__main__':
    unittest.main()
