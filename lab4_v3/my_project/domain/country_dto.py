from dataclasses import dataclass
from typing import Optional

@dataclass
class CountryDTO:
    country_id: Optional[int] = None
    country_name: str = ""
    country_code: str = ""
    
    def to_dict(self):
        return {
            'country_id': self.country_id,
            'country_name': self.country_name,
            'country_code': self.country_code
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            country_id=data.get('country_id'),
            country_name=data.get('country_name', ''),
            country_code=data.get('country_code', '')
        )
