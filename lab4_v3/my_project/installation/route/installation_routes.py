from flask import Blueprint
from flasgger import swag_from
from my_project.installation.controller.installation_controller import InstallationController

installation_bp = Blueprint('installation', __name__)
controller = InstallationController()


# --- Отримати всі встановлення ---
@installation_bp.route('/', methods=['GET'])
@swag_from({'tags': ['Installations'], 'summary': 'Отримати всі встановлення'})
def get_all_installations():
    return controller.get_all_installations()


# --- Отримати встановлення за ID ---
@installation_bp.route('/<int:installation_id>', methods=['GET'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Отримати встановлення за ID',
    'parameters': [{'name': 'installation_id', 'in': 'path', 'type': 'integer', 'required': True}]
})
def get_installation_by_id(installation_id):
    return controller.get_installation_by_id(installation_id)


# --- Створити встановлення ---
@installation_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Створити нове встановлення',
    'parameters': [{
        'name': 'body', 'in': 'body', 'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'user_id': {'type': 'integer', 'example': 1},
                'app_id': {'type': 'integer', 'example': 5}
            },
            'required': ['user_id', 'app_id']
        }
    }]
})
def create_installation():
    return controller.create_installation()


# --- Оновити встановлення ---
@installation_bp.route('/<int:installation_id>', methods=['PUT'])
@swag_from({
    'tags': ['Installations'],
    'summary': 'Оновити встановлення',
    'parameters': [
        {'name': 'installation_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'schema': {'type': 'object', 'properties': {'app_id': {'type': 'integer'}}}}
    ]
})
def update_installation(installation_id):
    return controller.update_installation(installation_id)


# --- Видалити встановлення ---
@installation_bp.route('/<int:installation_id>', methods=['DELETE'])
@swag_from({'tags': ['Installations'], 'summary': 'Видалити встановлення'})
def delete_installation(installation_id):
    return controller.delete_installation(installation_id)


# --- Отримати встановлення з деталями ---
@installation_bp.route('/details', methods=['GET'])
@swag_from({'tags': ['Installations'], 'summary': 'Отримати всі встановлення з деталями'})
def get_installations_with_details():
    return controller.get_installations_with_details()
