from typing import List, Optional
from my_project.country.dao.country_dao import CountryDAO
from my_project.domain.country_dto import CountryDTO

class CountryService:
    def __init__(self):
        self.country_dao = CountryDAO()
    
    def get_all_countries(self) -> List[CountryDTO]:
        """Отримати всі країни"""
        return self.country_dao.get_all()
    
    def get_country_by_id(self, country_id: int) -> Optional[CountryDTO]:
        """Отримати країну за ID"""
        return self.country_dao.get_by_id(country_id)
    
    def create_country(self, country_data: dict) -> int:
        """Створити нову країну"""
        country = CountryDTO.from_dict(country_data)
        return self.country_dao.create(country)
    
    def update_country(self, country_id: int, country_data: dict) -> bool:
        """Оновити країну"""
        country = CountryDTO.from_dict(country_data)
        country.country_id = country_id
        return self.country_dao.update(country)
    
    def delete_country(self, country_id: int) -> bool:
        """Видалити країну"""
        return self.country_dao.delete(country_id)
    
    def get_users_by_country(self, country_id: int) -> List[dict]:
        """Отримати користувачів по країні (M:1 зв'язок)"""
        return self.country_dao.get_users_by_country(country_id)
