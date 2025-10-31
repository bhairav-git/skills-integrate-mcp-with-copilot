"""Authentication utilities for the school system."""

import json
import hashlib
from pathlib import Path
from typing import Optional

def hash_password(password: str) -> str:
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_teacher(username: str, password: str) -> Optional[dict]:
    """Verify teacher credentials against the JSON file.
    
    Returns:
        dict: Teacher info if credentials are valid
        None: If credentials are invalid
    """
    try:
        teachers_file = Path(__file__).parent / 'teachers.json'
        with open(teachers_file, 'r') as f:
            data = json.load(f)
            
        password_hash = hash_password(password)
        
        for teacher in data['teachers']:
            if teacher['username'] == username and teacher['password_hash'] == password_hash:
                return {
                    'username': teacher['username'],
                    'name': teacher['name']
                }
                
        return None
    except Exception as e:
        print(f"Auth error: {e}")
        return None