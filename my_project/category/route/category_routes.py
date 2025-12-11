from flask import Blueprint
from flasgger import swag_from
from my_project.category.controller.category_controller import CategoryController

category_bp = Blueprint('category', __name__)
controller = CategoryController()


# --- Get all categories ---
@category_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Get all categories',
    'description': 'Returns a list of all categories stored in the database.',
    'responses': {
        200: {'description': 'Successfully retrieved the list of categories'},
        500: {'description': 'Server error'}
    }
})
def get_all_categories():
    return controller.get_all_categories()


# --- Get category by ID ---
@category_bp.route('/<int:category_id>', methods=['GET'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Get a category by ID',
    'parameters': [
        {'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Category found'},
        404: {'description': 'Category not found'},
        500: {'description': 'Server error'}
    }
})
def get_category_by_id(category_id):
    return controller.get_category_by_id(category_id)


# --- Create a new category ---
@category_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Create a new category',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'description': 'Payload for creating a new category',
        'schema': {
            'type': 'object',
            'properties': {
                'category_name': {'type': 'string', 'example': 'Games'}
            },
            'required': ['category_name']
        }
    }],
    'responses': {
        201: {'description': 'Category successfully created'},
        400: {'description': 'Invalid input data'},
        500: {'description': 'Server error'}
    }
})
def create_category():
    return controller.create_category()


# --- Update category by ID ---
@category_bp.route('/<int:category_id>', methods=['PUT'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Update a category by ID',
    'parameters': [
        {'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Updated category data',
            'schema': {
                'type': 'object',
                'properties': {
                    'category_name': {'type': 'string', 'example': 'Productivity'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Category successfully updated'},
        404: {'description': 'Category not found'},
        500: {'description': 'Server error'}
    }
})
def update_category(category_id):
    return controller.update_category(category_id)


# --- Delete category ---
@category_bp.route('/<int:category_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Delete a category by ID',
    'parameters': [
        {'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Category successfully deleted'},
        404: {'description': 'Category not found'},
        500: {'description': 'Server error'}
    }
})
def delete_category(category_id):
    return controller.delete_category(category_id)


# --- Get apps by category ---
@category_bp.route('/<int:category_id>/apps', methods=['GET'])
@swag_from({
    'tags': ['Categories'],
    'summary': 'Get apps by category',
    'parameters': [
        {'name': 'category_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'List of applications in this category'},
        500: {'description': 'Server error'}
    }
})
def get_apps_by_category(category_id):
    return controller.get_apps_by_category(category_id)
