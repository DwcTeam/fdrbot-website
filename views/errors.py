from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not found"}), 404

@errors.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal error"}), 500

@errors.errorhandler(400)
def bad_request(error):
    return jsonify({"message": "Bad request"}), 400

@errors.errorhandler(401)
def unauthorized(error):
    return jsonify({"message": "Unauthorized"}), 401

@errors.errorhandler(403)
def forbidden(error):
    return jsonify({"message": "Forbidden"}), 403

@errors.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"message": "Method not allowed"}), 405

@errors.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({"message": "Unprocessable entity"}), 422

@errors.errorhandler(429)
def too_many_requests(error):
    return jsonify({"message": "Too many requests"}), 429

@errors.errorhandler(502)
def bad_gateway(error):
    return jsonify({"message": "Bad gateway"}), 502

@errors.errorhandler(503)
def service_unavailable(error):
    return jsonify({"message": "Service unavailable"}), 503

@errors.errorhandler(504)
def gateway_timeout(error):
    return jsonify({"message": "Gateway timeout"}), 504
    