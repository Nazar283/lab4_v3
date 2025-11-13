from typing import List, Optional
from my_project.user.dao.user_dao import UserDAO
from my_project.domain.user_dto import UserDTO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()
    
    def get_all_users(self) -> List[UserDTO]:
        """Отримати всіх користувачів"""
        return self.user_dao.get_all()
    
    def get_user_by_id(self, user_id: int) -> Optional[UserDTO]:
        """Отримати користувача за ID"""
        return self.user_dao.get_by_id(user_id)
    
    def create_user(self, user_data: dict) -> int:
        """Створити нового користувача"""
        user = UserDTO.from_dict(user_data)
        return self.user_dao.create(user)
    
    def update_user(self, user_id: int, user_data: dict) -> bool:
        """Оновити користувача"""
        user = UserDTO.from_dict(user_data)
        user.user_id = user_id
        return self.user_dao.update(user)
    
    def delete_user(self, user_id: int) -> bool:
        """Видалити користувача"""
        return self.user_dao.delete(user_id)
    
    def get_reviews_by_user(self, user_id: int) -> List[dict]:
        """Отримати відгуки користувача (M:1 зв'язок)"""
        return self.user_dao.get_reviews_by_user(user_id)
    
    def get_installations_by_user(self, user_id: int) -> List[dict]:
        """Отримати встановлення користувача (M:1 зв'язок)"""
        return self.user_dao.get_installations_by_user(user_id)
