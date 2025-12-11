from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ReviewDTO:
    review_id: Optional[int] = None
    app_id: int = 0
    user_id: int = 0
    rating: int = 0
    review_text: Optional[str] = None
    review_date: Optional[datetime] = None
    
    def to_dict(self):
        return {
            'review_id': self.review_id,
            'app_id': self.app_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'review_text': self.review_text,
            'review_date': self.review_date.isoformat() if self.review_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        review_date = data.get('review_date')
        if review_date:
            if isinstance(review_date, str):
                review_date = datetime.fromisoformat(review_date)
            elif hasattr(review_date, 'isoformat'):
                # Якщо це вже datetime об'єкт
                pass
            else:
                review_date = None
        
        return cls(
            review_id=data.get('review_id'),
            app_id=int(data.get('app_id', 0)),
            user_id=int(data.get('user_id', 0)),
            rating=int(data.get('rating', 0)),
            review_text=data.get('review_text'),
            review_date=review_date
        )
