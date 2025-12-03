import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.user_dto import UserDTO

class UserDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[UserDTO]:
        """Отримати всіх користувачів"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Users ORDER BY username")
            results = cursor.fetchall()
            return [UserDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, user_id: int) -> Optional[UserDTO]:
        """Отримати користувача за ID"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            return UserDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, user: UserDTO) -> int:
        """Створити нового користувача"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Users (email, username, password_hash, country_id) VALUES (%s, %s, %s, %s)",
                (user.email, user.username, user.password_hash, user.country_id)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, user: UserDTO) -> bool:
        """Оновити користувача"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Users SET email = %s, username = %s, password_hash = %s, country_id = %s WHERE user_id = %s",
                (user.email, user.username, user.password_hash, user.country_id, user.user_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, user_id: int) -> bool:
        """Видалити користувача"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_reviews_by_user(self, user_id: int) -> List[dict]:
        """Отримати відгуки користувача (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT r.*, a.app_name, u.username 
                FROM Reviews r 
                LEFT JOIN Apps a ON r.app_id = a.app_id 
                LEFT JOIN Users u ON r.user_id = u.user_id 
                WHERE r.user_id = %s
                ORDER BY r.review_date DESC
            """, (user_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def get_installations_by_user(self, user_id: int) -> List[dict]:
        """Отримати встановлення користувача (M:1 зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT i.*, a.app_name, av.version_name 
                FROM Installations i 
                LEFT JOIN Apps a ON i.app_id = a.app_id 
                LEFT JOIN AppVersions av ON i.installed_version_id = av.version_id 
                WHERE i.user_id = %s
                ORDER BY i.install_date DESC
            """, (user_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
