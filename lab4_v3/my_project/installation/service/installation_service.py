from typing import List, Optional
from my_project.installation.dao.installation_dao import InstallationDAO
from my_project.domain.installation_dto import InstallationDTO

class InstallationService:
    def __init__(self):
        self.installation_dao = InstallationDAO()
    
    def get_all_installations(self) -> List[InstallationDTO]:
        return self.installation_dao.get_all()
    
    def get_installation_by_id(self, installation_id: int) -> Optional[InstallationDTO]:
        return self.installation_dao.get_by_id(installation_id)
    
    def create_installation(self, installation_data: dict) -> int:
        installation = InstallationDTO.from_dict(installation_data)
        return self.installation_dao.create(installation)
    
    def update_installation(self, installation_id: int, installation_data: dict) -> bool:
        installation = InstallationDTO.from_dict(installation_data)
        installation.installation_id = installation_id
        return self.installation_dao.update(installation)
    
    def delete_installation(self, installation_id: int) -> bool:
        return self.installation_dao.delete(installation_id)
    
    def get_installations_with_details(self) -> List[dict]:
        return self.installation_dao.get_installations_with_details()
