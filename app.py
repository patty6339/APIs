# # Description: A simple Flask API with two routes to get and add data.

# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, Flask!"

# # Route to get data
# @app.route('/api/v1/users', methods=['GET'])
# def get_users():
#     users = [
#         {"id": 1, "name": "Patrick", "role": "Developer"},
#         {"id": 2, "name": "John", "role": "Designer"},
#     ]
#     return jsonify(users)

# # Route to add data
# @app.route('/api/v1/users', methods=['POST'])
# def add_user():
#     new_user = request.get_json()
#     return jsonify({
#         "message": "User added successfully",
#         "user": new_user
#     }), 201

# @app.route('/api/v1/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     users = [
#         {"id": 1, "name": "Patrick", "role": "Developer"},
#         {"id": 2, "name": "John", "role": "Designer"},
#     ]
    
#     user = next((u for u in users if u['id'] == user_id), None)
    
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"error": "User not found"}), 404


# if __name__ == '__main__':
#     app.run(debug=True)

# Description: A simple Flask API with two routes to get and add data.

# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     role = db.Column(db.String(50), nullable=False)

# @app.route('/')
# def home():
#     return "Hello, Flask!"

# # Route to get data
# @app.route('/api/v1/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify([{"id": user.id, "name": user.name, "role": user.role} for user in users])

# # Route to add data
# @app.route('/api/v1/users', methods=['POST'])
# def add_user():
#     data = request.get_json()
#     new_user = User(name=data['name'], role=data['role'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User added successfully"}), 201

# @app.route('/api/v1/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get(user_id)
#     if user:
#         return jsonify({"id": user.id, "name": user.name, "role": user.role})
#     else:
#         return jsonify({"error": "User not found"}), 404

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

# Description: A simple Flask API with routes to get, add, update, and delete data.

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return "Hello, Flask!"

# Route to get data
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "role": user.role} for user in users])

# Route to add data
@app.route('/api/v1/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

# Route to get a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "role": user.role})
    else:
        return jsonify({"error": "User not found"}), 404

# Route to update a user
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.name = data['name']
        user.role = data['role']
        db.session.commit()
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

# Route to delete a user
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
