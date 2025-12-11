from typing import List, Optional
from my_project.category.dao.category_dao import CategoryDAO
from my_project.domain.category_dto import CategoryDTO

class CategoryService:
    def __init__(self):
        self.category_dao = CategoryDAO()
    
    def get_all_categories(self) -> List[CategoryDTO]:
        return self.category_dao.get_all()
    
    def get_category_by_id(self, category_id: int) -> Optional[CategoryDTO]:
        return self.category_dao.get_by_id(category_id)
    
    def create_category(self, category_data: dict) -> int:
        category = CategoryDTO.from_dict(category_data)
        return self.category_dao.create(category)
    
    def update_category(self, category_id: int, category_data: dict) -> bool:
        category = CategoryDTO.from_dict(category_data)
        category.category_id = category_id
        return self.category_dao.update(category)
    
    def delete_category(self, category_id: int) -> bool:
        return self.category_dao.delete(category_id)
    
    def get_apps_by_category(self, category_id: int) -> List[dict]:
        return self.category_dao.get_apps_by_category(category_id)
