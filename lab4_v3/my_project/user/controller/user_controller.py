from flask import request, jsonify
from my_project.user.service.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()
    
    def get_all_users(self):
        """GET /api/users - Отримати всіх користувачів"""
        try:
            users = self.user_service.get_all_users()
            return jsonify([user.to_dict() for user in users]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_user_by_id(self, user_id):
        """GET /api/users/<id> - Отримати користувача за ID"""
        try:
            user = self.user_service.get_user_by_id(user_id)
            if user:
                return jsonify(user.to_dict()), 200
            else:
                return jsonify({'error': 'User not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_user(self):
        """POST /api/users - Створити нового користувача"""
        try:
            data = request.get_json()
            if not data or 'email' not in data or 'username' not in data or 'password_hash' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            user_id = self.user_service.create_user(data)
            return jsonify({'id': user_id, 'message': 'User created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_user(self, user_id):
        """PUT /api/users/<id> - Оновити користувача"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            success = self.user_service.update_user(user_id, data)
            if success:
                return jsonify({'message': 'User updated successfully'}), 200
            else:
                return jsonify({'error': 'User not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_user(self, user_id):
        """DELETE /api/users/<id> - Видалити користувача"""
        try:
            success = self.user_service.delete_user(user_id)
            if success:
                return jsonify({'message': 'User deleted successfully'}), 200
            else:
                return jsonify({'error': 'User not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_reviews_by_user(self, user_id):
        """GET /api/users/<id>/reviews - Отримати відгуки користувача (M:1)"""
        try:
            reviews = self.user_service.get_reviews_by_user(user_id)
            return jsonify(reviews), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_installations_by_user(self, user_id):
        """GET /api/users/<id>/installations - Отримати встановлення користувача (M:1)"""
        try:
            installations = self.user_service.get_installations_by_user(user_id)
            return jsonify(installations), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
