from flask import Blueprint
from flasgger import swag_from
from my_project.user.controller.user_controller import UserController

user_bp = Blueprint('user', __name__)
controller = UserController()


# --- Отримати всіх користувачів ---
@user_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Отримати всіх користувачів',
    'responses': {200: {'description': 'Список користувачів'}, 500: {'description': 'Помилка сервера'}}
})
def get_all_users():
    return controller.get_all_users()


# --- Отримати користувача за ID ---
@user_bp.route('/<int:user_id>', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Отримати користувача за ID',
    'parameters': [{'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Користувач знайдений'}, 404: {'description': 'Не знайдено'}}
})
def get_user_by_id(user_id):
    return controller.get_user_by_id(user_id)


# --- Створити користувача ---
@user_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Створити нового користувача',
    'parameters': [{
        'name': 'body', 'in': 'body', 'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'email': {'type': 'string', 'example': 'user@example.com'},
                'username': {'type': 'string', 'example': 'new_user'},
                'password_hash': {'type': 'string', 'example': 'hashedpassword123'}
            },
            'required': ['email', 'username', 'password_hash']
        }
    }],
    'responses': {201: {'description': 'Користувача створено'}, 400: {'description': 'Некоректні дані'}}
})
def create_user():
    return controller.create_user()


# --- Оновити користувача ---
@user_bp.route('/<int:user_id>', methods=['PUT'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Оновити користувача',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'schema': {'type': 'object', 'properties': {'username': {'type': 'string'}}}}
    ],
    'responses': {200: {'description': 'Оновлено'}, 404: {'description': 'Не знайдено'}}
})
def update_user(user_id):
    return controller.update_user(user_id)


# --- Видалити користувача ---
@user_bp.route('/<int:user_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Видалити користувача',
    'parameters': [{'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Видалено'}, 404: {'description': 'Не знайдено'}}
})
def delete_user(user_id):
    return controller.delete_user(user_id)


# --- Отримати відгуки користувача ---
@user_bp.route('/<int:user_id>/reviews', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Отримати відгуки користувача',
    'parameters': [{'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Список відгуків користувача'}, 500: {'description': 'Помилка сервера'}}
})
def get_reviews_by_user(user_id):
    return controller.get_reviews_by_user(user_id)


# --- Отримати встановлення користувача ---
@user_bp.route('/<int:user_id>/installations', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Отримати встановлення користувача',
    'parameters': [{'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Список встановлень'}, 500: {'description': 'Помилка сервера'}}
})
def get_installations_by_user(user_id):
    return controller.get_installations_by_user(user_id)
