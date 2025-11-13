from dataclasses import dataclass
from typing import Optional

@dataclass
class DeveloperDTO:
    developer_id: Optional[int] = None
    developer_name: str = ""
    website: Optional[str] = None
    contact_email: str = ""
    
    def to_dict(self):
        return {
            'developer_id': self.developer_id,
            'developer_name': self.developer_name,
            'website': self.website,
            'contact_email': self.contact_email
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            developer_id=data.get('developer_id'),
            developer_name=data.get('developer_name', ''),
            website=data.get('website'),
            contact_email=data.get('contact_email', '')
        )
