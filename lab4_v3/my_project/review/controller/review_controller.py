from flask import request, jsonify
from my_project.review.service.review_service import ReviewService

class ReviewController:
    def __init__(self):
        self.review_service = ReviewService()
    
    def get_all_reviews(self):
        """GET /api/reviews - Отримати всі відгуки"""
        try:
            reviews = self.review_service.get_all_reviews()
            return jsonify([review.to_dict() for review in reviews]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_review_by_id(self, review_id):
        """GET /api/reviews/<id> - Отримати відгук за ID"""
        try:
            review = self.review_service.get_review_by_id(review_id)
            if review:
                return jsonify(review.to_dict()), 200
            else:
                return jsonify({'error': 'Review not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_review(self):
        """POST /api/reviews - Створити новий відгук"""
        try:
            data = request.get_json()
            if not data or 'app_id' not in data or 'user_id' not in data or 'rating' not in data:
                return jsonify({'error': 'Missing required fields'}), 400
            
            if not (1 <= data['rating'] <= 5):
                return jsonify({'error': 'Rating must be between 1 and 5'}), 400
            
            review_id = self.review_service.create_review(data)
            return jsonify({'id': review_id, 'message': 'Review created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_review(self, review_id):
        """PUT /api/reviews/<id> - Оновити відгук"""
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            
            if 'rating' in data and not (1 <= data['rating'] <= 5):
                return jsonify({'error': 'Rating must be between 1 and 5'}), 400
            
            success = self.review_service.update_review(review_id, data)
            if success:
                return jsonify({'message': 'Review updated successfully'}), 200
            else:
                return jsonify({'error': 'Review not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def delete_review(self, review_id):
        """DELETE /api/reviews/<id> - Видалити відгук"""
        try:
            success = self.review_service.delete_review(review_id)
            if success:
                return jsonify({'message': 'Review deleted successfully'}), 200
            else:
                return jsonify({'error': 'Review not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_reviews_with_details(self):
        """GET /api/reviews/details - Отримати відгуки з деталями (M:M)"""
        try:
            reviews = self.review_service.get_reviews_with_details()
            return jsonify(reviews), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_reviews_by_user_and_app(self, user_id, app_id):
        """GET /api/reviews/user/<user_id>/app/<app_id> - Отримати відгуки користувача для додатку"""
        try:
            reviews = self.review_service.get_reviews_by_user_and_app(user_id, app_id)
            return jsonify(reviews), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
