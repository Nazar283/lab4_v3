from typing import List, Optional
from my_project.developer.dao.developer_dao import DeveloperDAO
from my_project.domain.developer_dto import DeveloperDTO

class DeveloperService:
    def __init__(self):
        self.developer_dao = DeveloperDAO()
    
    def get_all_developers(self) -> List[DeveloperDTO]:
        return self.developer_dao.get_all()
    
    def get_developer_by_id(self, developer_id: int) -> Optional[DeveloperDTO]:
        return self.developer_dao.get_by_id(developer_id)
    
    def create_developer(self, developer_data: dict) -> int:
        developer = DeveloperDTO.from_dict(developer_data)
        return self.developer_dao.create(developer)
    
    def update_developer(self, developer_id: int, developer_data: dict) -> bool:
        developer = DeveloperDTO.from_dict(developer_data)
        developer.developer_id = developer_id
        return self.developer_dao.update(developer)
    
    def delete_developer(self, developer_id: int) -> bool:
        return self.developer_dao.delete(developer_id)
    
    def get_apps_by_developer(self, developer_id: int) -> List[dict]:
        return self.developer_dao.get_apps_by_developer(developer_id)
