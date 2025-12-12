from flask import Blueprint
from flasgger import swag_from
from my_project.app.controller.app_controller import AppController

app_bp = Blueprint('app', __name__)
controller = AppController()


# --- Отримати всі додатки ---
# @app_bp.route('/', methods=['GET'])
# @swag_from({
#     'tags': ['Apps'],
#     'summary': 'Отримати всі додатки',
#     'description': 'Повертає список усіх додатків із бази даних.',
#     'responses': {
#         200: {'description': 'Успішно отримано список додатків'},
#         500: {'description': 'Помилка сервера'}
#     }
# })
# def get_all_apps():
#     return controller.get_all_apps()


# # --- Отримати додаток за ID ---
# @app_bp.route('/<int:app_id>', methods=['GET'])
# @swag_from({
#     'tags': ['Apps'],
#     'summary': 'Отримати додаток за ID',
#     'parameters': [
#         {'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID додатку'}
#     ],
#     'responses': {
#         200: {'description': 'Додаток знайдено'},
#         404: {'description': 'Додаток не знайдено'},
#         500: {'description': 'Помилка сервера'}
#     }
# })
# def get_app_by_id(app_id):
#     return controller.get_app_by_id(app_id)


# # --- Створити новий додаток ---
# @app_bp.route('/', methods=['POST'])
# @swag_from({
#     'tags': ['Apps'],
#     'summary': 'Створити новий додаток',
#     'description': 'Створює новий запис додатку у базі даних.',
#     'parameters': [
#         {
#             'name': 'body',
#             'in': 'body',
#             'required': True,
#             'schema': {
#                 'type': 'object',
#                 'properties': {
#                     'app_name': {'type': 'string', 'example': 'Instagram'},
#                     'developer_id': {'type': 'integer', 'example': 1},
#                     'category_id': {'type': 'integer', 'example': 2}
#                 },
#                 'required': ['app_name', 'developer_id', 'category_id']
#             },
#             'description': 'Дані для створення нового додатку'
#         }
#     ],
#     'responses': {
#         201: {
#             'description': 'Додаток створено успішно',
#             'examples': {
#                 'application/json': {
#                     'id': 123,
#                     'message': 'App created successfully'
#                 }
#             }
#         },
#         400: {'description': 'Відсутні обов’язкові поля'},
#         500: {'description': 'Помилка сервера'}
#     }
# })
# def create_app():
#     return controller.create_app()




# --- Оновити додаток ---
@app_bp.route('/<int:app_id>', methods=['PUT'])
@swag_from({
    'tags': ['Apps'],
    'summary': 'Оновити додаток за ID',
    'parameters': [
        {'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID додатку'}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'example': {
                    'app_name': 'Instagram Updated',
                    'category_id': 3
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Додаток оновлено'},
        404: {'description': 'Додаток не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def update_app(app_id):
    return controller.update_app(app_id)


# --- Видалити додаток ---
@app_bp.route('/<int:app_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Apps'],
    'summary': 'Видалити додаток за ID',
    'parameters': [
        {'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID додатку'}
    ],
    'responses': {
        200: {'description': 'Додаток видалено'},
        404: {'description': 'Не знайдено'},
        500: {'description': 'Помилка сервера'}
    }
})
def delete_app(app_id):
    return controller.delete_app(app_id)


# --- Отримати відгуки додатку ---
@app_bp.route('/<int:app_id>/reviews', methods=['GET'])
@swag_from({
    'tags': ['Apps'],
    'summary': 'Отримати відгуки додатку',
    'description': 'Повертає всі відгуки, повʼязані з конкретним додатком.',
    'parameters': [
        {'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Список відгуків'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_reviews_by_app(app_id):
    return controller.get_reviews_by_app(app_id)


# --- Отримати встановлення додатку ---
@app_bp.route('/<int:app_id>/installations', methods=['GET'])
@swag_from({
    'tags': ['Apps'],
    'summary': 'Отримати встановлення додатку',
    'parameters': [{'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Список встановлень додатку'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_installations_by_app(app_id):
    return controller.get_installations_by_app(app_id)


# --- Отримати версії додатку ---
@app_bp.route('/<int:app_id>/versions', methods=['GET'])
@swag_from({
    'tags': ['Apps'],
    'summary': 'Отримати версії додатку',
    'parameters': [{'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Список версій додатку'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_versions_by_app(app_id):
    return controller.get_versions_by_app(app_id)


# --- Отримати скріншоти додатку ---
@app_bp.route('/<int:app_id>/screenshots', methods=['GET'])
@swag_from({
    'tags': ['Apps'],
    'summary': 'Отримати скріншоти додатку',
    'parameters': [{'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {
        200: {'description': 'Список скріншотів'},
        500: {'description': 'Помилка сервера'}
    }
})
def get_screenshots_by_app(app_id):
    return controller.get_screenshots_by_app(app_id)
