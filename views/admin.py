from flask import Blueprint, render_template, session, current_app as app
from utlits import is_admin, Auth, convert_data_user
from utlits.checks import only_admin


admin = Blueprint('admin', __name__, url_prefix='/admin')

