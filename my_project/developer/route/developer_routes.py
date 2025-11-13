from flask import Blueprint
from flasgger import swag_from
from my_project.developer.controller.developer_controller import DeveloperController

developer_bp = Blueprint('developer', __name__)
controller = DeveloperController()


# --- Отримати всіх розробників ---
@developer_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Отримати всіх розробників',
    'responses': {200: {'description': 'Список розробників'}, 500: {'description': 'Помилка сервера'}}
})
def get_all_developers():
    return controller.get_all_developers()


# --- Отримати розробника за ID ---
@developer_bp.route('/<int:developer_id>', methods=['GET'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Отримати розробника за ID',
    'parameters': [{'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Розробник знайдений'}, 404: {'description': 'Не знайдено'}}
})
def get_developer_by_id(developer_id):
    return controller.get_developer_by_id(developer_id)


# --- Створити розробника ---
@developer_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Створити нового розробника',
    'parameters': [{
        'name': 'body', 'in': 'body', 'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'developer_name': {'type': 'string', 'example': 'Meta Inc.'},
                'contact_email': {'type': 'string', 'example': 'support@meta.com'}
            },
            'required': ['developer_name', 'contact_email']
        }
    }],
    'responses': {201: {'description': 'Розробника створено'}, 400: {'description': 'Некоректні дані'}}
})
def create_developer():
    return controller.create_developer()


# --- Оновити розробника ---
@developer_bp.route('/<int:developer_id>', methods=['PUT'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Оновити розробника',
    'parameters': [
        {'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {'type': 'object', 'properties': {'developer_name': {'type': 'string'}}}}
    ],
    'responses': {200: {'description': 'Оновлено'}, 404: {'description': 'Не знайдено'}}
})
def update_developer(developer_id):
    return controller.update_developer(developer_id)


# --- Видалити розробника ---
@developer_bp.route('/<int:developer_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Видалити розробника',
    'parameters': [{'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Видалено'}, 404: {'description': 'Не знайдено'}}
})
def delete_developer(developer_id):
    return controller.delete_developer(developer_id)


# --- Отримати додатки розробника ---
@developer_bp.route('/<int:developer_id>/apps', methods=['GET'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Отримати додатки розробника',
    'parameters': [{'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Список додатків'}, 500: {'description': 'Помилка сервера'}}
})
def get_apps_by_developer(developer_id):
    return controller.get_apps_by_developer(developer_id)
