# handlers.py
from flask import jsonify
from werkzeug.exceptions import NotFound, BadRequest


def register_error_handlers(app):
    @app.errorhandler(NotFound)
    def handle_not_found(error):
        return jsonify({"message": str(error)}), 404

    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        return jsonify({"message": "Invalid request", "error": str(error)}), 400

    @app.errorhandler(Exception)
    def handle_general_exception(error):
        return jsonify({"message": "Something went wrong", "error": str(error)}), 500
