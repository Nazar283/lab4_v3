from dataclasses import dataclass
from typing import Optional

@dataclass
class ScreenshotDTO:
    screenshot_id: Optional[int] = None
    app_id: int = 0
    image_url: str = ""
    display_order: Optional[int] = None
    
    def to_dict(self):
        return {
            'screenshot_id': self.screenshot_id,
            'app_id': self.app_id,
            'image_url': self.image_url,
            'display_order': self.display_order
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            screenshot_id=data.get('screenshot_id'),
            app_id=int(data.get('app_id', 0)),
            image_url=data.get('image_url', ''),
            display_order=data.get('display_order')
        )
