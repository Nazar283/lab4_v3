from typing import List, Optional
from my_project.review.dao.review_dao import ReviewDAO
from my_project.domain.review_dto import ReviewDTO

class ReviewService:
    def __init__(self):
        self.review_dao = ReviewDAO()
    
    def get_all_reviews(self) -> List[ReviewDTO]:
        """Отримати всі відгуки"""
        return self.review_dao.get_all()
    
    def get_review_by_id(self, review_id: int) -> Optional[ReviewDTO]:
        """Отримати відгук за ID"""
        return self.review_dao.get_by_id(review_id)
    
    def create_review(self, review_data: dict) -> int:
        """Створити новий відгук"""
        review = ReviewDTO.from_dict(review_data)
        return self.review_dao.create(review)
    
    def update_review(self, review_id: int, review_data: dict) -> bool:
        """Оновити відгук"""
        review = ReviewDTO.from_dict(review_data)
        review.review_id = review_id
        return self.review_dao.update(review)
    
    def delete_review(self, review_id: int) -> bool:
        """Видалити відгук"""
        return self.review_dao.delete(review_id)
    
    def get_reviews_with_details(self) -> List[dict]:
        """Отримати відгуки з деталями (M:M зв'язок)"""
        return self.review_dao.get_reviews_with_details()
    
    def get_reviews_by_user_and_app(self, user_id: int, app_id: int) -> List[dict]:
        """Отримати відгуки конкретного користувача для конкретного додатку"""
        return self.review_dao.get_reviews_by_user_and_app(user_id, app_id)
