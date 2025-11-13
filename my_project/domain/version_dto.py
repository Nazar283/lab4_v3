from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class AppVersionDTO:
    version_id: Optional[int] = None
    app_id: int = 0
    version_name: str = ""
    release_notes: Optional[str] = None
    release_date: Optional[datetime] = None
    
    def to_dict(self):
        return {
            'version_id': self.version_id,
            'app_id': self.app_id,
            'version_name': self.version_name,
            'release_notes': self.release_notes,
            'release_date': self.release_date.isoformat() if self.release_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        release_date = data.get('release_date')
        if release_date:
            if isinstance(release_date, str):
                release_date = datetime.fromisoformat(release_date)
            elif hasattr(release_date, 'isoformat'):
                # Якщо це вже datetime об'єкт
                pass
            else:
                release_date = None
        
        return cls(
            version_id=data.get('version_id'),
            app_id=int(data.get('app_id', 0)),
            version_name=data.get('version_name', ''),
            release_notes=data.get('release_notes'),
            release_date=release_date
        )
