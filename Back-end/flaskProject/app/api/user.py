from flask import request, Blueprint, jsonify, g
from sqlalchemy import or_
from app.libs.error_code import Success, LoginFailed, ParameterException, DeleteSuccess, AuthFailed
from app.models.base import db
from app.models.user import User
from app.validators.forms import ClientForm
from app.libs.token_auth import auth

Users = Blueprint('user', __name__)


# 注册一个账号
@Users.route('/register', methods=['POST'])
def register_one_account():
    form = ClientForm().validate_for_api()
    if User.query.filter_by(username=form.username.data).first():
        return ParameterException(msg='User already exists')
    else:
        User.register_by_username(form.username.data, form.secret.data)
        return Success(msg='Register Success')


# 删除自己的账号
@Users.route('/delete', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


# 管理员删除账号(传入id号)
@Users.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    is_admin = g.user.is_admin
    if not is_admin:
        raise AuthFailed(msg='You are not admin!')
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


# 返回所有用户信息
@Users.route('/all_user')
@auth.login_required
def get_user():
    is_admin = g.user.is_admin
    if not is_admin:
        raise AuthFailed(msg='You are not admin!')
    result = {}
    num = 0
    all = User.query.filter(User.status == 1 and User.auth == 1).all()
    for i in all:
        num = num + 1
        Dict = {"id": i.id, "username": i.username}
        key = 'user' + str(num)
        result[key] = Dict
    return jsonify(result)








