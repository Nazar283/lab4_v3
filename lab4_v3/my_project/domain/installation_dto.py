from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class InstallationDTO:
    installation_id: Optional[int] = None
    user_id: int = 0
    app_id: int = 0
    installed_version_id: Optional[int] = None
    install_date: Optional[datetime] = None
    
    def to_dict(self):
        return {
            'installation_id': self.installation_id,
            'user_id': self.user_id,
            'app_id': self.app_id,
            'installed_version_id': self.installed_version_id,
            'install_date': self.install_date.isoformat() if self.install_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        install_date = data.get('install_date')
        if install_date:
            if isinstance(install_date, str):
                install_date = datetime.fromisoformat(install_date)
            elif hasattr(install_date, 'isoformat'):
                # Якщо це вже datetime об'єкт
                pass
            else:
                install_date = None
        
        return cls(
            installation_id=data.get('installation_id'),
            user_id=int(data.get('user_id', 0)),
            app_id=int(data.get('app_id', 0)),
            installed_version_id=data.get('installed_version_id'),
            install_date=install_date
        )
