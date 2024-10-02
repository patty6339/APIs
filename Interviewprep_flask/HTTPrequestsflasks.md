### HTTP Requests in Flask

In Flask, HTTP request types (also known as HTTP methods) determine the action that a client wants to perform on a resource. Here are the most common HTTP request types you can handle in a Flask application:

### 1. GET
- **Purpose**: Retrieves data from the server.
- **Usage**: Used for fetching resources or displaying pages.
- **Example**:
  ```python
  @app.route('/items', methods=['GET'])
  def get_items():
      return {'items': ['item1', 'item2', 'item3']}
  ```

### 2. POST
- **Purpose**: Sends data to the server to create or update a resource.
- **Usage**: Often used to submit forms or upload files.
- **Example**:
  ```python
  @app.route('/items', methods=['POST'])
  def create_item():
      new_item = request.json  # Get JSON data from request
      # Process the new item (e.g., save to database)
      return {'message': 'Item created'}, 201
  ```

### 3. PUT
- **Purpose**: Updates an existing resource with new data.
- **Usage**: Typically used for full updates of a resource.
- **Example**:
  ```python
  @app.route('/items/<int:item_id>', methods=['PUT'])
  def update_item(item_id):
      updated_item = request.json  # Get updated data
      # Update the item in the database
      return {'message': 'Item updated'}
  ```

### 4. PATCH
- **Purpose**: Partially updates an existing resource.
- **Usage**: Used when only a subset of the resource needs to be updated.
- **Example**:
  ```python
  @app.route('/items/<int:item_id>', methods=['PATCH'])
  def patch_item(item_id):
      update_data = request.json  # Get partial data
      # Apply the update to the existing item
      return {'message': 'Item partially updated'}
  ```

### 5. DELETE
- **Purpose**: Deletes a resource from the server.
- **Usage**: Used when you want to remove a resource.
- **Example**:
  ```python
  @app.route('/items/<int:item_id>', methods=['DELETE'])
  def delete_item(item_id):
      # Delete the item from the database
      return {'message': 'Item deleted'}
  ```

### 6. OPTIONS
- **Purpose**: Describes the communication options for the target resource.
- **Usage**: Used mainly for CORS (Cross-Origin Resource Sharing) preflight requests.
- **Example**:
  ```python
  @app.route('/items', methods=['OPTIONS'])
  def options_items():
      return {'methods': ['GET', 'POST', 'PUT', 'DELETE']}
  ```

### 7. HEAD
- **Purpose**: Similar to GET but retrieves only the headers of a resource, not the body.
- **Usage**: Used for checking if a resource is available or for retrieving metadata.
- **Example**:
  ```python
  @app.route('/items', methods=['HEAD'])
  def head_items():
      return '', 204  # No content response
  ```

### Summary
In Flask, you can define routes that respond to different HTTP methods, allowing your application to perform a variety of actions based on client requests. Properly using these methods helps maintain RESTful principles in web applications.