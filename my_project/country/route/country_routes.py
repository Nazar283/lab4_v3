from flask import Blueprint
from flasgger import swag_from
from my_project.country.controller.country_controller import CountryController

country_bp = Blueprint('country', __name__)
controller = CountryController()


# --- Get all countries ---
@country_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Get all countries',
    'description': 'Returns a complete list of countries available in the system.',
    'responses': {
        200: {'description': 'List of countries successfully retrieved'},
        500: {'description': 'Server error'}
    }
})
def get_all_countries():
    return controller.get_all_countries()


# --- Get a country by ID ---
@country_bp.route('/<int:country_id>', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Get a country by ID',
    'description': 'Returns information about a specific country based on its ID.',
    'parameters': [
        {'name': 'country_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Country found and returned'},
        404: {'description': 'Country not found'},
        500: {'description': 'Server error'}
    }
})
def get_country_by_id(country_id):
    return controller.get_country_by_id(country_id)


# --- Create a new country ---
@country_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Create a new country',
    'description': 'Adds a new country to the database.',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'country_name': {'type': 'string', 'example': 'Ukraine'},
                'country_code': {'type': 'string', 'example': 'UA'}
            },
            'required': ['country_name', 'country_code']
        }
    }],
    'responses': {
        201: {'description': 'Country successfully created'},
        400: {'description': 'Invalid input data'},
        500: {'description': 'Server error'}
    }
})
def create_country():
    return controller.create_country()


# --- Update a country ---
@country_bp.route('/<int:country_id>', methods=['PUT'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Update a country',
    'description': 'Updates country information by its ID.',
    'parameters': [
        {'name': 'country_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'country_name': {'type': 'string', 'example': 'Poland'},
                    'country_code': {'type': 'string', 'example': 'PL'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Country successfully updated'},
        400: {'description': 'Invalid update data'},
        404: {'description': 'Country not found'},
        500: {'description': 'Server error'}
    }
})
def update_country(country_id):
    return controller.update_country(country_id)


# --- Delete a country ---
@country_bp.route('/<int:country_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Delete a country',
    'description': 'Deletes a country from the database using its ID.',
    'parameters': [
        {'name': 'country_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Country successfully deleted'},
        404: {'description': 'Country not found'},
        500: {'description': 'Server error'}
    }
})
def delete_country(country_id):
    return controller.delete_country(country_id)


# --- Get users by country ---
@country_bp.route('/<int:country_id>/users', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'summary': 'Get users by country',
    'description': 'Returns a list of users associated with a specific country.',
    'parameters': [
        {'name': 'country_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Users successfully retrieved'},
        404: {'description': 'Country not found or has no users'},
        500: {'description': 'Server error'}
    }
})
def get_users_by_country(country_id):
    return controller.get_users_by_country(country_id)
