import pymysql
from typing import List, Optional
from my_project.utils.database import DatabaseConnection
from my_project.domain.installation_dto import InstallationDTO

class InstallationDAO:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get_all(self) -> List[InstallationDTO]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Installations ORDER BY install_date DESC")
            results = cursor.fetchall()
            return [InstallationDTO.from_dict(row) for row in results]
        finally:
            cursor.close()
    
    def get_by_id(self, installation_id: int) -> Optional[InstallationDTO]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM Installations WHERE installation_id = %s", (installation_id,))
            result = cursor.fetchone()
            return InstallationDTO.from_dict(result) if result else None
        finally:
            cursor.close()
    
    def create(self, installation: InstallationDTO) -> int:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO Installations (user_id, app_id, installed_version_id) VALUES (%s, %s, %s)",
                (installation.user_id, installation.app_id, installation.installed_version_id)
            )
            return cursor.lastrowid
        finally:
            cursor.close()
    
    def update(self, installation: InstallationDTO) -> bool:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute(
                "UPDATE Installations SET user_id = %s, app_id = %s, installed_version_id = %s WHERE installation_id = %s",
                (installation.user_id, installation.app_id, installation.installed_version_id, installation.installation_id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def delete(self, installation_id: int) -> bool:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM Installations WHERE installation_id = %s", (installation_id,))
            return cursor.rowcount > 0
        finally:
            cursor.close()
    
    def get_installations_with_details(self) -> List[dict]:
        connection = self.db.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT i.*, u.username, u.email, a.app_name, av.version_name, c.category_name, d.developer_name
                FROM Installations i 
                LEFT JOIN Users u ON i.user_id = u.user_id 
                LEFT JOIN Apps a ON i.app_id = a.app_id 
                LEFT JOIN AppVersions av ON i.installed_version_id = av.version_id
                LEFT JOIN Categories c ON a.category_id = c.category_id
                LEFT JOIN Developers d ON a.developer_id = d.developer_id
                ORDER BY i.install_date DESC
            """)
            return cursor.fetchall()
        finally:
            cursor.close()
