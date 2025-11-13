from flask import Blueprint
from flasgger import swag_from
from my_project.category.controller.category_controller import CategoryController

category_bp = Blueprint('category', __name__)
controller = CategoryController()


# --- Отримати всі категорії ---
@category_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Отримати всі категорії',
    'description': 'Повертає список усіх категорій із бази даних.',
    'responses': {
        200: {'description': 'Успішно отримано список категорій'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_all_categories():
    return controller.get_all_categories()


# --- Отримати категорію за ID ---
@category_bp.route('/<int:category_id>', methods=['GET'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Отримати категорію за ID',
    'parameters': [{'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Категорію знайдено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_category_by_id(category_id):
    return controller.get_category_by_id(category_id)


# --- Створити категорію ---
@category_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Створити нову категорію',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {'category_name': {'type': 'string', 'example': 'Games'}},
            'required': ['category_name']
        },
        'description': 'Дані для створення категорії'
    }],
    'responses': {
        201: {'description': 'Категорію створено'},
        400: {'description': 'Некоректні дані'},
        500: {'description': 'Помилка сервера'}
    }
})
def create_category():
    return controller.create_category()


# --- Оновити категорію ---
@category_bp.route('/<int:category_id>', methods=['PUT'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Оновити категорію за ID',
    'parameters': [
        {'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body', 'in': 'body', 'required': True,
            'schema': {'type': 'object', 'properties': {'category_name': {'type': 'string', 'example': 'Productivity'}}}
        }
    ],
    'responses': {
        200: {'description': 'Категорію оновлено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def update_category(category_id):
    return controller.update_category(category_id)


# --- Видалити категорію ---
@category_bp.route('/<int:category_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Видалити категорію',
    'parameters': [{'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Категорію видалено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def delete_category(category_id):
    return controller.delete_category(category_id)


# --- Отримати додатки за категорією ---
@category_bp.route('/<int:category_id>/apps', methods=['GET'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Отримати додатки за категорією',
    'parameters': [{'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Список додатків категорії'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_apps_by_category(category_id):
    return controller.get_apps_by_category(category_id)
