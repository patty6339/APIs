This repo contains my files for learnings on APIs

APIs (Application Programming Interfaces) are a way for different software applications to communicate with each other. When you use an API, you're accessing certain features or data of a service, website, or app without needing to know its internal workings. Let’s go through the basics of APIs, including what they are, how they work, and how to create, use, and test them.

### 1. **What is an API?**

An API defines a set of rules and protocols for two or more systems to communicate. This can be a **web API** (for interacting with web services) or a **library API** (for interacting with software libraries).

For example:
- A weather API can provide weather data when requested.
- A payment API can process online payments.

### 2. **Types of APIs**

APIs can be classified in different ways:

- **REST (Representational State Transfer)**: This is the most common type of API used for web services. REST APIs use HTTP requests to perform operations like GET (retrieve data), POST (create new data), PUT (update data), and DELETE (delete data).
  
- **SOAP (Simple Object Access Protocol)**: This is another protocol for web services but is more complex and strict compared to REST. It uses XML-based messaging.

- **GraphQL**: A newer standard that allows clients to request exactly the data they need and nothing more.

- **RPC (Remote Procedure Call)**: In this method, you invoke a procedure (function) on a remote system.

We will focus on **REST APIs** in this guide as they are the most widely used.

### 3. **How Does a REST API Work?**

REST APIs use standard HTTP methods such as:
- **GET**: Retrieve data.
- **POST**: Create new data.
- **PUT**: Update existing data.
- **DELETE**: Delete data.

When you send an HTTP request to an API, you interact with the server. The server processes your request and sends back a response, usually in **JSON** or **XML** format.

Example: When you type a URL in your browser (like `https://api.example.com/weather?city=London`), you're sending a **GET** request to an API to retrieve weather information.

### 4. **Basic Structure of a REST API**

Let’s create a simple REST API using Python and Flask, as mentioned before. Flask is a micro web framework that allows you to quickly develop APIs.

#### Step 1: Install Flask

```bash
pip install Flask
```

#### Step 2: Create a Simple REST API

Here’s how to create a simple API that handles a **GET** request and returns JSON data:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to get data
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Patrick", "role": "Developer"},
        {"id": 2, "name": "John", "role": "Designer"},
    ]
    return jsonify(users)

# Route to add data
@app.route('/api/v1/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    return jsonify({
        "message": "User added successfully",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
```

#### Step 3: Run the API

Save the file as `app.py` and run it with:

```bash
python app.py
```

Your API will now run on `http://127.0.0.1:5000/`.

#### Step 4: Test the API

You can test your API using **Postman**, **Curl**, or simply by using your browser for `GET` requests.

1. **GET Request**: Use the following Curl command to retrieve data from the API:

   ```bash
   curl http://127.0.0.1:5000/api/v1/users
   ```

   This should return a list of users in JSON format.

2. **POST Request**: You can send data to the API using a POST request:

   ```bash
   curl -X POST http://127.0.0.1:5000/api/v1/users -H "Content-Type: application/json" -d '{"id": 3, "name": "Alice", "role": "Tester"}'
   ```

   This sends new user data to the API, and the API responds with a success message and the new data.

### 5. **API Status Codes**

In addition to sending data, an API will usually return an HTTP status code:
- **200 OK**: The request was successful.
- **201 Created**: The resource was successfully created (used in POST requests).
- **400 Bad Request**: There was an error with the request (usually incorrect syntax).
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: Something went wrong on the server side.

### 6. **Error Handling in APIs**

Good APIs handle errors gracefully and return meaningful error messages.

Example of error handling in Flask:

```python
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = [
        {"id": 1, "name": "Patrick", "role": "Developer"},
        {"id": 2, "name": "John", "role": "Designer"},
    ]
    
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
```

### 7. **API Authentication**

Many APIs require authentication to control access to the services. The most common ways are:
- **API Key**: A token passed in the request header.
- **OAuth**: An open standard for access delegation used by many large providers like Google, Facebook, etc.

Example: Passing an API key in the request header:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:5000/api/v1/users
```

### 8. **Connect APIs with Databases**

APIs often connect with databases to store and retrieve data. Here's a simple example of how you can integrate Flask with an SQLite database using **SQLAlchemy**:

1. Install SQLAlchemy:
   ```bash
   pip install Flask-SQLAlchemy
   ```

2. Set up a database and use it in your API:

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "role": user.role} for user in users])

@app.route('/api/v1/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

### 9. **Best Practices for APIs**
- **Use meaningful status codes**.
- **Version your API** (e.g., `/api/v1/`).
- **Use proper authentication** (API keys, OAuth).
- **Document your API** so others can understand how to use it. You can use tools like **Swagger** or **Postman** for documentation.

### 10. **Testing APIs**

You can use tools like **Postman**, **Curl**, or **pytest** (in Python) to automate tests for your API endpoints to ensure they behave as expected.

---

This overview covers the essential aspects of APIs and how to create them using Python and Flask. Let me know if you'd like to explore specific aspects like connecting to more complex databases, adding authentication, or deploying the API to a cloud service like AWS or Heroku!


### Common Curl Commands

Here’s a list of common `curl` commands used to interact with APIs, along with brief explanations for each:

### 1. **GET Request**
Retrieve data from a server.
```bash
curl http://example.com/api/resource
```
- **Explanation**: Fetches data from the specified URL. Commonly used to retrieve resources or data.

### 2. **POST Request**
Send data to a server to create a new resource.
```bash
curl -X POST http://example.com/api/resource -H "Content-Type: application/json" -d '{"key": "value"}'
```
- **Explanation**: Sends data (e.g., JSON) to the server to create a new resource. `-d` specifies the data to send, and `-H` sets the content type.

### 3. **PUT Request**
Update an existing resource on the server.
```bash
curl -X PUT http://example.com/api/resource/1 -H "Content-Type: application/json" -d '{"key": "new_value"}'
```
- **Explanation**: Updates the resource at the specified URL. `-X PUT` indicates that this is a PUT request.

### 4. **DELETE Request**
Delete a resource from the server.
```bash
curl -X DELETE http://example.com/api/resource/1
```
- **Explanation**: Deletes the resource identified by the URL.

### 5. **HEAD Request**
Retrieve headers for a resource.
```bash
curl -I http://example.com/api/resource
```
- **Explanation**: Fetches only the headers of the specified resource, without the body.

### 6. **PATCH Request**
Apply partial modifications to a resource.
```bash
curl -X PATCH http://example.com/api/resource/1 -H "Content-Type: application/json" -d '{"key": "partial_update"}'
```
- **Explanation**: Sends partial updates to the resource specified by the URL.

### 7. **Request with Basic Authentication**
Send a request with Basic Authentication credentials.
```bash
curl -u username:password http://example.com/api/resource
```
- **Explanation**: Includes authentication credentials in the request header.

### 8. **Request with Bearer Token Authentication**
Send a request with a Bearer token.
```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://example.com/api/resource
```
- **Explanation**: Adds an Authorization header with a Bearer token for authentication.

### 9. **Request with Custom Headers**
Add custom headers to a request.
```bash
curl -H "Custom-Header: value" http://example.com/api/resource
```
- **Explanation**: Includes custom headers in the request.

### 10. **Verbose Output**
Show detailed request and response information.
```bash
curl -v http://example.com/api/resource
```
- **Explanation**: Provides detailed information about the request and response, useful for debugging.

### 11. **Silent Mode**
Suppress progress meter and error messages.
```bash
curl -s http://example.com/api/resource
```
- **Explanation**: Hides the progress meter and error messages. Use `-sS` to still show errors.

### 12. **Save Response to File**
Save the response body to a file.
```bash
curl -o filename.txt http://example.com/api/resource
```
- **Explanation**: Writes the response to a file named `filename.txt`.

### 13. **Follow Redirects**
Follow HTTP redirects.
```bash
curl -L http://example.com/api/resource
```
- **Explanation**: Follows any HTTP redirects returned by the server.

### 14. **Send Data as Form Data**
Send data as form-urlencoded.
```bash
curl -X POST -d "key=value&another_key=another_value" http://example.com/api/resource
```
- **Explanation**: Sends form data as `application/x-www-form-urlencoded`.

### 15. **Send Data from File**
Send data from a file.
```bash
curl -d @data.json -H "Content-Type: application/json" http://example.com/api/resource
```
- **Explanation**: Sends the contents of `data.json` as the request body.

These commands cover most of the common scenarios when interacting with APIs using `curl`. Adjust the URL and data according to your specific API and use case.

# Postman Tutorial

https://www.youtube.com/watch?v=CLG0ha_a0q8


## Postman Operations on a Local Server

Here’s a step-by-step tutorial on how to use Postman to perform various types of HTTP requests (GET, POST, PUT, DELETE, HEAD) with a server running at `http://127.0.0.1:5000`.

### **1. Open Postman**

Start the Postman application on your computer.

### **2. Setup a New Request**

1. **Create a New Request**:
   - Click on the **"New"** button in the top-left corner.
   - Select **"Request"** from the dropdown menu.
   - Name your request, choose or create a collection, and click **"Save"**.

### **3. Perform a GET Request**

1. **Enter Request URL**:
   - In the **"Enter request URL"** field, type `http://127.0.0.1:5000/api/v1/users` (or any endpoint you want to test).

2. **Select Method**:
   - Select **"GET"** from the HTTP method dropdown.

3. **Send Request**:
   - Click the **"Send"** button.

4. **View Response**:
   - Check the response in the lower section of Postman. You will see the returned data from your server.

### **4. Perform a POST Request**

1. **Enter Request URL**:
   - Type `http://127.0.0.1:5000/api/v1/users` (or your target endpoint).

2. **Select Method**:
   - Select **"POST"** from the dropdown.

3. **Add Headers** (if required):
   - Click on the **"Headers"** tab.
   - Add headers such as `Content-Type: application/json`.

4. **Add Body**:
   - Click on the **"Body"** tab.
   - Select **"raw"** and then choose `JSON` from the dropdown.
   - Enter the JSON payload. For example:
     ```json
     {
       "name": "Alice",
       "role": "Tester"
     }
     ```

5. **Send Request**:
   - Click the **"Send"** button.

6. **View Response**:
   - Review the response returned by the server.

### **5. Perform a PUT Request**

1. **Enter Request URL**:
   - Type `http://127.0.0.1:5000/api/v1/users/1` (assuming `1` is the user ID you want to update).

2. **Select Method**:
   - Select **"PUT"** from the dropdown.

3. **Add Headers** (if required):
   - Add headers such as `Content-Type: application/json`.

4. **Add Body**:
   - Click on the **"Body"** tab.
   - Select **"raw"** and then choose `JSON` from the dropdown.
   - Enter the updated JSON payload. For example:
     ```json
     {
       "name": "Alice",
       "role": "Senior Tester"
     }
     ```

5. **Send Request**:
   - Click the **"Send"** button.

6. **View Response**:
   - Check the response from the server to confirm the update.

### **6. Perform a DELETE Request**

1. **Enter Request URL**:
   - Type `http://127.0.0.1:5000/api/v1/users/1` (assuming `1` is the user ID you want to delete).

2. **Select Method**:
   - Select **"DELETE"** from the dropdown.

3. **Send Request**:
   - Click the **"Send"** button.

4. **View Response**:
   - Review the response to confirm the deletion.

### **7. Perform a HEAD Request**

1. **Enter Request URL**:
   - Type `http://127.0.0.1:5000/api/v1/users` (or any endpoint).

2. **Select Method**:
   - Select **"HEAD"** from the dropdown. Note: The HEAD method is not always supported, but if your server supports it, it will return only headers.

3. **Send Request**:
   - Click the **"Send"** button.

4. **View Response**:
   - Check the headers in the response section. The body will not be returned with a HEAD request, only headers.

### **Summary**

- **GET**: Retrieve data.
- **POST**: Create a new resource.
- **PUT**: Update an existing resource.
- **DELETE**: Remove a resource.
- **HEAD**: Retrieve headers only.

By following these steps, you can use Postman to test various HTTP methods and interact with your server at `http://127.0.0.1:5000`.