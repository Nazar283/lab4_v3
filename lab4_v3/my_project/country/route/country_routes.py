from flask import Blueprint
from flasgger import swag_from
from my_project.country.controller.country_controller import CountryController

country_bp = Blueprint('country', __name__)
controller = CountryController()


# --- Отримати всі країни ---
@country_bp.route('/', methods=['GET'])
@swag_from({'tags': ['Countries'], 'summary': 'Отримати всі країни'})
def get_all_countries():
    return controller.get_all_countries()


# --- Отримати країну за ID ---
@country_bp.route('/<int:country_id>', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Отримати країну за ID',
    'parameters': [{'name': 'country_id', 'in': 'path', 'type': 'integer', 'required': True}]
})
def get_country_by_id(country_id):
    return controller.get_country_by_id(country_id)


# --- Створити країну ---
@country_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Створити нову країну',
    'parameters': [{
        'name': 'body', 'in': 'body', 'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'country_name': {'type': 'string', 'example': 'Ukraine'},
                'country_code': {'type': 'string', 'example': 'UA'}
            },
            'required': ['country_name', 'country_code']
        }
    }]
})
def create_country():
    return controller.create_country()


# --- Оновити країну ---
@country_bp.route('/<int:country_id>', methods=['PUT'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Оновити країну',
    'parameters': [
        {'name': 'country_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'schema': {'type': 'object', 'properties': {'country_name': {'type': 'string'}}}}
    ]
})
def update_country(country_id):
    return controller.update_country(country_id)


# --- Видалити країну ---
@country_bp.route('/<int:country_id>', methods=['DELETE'])
@swag_from({'tags': ['Countries'], 'summary': 'Видалити країну'})
def delete_country(country_id):
    return controller.delete_country(country_id)


# --- Отримати користувачів за країною ---
@country_bp.route('/<int:country_id>/users', methods=['GET'])
@swag_from({'tags': ['Countries'], 'summary': 'Отримати користувачів країни'})
def get_users_by_country(country_id):
    return controller.get_users_by_country(country_id)
