import os.path
from app.db.models import User
from app.auth import login
from flask_login import login_user, login_required, logout_user, current_user
def login_test():
    login_user('johncena@gmail.com')
    assert current_user.__name == 'johncena@gmail.com'
    assert current_user.is_authenticated()