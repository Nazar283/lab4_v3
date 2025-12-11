from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger

from my_project.app.route.app_routes import app_bp
from my_project.user.route.user_routes import user_bp
from my_project.developer.route.developer_routes import developer_bp
from my_project.category.route.category_routes import category_bp
from my_project.review.route.review_routes import review_bp
from my_project.installation.route.installation_routes import installation_bp
from my_project.country.route.country_routes import country_bp

app = Flask(__name__)
CORS(app)

# --- Swagger Config ---
swagger_template = {
    "info": {
        "title": "GooglePlayStore API",
        "description": "REST API documentation with interactive testing capabilities.",
        "version": "1.0.0",
        "contact": {
            "name": "API Support",
            "email": "support@example.com"
        },
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": ["http"],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

swagger = Swagger(app, config=swagger_config)
# --- End Swagger Config ---

# --- Реєстрація Blueprint'ів ---
app.register_blueprint(app_bp, url_prefix='/api/apps')
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(developer_bp, url_prefix='/api/developers')
app.register_blueprint(category_bp, url_prefix='/api/categories')
app.register_blueprint(review_bp, url_prefix='/api/reviews')
app.register_blueprint(installation_bp, url_prefix='/api/installations')
app.register_blueprint(country_bp, url_prefix='/api/countries')
# --- Кінець реєстрації ---

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
