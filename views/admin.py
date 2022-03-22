from flask import Blueprint, render_template, request, redirect, url_for, abort


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return render_template('admin.html')

@admin.route('/logs')
def logs():
    return render_template('logs.html')
