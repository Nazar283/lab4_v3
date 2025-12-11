from flask import Blueprint
from flasgger import swag_from
from my_project.user.controller.user_controller import UserController

user_bp = Blueprint('user', __name__)
controller = UserController()


# --- Get all users ---
@user_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Get all users',
    'description': 'Returns a list of all registered users.',
    'responses': {
        200: {'description': 'User list retrieved successfully'},
        500: {'description': 'Server error'}
    }
})
def get_all_users():
    return controller.get_all_users()


# --- Get user by ID ---
@user_bp.route('/<int:user_id>', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Get a user by ID',
    'description': 'Returns detailed information about a specific user.',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'User found'},
        404: {'description': 'User not found'},
        500: {'description': 'Server error'}
    }
})
def get_user_by_id(user_id):
    return controller.get_user_by_id(user_id)


# --- Create a new user ---
@user_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Create a new user',
    'description': 'Creates a new user account in the system.',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
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
    'responses': {
        201: {'description': 'User created successfully'},
        400: {'description': 'Invalid input data'},
        500: {'description': 'Server error'}
    }
})
def create_user():
    return controller.create_user()


# --- Update user ---
@user_bp.route('/<int:user_id>', methods=['PUT'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Update a user',
    'description': 'Updates user data such as username or other attributes.',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string', 'example': 'updated_username'},
                    'email': {'type': 'string', 'example': 'updated@example.com'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'User updated successfully'},
        400: {'description': 'Invalid update data'},
        404: {'description': 'User not found'},
        500: {'description': 'Server error'}
    }
})
def update_user(user_id):
    return controller.update_user(user_id)


# --- Delete user ---
@user_bp.route('/<int:user_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Delete a user',
    'description': 'Deletes a user account from the system.',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'User deleted successfully'},
        404: {'description': 'User not found'},
        500: {'description': 'Server error'}
    }
})
def delete_user(user_id):
    return controller.delete_user(user_id)


# --- Get reviews written by a user ---
@user_bp.route('/<int:user_id>/reviews', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'summary': 'Get user reviews',
    'description': 'Returns all reviews written by the specified user.',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'User reviews retrieved successfully'},
        500: {'description': 'Server error'}
    }
})
def get_reviews_by_user(user_id):
    return controller.get_reviews_by_user(user_id)


# --- Get installations performed by a user ---
@user_bp.route('/<int:user_id>/installations', methods=['GET'])
@swag_From({
    'tags': ['Users'],
    'summary': 'Get user installations',
    'description': 'Returns all application installations performed by the specified user.',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'User installations retrieved successfully'},
        500: {'description': 'Server error'}
    }
})
def get_installations_by_user(user_id):
    return controller.get_installations_by_user(user_id)
