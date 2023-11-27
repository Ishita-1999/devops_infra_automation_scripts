Task 1. Create an in-memory key-value store HTTP API Service which implements:
• /get/<key> ----> Return value of the key
• /set ----> Post call which sets the key/value pair
 
Solution:
Created Flask API application instance. It uses a dictionary (key_value_store) to store key-value pairs. It has two routes:
GET /get/<key>: Retrieves the value associated with the specified key from the dictionary. Returns the key-value pair as JSON or an error message if the key is not found.
POST /set: Sets a key-value pair in the dictionary based on the JSON data received in the request. Responds with a success message or an error if the request data is invalid.
When executed as the main script, it runs the Flask app in debug mode.

<img width="1179" alt="image" src="https://github.com/Ishita-1999/devops_knorex/assets/61704617/0551f2bd-e77e-456c-8d8b-07d6568054e0">

