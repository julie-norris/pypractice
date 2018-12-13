
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api =  Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]


class User (Resource):

	def get(self, name):
		"""The get method is used to retrieve a particular user details by specifying the name"""
		""" 400 = Bad Request, 201 = Created, 200 = OK, 404 = Not Found"""
		
		for user in users:
			if(name == user["name"]):
				return user, 200
		return "User not found", 404
		
	def post(self, name):
		"""The post method is used to create a new user"""
	
		parser = reparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()
		
		for user in users:
			if(name == user["name"]):
				return "User with name {} already exists".format(name), 400
				
		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201
		
	def put(self, name):
		""" the put method is used to update details of user, or create a new one if it does not exist"""
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args( )
		
		for user in users:
			if(name == user["name"]):
				user["age"] = args["age"]
				user["occupation"] = args["occupation"]
				return user, 200
				
		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201

				
	def delete(self, name):
		""" the delete method is used to delete user that is no longer relevant. 
		By specifying users as a variable in global scope, we update the users list using list comprehension to create a list without the name specified (simulating delete)."""
	
		global users
		users = [user for user in users if user["name"] != name]
		return "{} is deleted.".format(name), 200
	
		""" <string:name> indicates that it is a variable in the route which accepts any name this is useful in development setting but shoud NEVER be used in production setting"""
	
	api.add_resource(User, "/user/<string:name>")
	app.reun(debug=True)
	
	
	
	
