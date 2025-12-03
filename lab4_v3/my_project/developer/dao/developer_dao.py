import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.developer_dto import DeveloperDTO

class DeveloperDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[DeveloperDTO]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Developers ORDER BY developer_name")
            results = cursor.fetchall()
            return [DeveloperDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, developer_id: int) -> Optional[DeveloperDTO]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Developers WHERE developer_id = %s", (developer_id,))
            result = cursor.fetchone()
            return DeveloperDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, developer: DeveloperDTO) -> int:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Developers (developer_name, website, contact_email) VALUES (%s, %s, %s)",
                (developer.developer_name, developer.website, developer.contact_email)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, developer: DeveloperDTO) -> bool:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Developers SET developer_name = %s, website = %s, contact_email = %s WHERE developer_id = %s",
                (developer.developer_name, developer.website, developer.contact_email, developer.developer_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, developer_id: int) -> bool:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Developers WHERE developer_id = %s", (developer_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_apps_by_developer(self, developer_id: int) -> List[dict]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT a.*, d.developer_name, c.category_name 
                FROM Apps a 
                LEFT JOIN Developers d ON a.developer_id = d.developer_id 
                LEFT JOIN Categories c ON a.category_id = c.category_id 
                WHERE a.developer_id = %s
                ORDER BY a.app_name
            """, (developer_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
