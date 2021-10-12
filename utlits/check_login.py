from flask import flash, session, redirect
from functools import wraps

def login_required(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        if "token" in session:
            # Success!
            return function_to_protect(*args, **kwargs)
        flash("Please log in")
        return redirect("/login")
    return wrapper
