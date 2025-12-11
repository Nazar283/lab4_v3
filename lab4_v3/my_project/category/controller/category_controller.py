from flask import request, jsonify
from my_project.category.service.category_service import CategoryService

class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()
    
    def get_all_categories(self):
        try:
            categories = self.category_service.get_all_categories()
            return jsonify([category.to_dict() for category in categories]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_category_by_id(self, category_id):
        try:
            category = self.category_service.get_category_by_id(category_id)
            if category:
                return jsonify(category.to_dict()), 200
            else:
                return jsonify({'error': 'Category not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_category(self):
        try:
            data = request.get_json()
            if not data or 'category_name' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            category_id = self.category_service.create_category(data)
            return jsonify({'id': category_id, 'message': 'Category created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_category(self, category_id):
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            success = self.category_service.update_category(category_id, data)
            if success:
                return jsonify({'message': 'Category updated successfully'}), 200
            else:
                return jsonify({'error': 'Category not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_category(self, category_id):
        try:
            success = self.category_service.delete_category(category_id)
            if success:
                return jsonify({'message': 'Category deleted successfully'}), 200
            else:
                return jsonify({'error': 'Category not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_apps_by_category(self, category_id):
        try:
            apps = self.category_service.get_apps_by_category(category_id)
            return jsonify(apps), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
