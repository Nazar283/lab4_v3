from flask import request, jsonify
from my_project.app.service.app_service import AppService

class AppController:
    def __init__(self):
        self.app_service = AppService()
    
    def get_all_apps(self):
        """GET /api/apps - Отримати всі додатки"""
        try:
            apps = self.app_service.get_all_apps()
            return jsonify([app.to_dict() for app in apps]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_app_by_id(self, app_id):
        """GET /api/apps/<id> - Отримати додаток за ID"""
        try:
            app = self.app_service.get_app_by_id(app_id)
            if app:
                return jsonify(app.to_dict()), 200
            else:
                return jsonify({'error': 'App not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_app(self):
        """POST /api/apps - Створити новий додаток"""
        try:
            data = request.get_json()
            if not data or 'app_name' not in data or 'developer_id' not in data or 'category_id' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            app_id = self.app_service.create_app(data)
            return jsonify({'id': app_id, 'message': 'App created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_app(self, app_id):
        """PUT /api/apps/<id> - Оновити додаток"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            success = self.app_service.update_app(app_id, data)
            if success:
                return jsonify({'message': 'App updated successfully'}), 200
            else:
                return jsonify({'error': 'App not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_app(self, app_id):
        """DELETE /api/apps/<id> - Видалити додаток"""
        try:
            success = self.app_service.delete_app(app_id)
            if success:
                return jsonify({'message': 'App deleted successfully'}), 200
            else:
                return jsonify({'error': 'App not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_reviews_by_app(self, app_id):
        """GET /api/apps/<id>/reviews - Отримати відгуки додатку (M:1)"""
        try:
            reviews = self.app_service.get_reviews_by_app(app_id)
            return jsonify(reviews), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_installations_by_app(self, app_id):
        """GET /api/apps/<id>/installations - Отримати встановлення додатку (M:1)"""
        try:
            installations = self.app_service.get_installations_by_app(app_id)
            return jsonify(installations), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_versions_by_app(self, app_id):
        """GET /api/apps/<id>/versions - Отримати версії додатку (M:1)"""
        try:
            versions = self.app_service.get_versions_by_app(app_id)
            return jsonify(versions), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_screenshots_by_app(self, app_id):
        """GET /api/apps/<id>/screenshots - Отримати скріншоти додатку (M:1)"""
        try:
            screenshots = self.app_service.get_screenshots_by_app(app_id)
            return jsonify(screenshots), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
