from werkzeug.security import generate_password_hash
from App import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema

def post_user():
    username =  request.form['username']
    password =  request.form['password']
    name     =  request.form['name']
    question =  request.form['question']
    answer   =  request.form['answer']

    pass_hash = generate_password_hash(password)
    user = Users(username,pass_hash,name,question,answer)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        print(result)
        return 'OK'
    except:
        return 'ERROR'
    
def update_user():
    user =  request.form['username']
    password =  request.form['password']
    answer   =  request.form['answer']

    user = Users.query.filter_by(username=user).first()

    if not user:
        return 'Usuario não encontrado'
    
    if user.answer != answer:
        return 'Senha de segurança invalida'

    pass_hash = generate_password_hash(password)

    try:
        user.password = pass_hash
        db.session.commit()
        result = user_schema.dump(user)
        print(result)
        return 'OK'
    except:
        return 'Falha ao atualizar'
    
def get_user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None