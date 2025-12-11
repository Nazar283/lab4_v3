from flask import Blueprint
from flasgger import swag_from
from my_project.review.controller.review_controller import ReviewController

review_bp = Blueprint('review', __name__)
controller = ReviewController()


# --- Get all reviews ---
@review_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Get all reviews',
    'description': 'Returns a list of all reviews stored in the database.',
    'responses': {
        200: {'description': 'List of reviews retrieved successfully'},
        500: {'description': 'Server error'}
    }
})
def get_all_reviews():
    return controller.get_all_reviews()


# --- Get review by ID ---
@review_bp.route('/<int:review_id>', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Get a review by ID',
    'description': 'Returns review information based on the provided ID.',
    'parameters': [
        {'name': 'review_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Review found'},
        404: {'description': 'Review not found'},
        500: {'description': 'Server error'}
    }
})
def get_review_by_id(review_id):
    return controller.get_review_by_id(review_id)


# --- Create a new review ---
@review_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Create a new review',
    'description': 'Creates a new review for an app from a specific user.',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'user_id': {'type': 'integer', 'example': 1},
                'app_id': {'type': 'integer', 'example': 5},
                'rating': {'type': 'number', 'example': 4.5},
                'comment': {'type': 'string', 'example': 'Very convenient and useful app!'}
            },
            'required': ['user_id', 'app_id', 'rating']
        }
    }],
    'responses': {
        201: {'description': 'Review successfully created'},
        400: {'description': 'Invalid input data'},
        500: {'description': 'Server error'}
    }
})
def create_review():
    return controller.create_review()


# --- Update review ---
@review_bp.route('/<int:review_id>', methods=['PUT'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Update a review',
    'description': 'Updates review details such as rating or comment.',
    'parameters': [
        {'name': 'review_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'rating': {'type': 'number', 'example': 5},
                    'comment': {'type': 'string', 'example': 'Updated comment text'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Review successfully updated'},
        400: {'description': 'Invalid update data'},
        404: {'description': 'Review not found'},
        500: {'description': 'Server error'}
    }
})
def update_review(review_id):
    return controller.update_review(review_id)


# --- Delete review ---
@review_bp.route('/<int:review_id>', methods=['DELETE'])
@swag_From({
    'tags': ['Reviews'],
    'summary': 'Delete a review',
    'description': 'Deletes a review from the database.',
    'parameters': [
        {'name': 'review_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Review successfully deleted'},
        404: {'description': 'Review not found'},
        500: {'description': 'Server error'}
    }
})
def delete_review(review_id):
    return controller.delete_review(review_id)


# --- Get reviews with full details ---
@review_bp.route('/details', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Get reviews with full details (JOIN)',
    'description': 'Returns reviews including user and application info via JOIN query.',
    'responses': {
        200: {'description': 'List of detailed reviews retrieved successfully'},
        500: {'description': 'Server error'}
    }
})
def get_reviews_with_details():
    return controller.get_reviews_with_details()


# --- Get reviews by user and app ---
@review_bp.route('/user/<int:user_id>/app/<int:app_id>', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'summary': 'Get reviews by a user for a specific app',
    'description': 'Returns all reviews written by a specific user for a specific application.',
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'app_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'List of reviews retrieved successfully'},
        404: {'description': 'No reviews found for provided user and app'},
        500: {'description': 'Server error'}
    }
})
def get_reviews_by_user_and_app(user_id, app_id):
    return controller.get_reviews_by_user_and_app(user_id, app_id)
