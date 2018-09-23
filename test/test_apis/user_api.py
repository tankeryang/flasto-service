from flask_restplus import Resource, fields, Namespace

from .model import User
from test.test_apis import api

ns = Namespace("users", description="Users CURD api.")

user_model = ns.model('UserModel', {
    'user_id': fields.String(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
})
user_list_model = ns.model('UserListModel', {
    'users': fields.List(fields.Nested(user_model)),
    'total': fields.Integer,
})


@ns.route("")
class UserListApi(Resource):
    # 初始化数据
    users = [User("HanMeiMei"), User("LiLei")]

    @ns.doc('get_user_list')
    @ns.marshal_with(user_list_model)
    def get(self):
        return {
            "users": self.users,
            "total": len(self.users),
        }

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        user = User(api.payload['username'])
        return user


@ns.route("/<string:user_id>")
@ns.response(404, 'User not found')
@ns.param('user_id', 'The user identifier')
class UserInfoApi(Resource):
    
    users = [User("HanMeiMei"), User("LiLei")]
    print([u.user_id for u in users])

    @ns.doc("get_user_by_id")
    @ns.marshal_with(user_model)
    def get(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                return u
        ns.abort(404, "User {} doesn't exist".format(user_id))

    @ns.doc("update_user_info")
    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, user_id):
        user = None
        for u in self.users:
            if u.user_id == user_id:
                user = u
        if not user:
            ns.abort(404, "User {} doesn't exist".format(user_id))
        user.username = api.payload['username']
        return user
