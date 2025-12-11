from flask import request, jsonify
from my_project.country.service.country_service import CountryService

class CountryController:
    def __init__(self):
        self.country_service = CountryService()
    
    def get_all_countries(self):
        """GET /api/countries - Отримати всі країни"""
        try:
            countries = self.country_service.get_all_countries()
            return jsonify([country.to_dict() for country in countries]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_country_by_id(self, country_id):
        """GET /api/countries/<id> - Отримати країну за ID"""
        try:
            country = self.country_service.get_country_by_id(country_id)
            if country:
                return jsonify(country.to_dict()), 200
            else:
                return jsonify({'error': 'Country not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_country(self):
        """POST /api/countries - Створити нову країну"""
        try:
            data = request.get_json()
            if not data or 'country_name' not in data or 'country_code' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            country_id = self.country_service.create_country(data)
            return jsonify({'id': country_id, 'message': 'Country created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_country(self, country_id):
        """PUT /api/countries/<id> - Оновити країну"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            success = self.country_service.update_country(country_id, data)
            if success:
                return jsonify({'message': 'Country updated successfully'}), 200
            else:
                return jsonify({'error': 'Country not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_country(self, country_id):
        """DELETE /api/countries/<id> - Видалити країну"""
        try:
            success = self.country_service.delete_country(country_id)
            if success:
                return jsonify({'message': 'Country deleted successfully'}), 200
            else:
                return jsonify({'error': 'Country not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_users_by_country(self, country_id):
        """GET /api/countries/<id>/users - Отримати користувачів по країні (M:1)"""
        try:
            users = self.country_service.get_users_by_country(country_id)
            return jsonify(users), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
