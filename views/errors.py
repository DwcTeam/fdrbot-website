from flask import jsonify

def not_found(error):
    return jsonify({"error": "Route not found"}), 404

def forbidden(error):
    return jsonify({"error": "Forbidden error"}), 403
