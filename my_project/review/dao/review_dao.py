import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.review_dto import ReviewDTO

class ReviewDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[ReviewDTO]:
        """Отримати всі відгуки"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Reviews ORDER BY review_date DESC")
            results = cursor.fetchall()
            return [ReviewDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, review_id: int) -> Optional[ReviewDTO]:
        """Отримати відгук за ID"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Reviews WHERE review_id = %s", (review_id,))
            result = cursor.fetchone()
            return ReviewDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, review: ReviewDTO) -> int:
        """Створити новий відгук"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Reviews (app_id, user_id, rating, review_text) VALUES (%s, %s, %s, %s)",
                (review.app_id, review.user_id, review.rating, review.review_text)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, review: ReviewDTO) -> bool:
        """Оновити відгук"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Reviews SET app_id = %s, user_id = %s, rating = %s, review_text = %s WHERE review_id = %s",
                (review.app_id, review.user_id, review.rating, review.review_text, review.review_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, review_id: int) -> bool:
        """Видалити відгук"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Reviews WHERE review_id = %s", (review_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_reviews_with_details(self) -> List[dict]:
        """Отримати відгуки з деталями (M:M зв'язок)"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT r.*, u.username, u.email, a.app_name, c.category_name, d.developer_name
                FROM Reviews r 
                LEFT JOIN Users u ON r.user_id = u.user_id 
                LEFT JOIN Apps a ON r.app_id = a.app_id 
                LEFT JOIN Categories c ON a.category_id = c.category_id
                LEFT JOIN Developers d ON a.developer_id = d.developer_id
                ORDER BY r.review_date DESC
            """)
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def get_reviews_by_user_and_app(self, user_id: int, app_id: int) -> List[dict]:
        """Отримати відгуки конкретного користувача для конкретного додатку"""
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT r.*, u.username, a.app_name
                FROM Reviews r 
                LEFT JOIN Users u ON r.user_id = u.user_id 
                LEFT JOIN Apps a ON r.app_id = a.app_id 
                WHERE r.user_id = %s AND r.app_id = %s
                ORDER BY r.review_date DESC
            """, (user_id, app_id))
            return cursor.fetchall()
        finally:
            cursor.close()
