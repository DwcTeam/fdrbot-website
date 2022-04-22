from flask import jsonify

def not_found(error):
    return jsonify({"error": error}), 404

def forbidden(error):
    return jsonify({"error": error}), 403
