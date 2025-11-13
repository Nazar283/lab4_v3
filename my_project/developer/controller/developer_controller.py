from flask import request, jsonify
from my_project.developer.service.developer_service import DeveloperService

class DeveloperController:
    def __init__(self):
        self.developer_service = DeveloperService()
    
    def get_all_developers(self):
        try:
            developers = self.developer_service.get_all_developers()
            return jsonify([developer.to_dict() for developer in developers]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_developer_by_id(self, developer_id):
        try:
            developer = self.developer_service.get_developer_by_id(developer_id)
            if developer:
                return jsonify(developer.to_dict()), 200
            else:
                return jsonify({'error': 'Developer not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_developer(self):
        try:
            data = request.get_json()
            if not data or 'developer_name' not in data or 'contact_email' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            developer_id = self.developer_service.create_developer(data)
            return jsonify({'id': developer_id, 'message': 'Developer created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_developer(self, developer_id):
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            success = self.developer_service.update_developer(developer_id, data)
            if success:
                return jsonify({'message': 'Developer updated successfully'}), 200
            else:
                return jsonify({'error': 'Developer not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_developer(self, developer_id):
        try:
            success = self.developer_service.delete_developer(developer_id)
            if success:
                return jsonify({'message': 'Developer deleted successfully'}), 200
            else:
                return jsonify({'error': 'Developer not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_apps_by_developer(self, developer_id):
        try:
            apps = self.developer_service.get_apps_by_developer(developer_id)
            return jsonify(apps), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
