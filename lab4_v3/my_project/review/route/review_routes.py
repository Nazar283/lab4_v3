from flask import Blueprint
from flasgger import swag_from
from my_project.review.controller.review_controller import ReviewController

review_bp = Blueprint('review', __name__)
controller = ReviewController()


# --- Отримати всі відгуки ---
@review_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Отримати всі відгуки',
    'description': 'Повертає список усіх відгуків у базі даних.',
    'responses': {
        200: {'description': 'Список відгуків отримано'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_all_reviews():
    return controller.get_all_reviews()


# --- Отримати відгук за ID ---
@review_bp.route('/<int:review_id>', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Отримати відгук за ID',
    'parameters': [{'name': 'review_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Відгук знайдено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_review_by_id(review_id):
    return controller.get_review_by_id(review_id)


# --- Створити відгук ---
@review_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Створити новий відгук',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'user_id': {'type': 'integer', 'example': 1},
                'app_id': {'type': 'integer', 'example': 5},
                'rating': {'type': 'number', 'example': 4.5},
                'comment': {'type': 'string', 'example': 'Дуже зручний додаток!'}
            },
            'required': ['user_id', 'app_id', 'rating']
        },
        'description': 'Дані для створення нового відгуку'
    }],
    'responses': {
        201: {'description': 'Відгук створено'},
        400: {'description': 'Некоректні дані'},
        500: {'description': 'Помилка сервера'}
    }
})
def create_review():
    return controller.create_review()


# --- Оновити відгук ---
@review_bp.route('/<int:review_id>', methods=['PUT'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Оновити відгук',
    'parameters': [
        {'name': 'review_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True,
         'schema': {'type': 'object', 'properties': {'rating': {'type': 'number'}, 'comment': {'type': 'string'}}}}
    ],
    'responses': {
        200: {'description': 'Відгук оновлено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def update_review(review_id):
    return controller.update_review(review_id)


# --- Видалити відгук ---
@review_bp.route('/<int:review_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Видалити відгук',
    'parameters': [{'name': 'review_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Відгук видалено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def delete_review(review_id):
    return controller.delete_review(review_id)


# --- Отримати відгуки з деталями ---
@review_bp.route('/details', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Отримати відгуки з деталями (join)',
    'description': 'Повертає відгуки з повною інформацією про користувача та додаток.',
    'responses': {
        200: {'description': 'Список відгуків з деталями'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_reviews_with_details():
    return controller.get_reviews_with_details()


# --- Отримати відгуки за користувачем і додатком ---
@review_bp.route('/user/<int:user_id>/app/<int:app_id>', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Отримати відгуки користувача про конкретний додаток',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Список відгуків'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_reviews_by_user_and_app(user_id, app_id):
    return controller.get_reviews_by_user_and_app(user_id, app_id)
