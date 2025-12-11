from flask import Blueprint
from flasgger import swag_from
from my_project.installation.controller.installation_controller import InstallationController

installation_bp = Blueprint('installation', __name__)
controller = InstallationController()


# --- Get all installations ---
@installation_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Get all installations',
    'description': 'Returns a list of all installation records.',
    'responses': {
        200: {'description': 'List of installations successfully retrieved'},
        500: {'description': 'Server error'}
    }
})
def get_all_installations():
    return controller.get_all_installations()


# --- Get installation by ID ---
@installation_bp.route('/<int:installation_id>', methods=['GET'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Get installation by ID',
    'description': 'Returns information about a specific installation.',
    'parameters': [
        {'name': 'installation_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Installation found'},
        404: {'description': 'Installation not found'},
        500: {'description': 'Server error'}
    }
})
def get_installation_by_id(installation_id):
    return controller.get_installation_by_id(installation_id)


# --- Create a new installation ---
@installation_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Create a new installation',
    'description': 'Creates a new installation record for a specific app and user.',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'user_id': {'type': 'integer', 'example': 1},
                'app_id': {'type': 'integer', 'example': 5}
            },
            'required': ['user_id', 'app_id']
        }
    }],
    'responses': {
        201: {'description': 'Installation successfully created'},
        400: {'description': 'Invalid input data'},
        500: {'description': 'Server error'}
    }
})
def create_installation():
    return controller.create_installation()


# --- Update installation ---
@installation_bp.route('/<int:installation_id>', methods=['PUT'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Update an installation',
    'description': 'Updates installation details identified by its ID.',
    'parameters': [
        {'name': 'installation_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'integer', 'example': 10},
                    'user_id': {'type': 'integer', 'example': 2}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Installation successfully updated'},
        400: {'description': 'Invalid update data'},
        404: {'description': 'Installation not found'},
        500: {'description': 'Server error'}
    }
})
def update_installation(installation_id):
    return controller.update_installation(installation_id)


# --- Delete installation ---
@installation_bp.route('/<int:installation_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Delete an installation',
    'description': 'Deletes an installation record based on its ID.',
    'parameters': [
        {'name': 'installation_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Installation successfully deleted'},
        404: {'description': 'Installation not found'},
        500: {'description': 'Server error'}
    }
})
def delete_installation(installation_id):
    return controller.delete_installation(installation_id)


# --- Get all installations with details ---
@installation_bp.route('/details', methods=['GET'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Get all installations with details',
    'description': 'Returns extended installation information, including related user, app, and version data.',
    'responses': {
        200: {'description': 'Detailed installation list successfully retrieved'},
        500: {'description': 'Server error'}
    }
})
def get_installations_with_details():
    return controller.get_installations_with_details()
