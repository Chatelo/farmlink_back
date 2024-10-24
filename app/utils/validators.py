import re
from typing import Tuple


def validate_phone(phone: str) -> Tuple[bool, str]:
    """Validate phone number format."""
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    if not pattern.match(phone):
        return False, "Invalid phone number format"
    return True, ""

def validate_password(password: str) -> Tuple[bool, str]:
    """
    Validate password strength.
    Requirements:
    - At least 8 characters
    - Contains uppercase and lowercase letters
    - Contains at least one number
    - Contains at least one special character
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character"
    
    return True, ""

def validate_coordinates(lat: float, lon: float) -> bool:
    """Validate geographical coordinates."""
    return -90 <= lat <= 90 and -180 <= lon <= 180