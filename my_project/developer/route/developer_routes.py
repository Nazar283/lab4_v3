from flask import Blueprint
from flasgger import swag_from
from my_project.developer.controller.developer_controller import DeveloperController

developer_bp = Blueprint('developer', __name__)
controller = DeveloperController()


# --- Get all developers ---
@developer_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Get all developers',
    'description': 'Returns a list of all registered developers.',
    'responses': {
        200: {'description': 'List of developers successfully retrieved'},
        500: {'description': 'Server error'}
    }
})
def get_all_developers():
    return controller.get_all_developers()


# --- Get developer by ID ---
@developer_bp.route('/<int:developer_id>', methods=['GET'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Get a developer by ID',
    'description': 'Returns developer information based on the provided ID.',
    'parameters': [
        {'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Developer found'},
        404: {'description': 'Developer not found'},
        500: {'description': 'Server error'}
    }
})
def get_developer_by_id(developer_id):
    return controller.get_developer_by_id(developer_id)


# --- Create a new developer ---
@developer_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Create a new developer',
    'description': 'Creates a new developer record in the system.',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'developer_name': {'type': 'string', 'example': 'Meta Inc.'},
                'contact_email': {'type': 'string', 'example': 'support@meta.com'}
            },
            'required': ['developer_name', 'contact_email']
        }
    }],
    'responses': {
        201: {'description': 'Developer successfully created'},
        400: {'description': 'Invalid input data'},
        500: {'description': 'Server error'}
    }
})
def create_developer():
    return controller.create_developer()


# --- Update a developer ---
@developer_bp.route('/<int:developer_id>', methods=['PUT'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Update an existing developer',
    'description': 'Updates developer details based on the provided ID.',
    'parameters': [
        {'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'developer_name': {'type': 'string', 'example': 'Updated Developer Name'},
                    'contact_email': {'type': 'string', 'example': 'new_contact@example.com'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Developer successfully updated'},
        400: {'description': 'Invalid update data'},
        404: {'description': 'Developer not found'},
        500: {'description': 'Server error'}
    }
})
def update_developer(developer_id):
    return controller.update_developer(developer_id)


# --- Delete a developer ---
@developer_bp.route('/<int:developer_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Delete a developer',
    'description': 'Deletes a developer record using its ID.',
    'parameters': [
        {'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Developer successfully deleted'},
        404: {'description': 'Developer not found'},
        500: {'description': 'Server error'}
    }
})
def delete_developer(developer_id):
    return controller.delete_developer(developer_id)


# --- Get apps by developer ---
@developer_bp.route('/<int:developer_id>/apps', methods=['GET'])
@swag_from({
    'tags': ['Developers'],
    'summary': 'Get applications developed by a specific developer',
    'description': 'Returns a list of applications created by the developer with the given ID.',
    'parameters': [
        {'name': 'developer_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'List of applications successfully retrieved'},
        404: {'description': 'Developer not found'},
        500: {'description': 'Server error'}
    }
})
def get_apps_by_developer(developer_id):
    return controller.get_apps_by_developer(developer_id)
