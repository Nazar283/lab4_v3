from dataclasses import dataclass
from typing import Optional

@dataclass
class CategoryDTO:
    category_id: Optional[int] = None
    category_name: str = ""
    parent_category_id: Optional[int] = None
    
    def to_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'parent_category_id': self.parent_category_id
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            category_id=data.get('category_id'),
            category_name=data.get('category_name', ''),
            parent_category_id=data.get('parent_category_id')
        )
