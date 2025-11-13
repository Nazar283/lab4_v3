from dataclasses import dataclass
from typing import Optional

@dataclass
class PermissionDTO:
    permission_id: Optional[int] = None
    permission_name: str = ""
    description: Optional[str] = None
    
    def to_dict(self):
        return {
            'permission_id': self.permission_id,
            'permission_name': self.permission_name,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            permission_id=data.get('permission_id'),
            permission_name=data.get('permission_name', ''),
            description=data.get('description')
        )
