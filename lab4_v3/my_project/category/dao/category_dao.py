import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.category_dto import CategoryDTO

class CategoryDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[CategoryDTO]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Categories ORDER BY category_name")
            results = cursor.fetchall()
            return [CategoryDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, category_id: int) -> Optional[CategoryDTO]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Categories WHERE category_id = %s", (category_id,))
            result = cursor.fetchone()
            return CategoryDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, category: CategoryDTO) -> int:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Categories (category_name, parent_category_id) VALUES (%s, %s)",
                (category.category_name, category.parent_category_id)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, category: CategoryDTO) -> bool:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Categories SET category_name = %s, parent_category_id = %s WHERE category_id = %s",
                (category.category_name, category.parent_category_id, category.category_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, category_id: int) -> bool:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Categories WHERE category_id = %s", (category_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_apps_by_category(self, category_id: int) -> List[dict]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT a.*, c.category_name, d.developer_name 
                FROM Apps a 
                LEFT JOIN Categories c ON a.category_id = c.category_id 
                LEFT JOIN Developers d ON a.developer_id = d.developer_id 
                WHERE a.category_id = %s
                ORDER BY a.app_name
            """, (category_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
