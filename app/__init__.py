# # Required Imports
# import os
# from flask import Flask, request, jsonify
# from firebase_admin import credentials, firestore, initialize_app, auth
# app = Flask(__name__)


# # Autenticate Firebase
# cred = credentials.Certificate('app/key.json')
# default_app = initialize_app(cred)

# # Initialize Firestore DB
# db = firestore.client()
# users_ref = db.collection('users')
# # dir(auth)

# @app.route('/api/authenticate', methods=['POST'])
# def authenticate():
#     """
#     authenticate(): Check if username and password match
#     return True or False
#     """

# @app.route('/api/createUser', methods=['POST'])
# def create():
#     """
#         create() : Create user with an email and password
#         Add document to Firestore collection with requested user
#         Ensure you pass a username, user-email, password as part of json body in post request
#         e.g. json={'name': 'Huzaifa', 'email': 'ahmadhuzaifa012@gmail.com', 'password':'PaSsword'}
#     """
#     try:
#         name = request.json['name']
#         email = request.json['email']
#         password = request.json['password']
#         user = auth.create_user(display_name = name, email = email, password =password)
#         users_ref.add({'name': name,'email' :email})
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"


# @app.route('/users', methods=['GET'])
# def read():
#     """
#         read() : Fetches documents from Firestore collection as JSON
#         todo : Return document that matches query ID
#         all_todos : Return all documents
#     """
#     try:
#         # Check if ID was passed to URL query
#         user_id = request.args.get('uid')    
#         if user_id:
#             todo = users_ref.document(user_id).get()
#             return jsonify(todo.to_dict()), 200
#         else:
#             all_todos = [doc.to_dict() for doc in users_ref.stream()]
#             return jsonify(all_todos), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"


# port = int(os.environ.get('PORT', 8080))
# if __name__ == '__main__':
#     app.run(threaded=True, host='0.0.0.0', port=port)