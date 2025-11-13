from typing import List, Optional
from my_project.app.dao.app_dao import AppDAO
from my_project.domain.app_dto import AppDTO

class AppService:
    def __init__(self):
        self.app_dao = AppDAO()
    
    def get_all_apps(self) -> List[AppDTO]:
        """Отримати всі додатки"""
        return self.app_dao.get_all()
    
    def get_app_by_id(self, app_id: int) -> Optional[AppDTO]:
        """Отримати додаток за ID"""
        return self.app_dao.get_by_id(app_id)
    
    def create_app(self, app_data: dict) -> int:
        """Створити новий додаток"""
        app = AppDTO.from_dict(app_data)
        return self.app_dao.create(app)
    
    def update_app(self, app_id: int, app_data: dict) -> bool:
        """Оновити додаток"""
        app = AppDTO.from_dict(app_data)
        app.app_id = app_id
        return self.app_dao.update(app)
    
    def delete_app(self, app_id: int) -> bool:
        """Видалити додаток"""
        return self.app_dao.delete(app_id)
    
    def get_reviews_by_app(self, app_id: int) -> List[dict]:
        """Отримати відгуки додатку (M:1 зв'язок)"""
        return self.app_dao.get_reviews_by_app(app_id)
    
    def get_installations_by_app(self, app_id: int) -> List[dict]:
        """Отримати встановлення додатку (M:1 зв'язок)"""
        return self.app_dao.get_installations_by_app(app_id)
    
    def get_versions_by_app(self, app_id: int) -> List[dict]:
        """Отримати версії додатку (M:1 зв'язок)"""
        return self.app_dao.get_versions_by_app(app_id)
    
    def get_screenshots_by_app(self, app_id: int) -> List[dict]:
        """Отримати скріншоти додатку (M:1 зв'язок)"""
        return self.app_dao.get_screenshots_by_app(app_id)
