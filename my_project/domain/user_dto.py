from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class UserDTO:
    user_id: Optional[int] = None
    email: str = ""
    username: str = ""
    password_hash: str = ""
    date_joined: Optional[datetime] = None
    country_id: Optional[int] = None
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username': self.username,
            'password_hash': self.password_hash,
            'date_joined': self.date_joined.isoformat() if self.date_joined else None,
            'country_id': self.country_id
        }
    
    @classmethod
    def from_dict(cls, data):
        date_joined = data.get('date_joined')
        if date_joined:
            if isinstance(date_joined, str):
                date_joined = datetime.fromisoformat(date_joined)
            elif hasattr(date_joined, 'isoformat'):
                # Якщо це вже datetime об'єкт
                pass
            else:
                date_joined = None
        
        return cls(
            user_id=data.get('user_id'),
            email=data.get('email', ''),
            username=data.get('username', ''),
            password_hash=data.get('password_hash', ''),
            date_joined=date_joined,
            country_id=data.get('country_id')
        )
