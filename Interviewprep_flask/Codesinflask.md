### HTTP Code Requests

In Flask, HTTP status codes are returned to indicate the outcome of a client's request. These codes follow the standard HTTP status code definitions. Here's a breakdown of the most commonly used HTTP status codes and their meanings:

### 1. **1xx Informational Codes**
These codes indicate that the request has been received and is being processed.

- **100 Continue**: The server has received the initial part of the request and the client can continue.
- **101 Switching Protocols**: The server is switching to a different protocol as requested by the client.

### 2. **2xx Success Codes**
These codes indicate that the request was successfully received, understood, and processed.

- **200 OK**: The request was successful, and the server returned the requested data or action.
  - Example: A successful `GET` request.
- **201 Created**: The request was successful, and a new resource was created as a result.
  - Example: A successful `POST` request creating a new item.
- **204 No Content**: The request was successful, but there is no content to send in the response.
  - Example: A successful `DELETE` request where the resource was deleted.

### 3. **3xx Redirection Codes**
These codes indicate that further action is needed to complete the request.

- **301 Moved Permanently**: The requested resource has been permanently moved to a new URL.
- **302 Found**: The resource has been temporarily moved to a different URL.
- **304 Not Modified**: The resource has not been modified since the last request, so no new data is returned.

### 4. **4xx Client Error Codes**
These codes indicate that there was a problem with the client's request.

- **400 Bad Request**: The server could not understand the request due to malformed syntax or invalid input.
  - Example: Incorrect or missing data in a `POST` or `PUT` request.
- **401 Unauthorized**: Authentication is required to access the resource but was not provided or failed.
  - Example: Accessing a protected API endpoint without providing valid credentials.
- **403 Forbidden**: The server understood the request but refuses to authorize it.
  - Example: A user trying to access a resource they don't have permission for.
- **404 Not Found**: The requested resource could not be found on the server.
  - Example: Trying to access an endpoint or resource that doesn't exist.
- **405 Method Not Allowed**: The request method (e.g., `POST`, `GET`) is not supported for the requested resource.
  - Example: Trying to `POST` to a URL that only supports `GET`.
- **409 Conflict**: The request could not be processed because of a conflict in the current state of the resource.
  - Example: Trying to create a resource that already exists.
- **429 Too Many Requests**: The client has sent too many requests in a given amount of time and is being rate-limited.

### 5. **5xx Server Error Codes**
These codes indicate that the server encountered an error while processing the request.

- **500 Internal Server Error**: A generic error message indicating the server encountered an unexpected condition.
  - Example: An unhandled exception in the application.
- **502 Bad Gateway**: The server, while acting as a gateway, received an invalid response from the upstream server.
- **503 Service Unavailable**: The server is temporarily unable to handle the request due to overload or maintenance.
- **504 Gateway Timeout**: The server, acting as a gateway, did not receive a timely response from the upstream server.

### Example of Returning Status Codes in Flask

In Flask, you can explicitly return a status code along with a response using the following syntax:
```python
from flask import jsonify

@app.route('/items', methods=['POST'])
def create_item():
    if invalid_input():
        return jsonify({'error': 'Bad request'}), 400  # 400 Bad Request
    new_item = save_item()
    return jsonify(new_item), 201  # 201 Created
```

By understanding and using the appropriate status codes, you can make your Flask API more robust and provide meaningful feedback to clients.
