import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.country_dto import CountryDTO

class CountryDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[CountryDTO]:
        """Отримати всі країни"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Countries ORDER BY country_name")
            results = cursor.fetchall()
            return [CountryDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, country_id: int) -> Optional[CountryDTO]:
        """Отримати країну за ID"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Countries WHERE country_id = %s", (country_id,))
            result = cursor.fetchone()
            return CountryDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, country: CountryDTO) -> int:
        """Створити нову країну"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Countries (country_name, country_code) VALUES (%s, %s)",
                (country.country_name, country.country_code)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, country: CountryDTO) -> bool:
        """Оновити країну"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Countries SET country_name = %s, country_code = %s WHERE country_id = %s",
                (country.country_name, country.country_code, country.country_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, country_id: int) -> bool:
        """Видалити країну"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Countries WHERE country_id = %s", (country_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_users_by_country(self, country_id: int) -> List[dict]:
        """Отримати користувачів по країні (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT u.*, c.country_name 
                FROM Users u 
                LEFT JOIN Countries c ON u.country_id = c.country_id 
                WHERE u.country_id = %s
                ORDER BY u.username
            """, (country_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
