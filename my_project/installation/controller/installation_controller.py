from flask import request, jsonify
from my_project.installation.service.installation_service import InstallationService

class InstallationController:
    def __init__(self):
        self.installation_service = InstallationService()
    
    def get_all_installations(self):
        try:
            installations = self.installation_service.get_all_installations()
            return jsonify([installation.to_dict() for installation in installations]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_installation_by_id(self, installation_id):
        try:
            installation = self.installation_service.get_installation_by_id(installation_id)
            if installation:
                return jsonify(installation.to_dict()), 200
            else:
                return jsonify({'error': 'Installation not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_installation(self):
        try:
            data = request.get_json()
            if not data or 'user_id' not in data or 'app_id' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            installation_id = self.installation_service.create_installation(data)
            return jsonify({'id': installation_id, 'message': 'Installation created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_installation(self, installation_id):
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            success = self.installation_service.update_installation(installation_id, data)
            if success:
                return jsonify({'message': 'Installation updated successfully'}), 200
            else:
                return jsonify({'error': 'Installation not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_installation(self, installation_id):
        try:
            success = self.installation_service.delete_installation(installation_id)
            if success:
                return jsonify({'message': 'Installation deleted successfully'}), 200
            else:
                return jsonify({'error': 'Installation not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_installations_with_details(self):
        try:
            installations = self.installation_service.get_installations_with_details()
            return jsonify(installations), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
