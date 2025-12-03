import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.app_dto import AppDTO

class AppDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[AppDTO]:
        """Отримати всі додатки"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Apps ORDER BY app_name")
            results = cursor.fetchall()
            return [AppDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, app_id: int) -> Optional[AppDTO]:
        """Отримати додаток за ID"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Apps WHERE app_id = %s", (app_id,))
            result = cursor.fetchone()
            return AppDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, app: AppDTO) -> int:
        """Створити новий додаток"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Apps (app_name, description, price, developer_id, category_id, release_date) VALUES (%s, %s, %s, %s, %s, %s)",
                (app.app_name, app.description, app.price, app.developer_id, app.category_id, app.release_date)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, app: AppDTO) -> bool:
        """Оновити додаток"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Apps SET app_name = %s, description = %s, price = %s, developer_id = %s, category_id = %s, release_date = %s WHERE app_id = %s",
                (app.app_name, app.description, app.price, app.developer_id, app.category_id, app.release_date, app.app_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, app_id: int) -> bool:
        """Видалити додаток"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Apps WHERE app_id = %s", (app_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_reviews_by_app(self, app_id: int) -> List[dict]:
        """Отримати відгуки додатку (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT r.*, u.username, a.app_name 
                FROM Reviews r 
                LEFT JOIN Users u ON r.user_id = u.user_id 
                LEFT JOIN Apps a ON r.app_id = a.app_id 
                WHERE r.app_id = %s
                ORDER BY r.review_date DESC
            """, (app_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def get_installations_by_app(self, app_id: int) -> List[dict]:
        """Отримати встановлення додатку (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT i.*, u.username, a.app_name, av.version_name 
                FROM Installations i 
                LEFT JOIN Users u ON i.user_id = u.user_id 
                LEFT JOIN Apps a ON i.app_id = a.app_id 
                LEFT JOIN AppVersions av ON i.installed_version_id = av.version_id 
                WHERE i.app_id = %s
                ORDER BY i.install_date DESC
            """, (app_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def get_versions_by_app(self, app_id: int) -> List[dict]:
        """Отримати версії додатку (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT av.*, a.app_name 
                FROM AppVersions av 
                LEFT JOIN Apps a ON av.app_id = a.app_id 
                WHERE av.app_id = %s
                ORDER BY av.release_date DESC
            """, (app_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def get_screenshots_by_app(self, app_id: int) -> List[dict]:
        """Отримати скріншоти додатку (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT s.*, a.app_name 
                FROM Screenshots s 
                LEFT JOIN Apps a ON s.app_id = a.app_id 
                WHERE s.app_id = %s
                ORDER BY s.display_order ASC
            """, (app_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
