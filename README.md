README - Kubernetes Cluster with Services

**Project Description**

This project involves creating a Kubernetes (K8S) cluster in Azure using AKS. The cluster includes two services, Service-A and Service-B, with the following requirements:

- Create a K8S cluster with RBAC enabled.
- Add an Ingress controller to route traffic based on URLs:
- xxx/service-A
- xxx/service-B
- Prevent communication between Service-A and Service-B using a net- work policy.
- Develop an application for Service-A that fetches the Bitcoin value in USD every minute and calculates the 10-minute moving average every 10 minutes.

**File Structure**

The project files are located in the k8sCluster directory and include:

- main.tf: Terraform file for creating the resource group and K8S clus- ter.
- YAML files:
    - service-a.yaml: Deployment and service configuration for Service-A
    - service-b.yaml: Deployment and service configuration for Service-B
    - network-policy.yaml: Network policy to block communication between the services.
    - ingress.yaml: Ingress controller configuration.
- Dockerfile: Dockerfile to build the Service-A image.
- app/ directory:
    - service_a_app.py: Python application for tracking Bitcoin value.
    - templates/index.html: HTML template for displaying the data.

**Steps to Execute**

1. Create the resource group and K8S cluster using main.tf.
2. Deploy the services (Service-A and Service-B) using the YAML files.
3. Apply the network policy to block communication between the services using network-policy.yaml.
4. Configure the Ingress controller to route traffic based on URLs using ingress.yaml.
5. Build the Docker image for Service-A using the Dockerfile.
6. Run Service-A:
    - Fetch the Bitcoin value in USD using the API: [https://api. coindesk.com/v1/bpi/currentprice/BTC.json.](https://api.coindesk.com/v1/bpi/currentprice/BTC.json)
    - Display the current value and the 10-minute moving average.

**How to Run the Project**

1. Ensure you have an active Azure account with appropriate permissions.
2. Install the following tools:
    - Terraform
    - Azure CLI
    - Docker
    - kubectl
3. Run the Terraform script to create the cluster:

    - terraform init 
    - terraform apply

4. Deploy the services and network policies:

    - kubectl apply -f service-a.yaml 
    - kubectl apply -f service-b.yaml 
    - kubectl apply -f network-policy.yaml 
    - kubectl apply -f ingress.yaml

5. Build and push the Docker image for Service-A:

    - docker build -t <your-dockerhub-username>/service-a:latest . 
    - docker push <your-dockerhub-username>/service-a:latest
