from flask import jsonify, render_template

def not_found(error):
    return render_template("404.html", code=404), 404

def forbidden(error):
    return render_template("404.html", code=403), 403

# @errors.errorhandler(405)
# def method_not_allowed(error):
#     return jsonify({"message": "Method not allowed"}), 405

# @errors.errorhandler(422)
# def unprocessable_entity(error):
#     return jsonify({"message": "Unprocessable entity"}), 422
    