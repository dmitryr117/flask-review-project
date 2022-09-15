from flask import Blueprint, request, jsonify
from utils.dto import check_dto
from utils.dto.user_dto import register_schema, login_schema
from models.user import User
from core.app import db, bcrypt
from flask_jwt_extended import set_access_cookies, jwt_required, create_access_token, unset_jwt_cookies, get_jwt_identity
import json

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
  users = User.query.all()
  return json.dumps(users)

@users.route('/register', methods=['POST'])
def register_user():
  content_type = request.headers.get('Content-Type')
  if (content_type != 'application/json'):
    return 'Content-Type not supported!'

  data = request.json
  if not check_dto(register_schema, data):
    return 'failed', 406

  hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
  user = User(username=data["username"], email=data["email"], password=hashed_password)
  db.session.add(user)
  db.session.commit()
  return '', 201

@users.route('/login', methods=['POST'])
def login_user():
  content_type = request.headers.get('Content-Type')
  if (content_type != 'application/json'):
    return jsonify({"msg": "unsupported format"})

  data = request.json
  if not check_dto(login_schema, data):
    return jsonify({"msg": "invalid data format"})
  user: User = User.query.filter_by(email=data["email"]).first()
  if user and bcrypt.check_password_hash(user.password, data["password"]):
    identity = json.dumps({
      'uid': user.id,
      'username': user.username,
      'email': user.email
    })
    response = jsonify(identity)
    access_token = create_access_token(identity=identity)
    set_access_cookies(response, access_token)
    return response
  else:
    return jsonify({"msg": "login failed"})

@users.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
  identity = get_jwt_identity()
  return jsonify(identity)

@users.route("/logout", methods=["GET"])
def logout_with_cookies():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
  
