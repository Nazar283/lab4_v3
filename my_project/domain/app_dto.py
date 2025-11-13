from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class AppDTO:
    app_id: Optional[int] = None
    app_name: str = ""
    description: Optional[str] = None
    price: float = 0.0
    developer_id: int = 0
    category_id: int = 0
    release_date: Optional[date] = None
    
    def to_dict(self):
        return {
            'app_id': self.app_id,
            'app_name': self.app_name,
            'description': self.description,
            'price': self.price,
            'developer_id': self.developer_id,
            'category_id': self.category_id,
            'release_date': self.release_date.isoformat() if self.release_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        release_date = data.get('release_date')
        if release_date:
            if isinstance(release_date, str):
                release_date = date.fromisoformat(release_date)
            elif hasattr(release_date, 'date'):
                release_date = release_date.date()
        
        return cls(
            app_id=data.get('app_id'),
            app_name=data.get('app_name', ''),
            description=data.get('description'),
            price=float(data.get('price', 0.0)),
            developer_id=int(data.get('developer_id', 0)),
            category_id=int(data.get('category_id', 0)),
            release_date=release_date
        )
