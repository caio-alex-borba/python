from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST


atributos =reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="Campo 'login' obrigatorio")
atributos.add_argument('senha', type=str, required=True, help="Campo 'senha' obrigatorio")

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'user not found.'}, 404 #not found


    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'ocorreu um erro ao deletar o usuario.'}, 500
            return {'message': 'usuario deletado'}, 200 #ok
        return {'message': 'user not found.'}, 404

class Userregister(Resource):
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": "o login '{}' ja existe.".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message':'usuario criado com sucesso'}, 201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'login ou senha incorreta'}, 401

class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']# identificador do token
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully'}, 200