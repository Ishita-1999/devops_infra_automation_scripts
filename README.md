# Task 1. Create an in-memory key-value store HTTP API Service which implements:
- /get/<key> ----> Return value of the key
- /set ----> Post call which sets the key/value pair
 
## Solution 1:
Created Flask API application instance. It uses a dictionary (key_value_store) to store key-value pairs. It has two routes:
GET /get/<key>: Retrieves the value associated with the specified key from the dictionary. Returns the key-value pair as JSON or an error message if the key is not found.
POST /set: Sets a key-value pair in the dictionary based on the JSON data received in the request. Responds with a success message or an error if the request data is invalid.
When executed as the main script, it runs the Flask app in debug mode.

<img width="1179" alt="image" src="https://github.com/Ishita-1999/devops_knorex/assets/61704617/0551f2bd-e77e-456c-8d8b-07d6568054e0">

# Task 2. It should have a Dockerfile

## Solution 2: 
Created and pushed to Docker hub.
https://hub.docker.com/r/ishita1999/devops_knorex

# Task 3. DevOps Evaluation(Kubernetes):
- Write a CI/CD pipeline to deploy the Docker image to some Docker repository (preferably
Dockerhub)
- Deploy this image into a Kubernetes cluster <--- assume that the
Jenkins/CircleCI/TravisCI has Admin access to the K8s cluster, so running kubectl apply -f
./knx-key-value-assignment.yaml from Pipeline itself would work fine.
- Write the Service, Ingress etc for the K8s resource.

## Solution 3:
- Created Jenkins CI/CD pipeline to build docker image and pushed the same to docker hub repository.
- Deployed the knx-key-value deployment, service and ngress on ubuntu virtual machine where kubernetes is running.
