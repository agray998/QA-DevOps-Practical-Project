# QA-DevOps-Practical-Project  
This repository contains my deliverable for the QA DevOps practical project.

## Contents:  
*  [Project Brief](#Project-Brief)
*  [App Design](#App-Design)
*  

## Project Brief:  
The brief for this project was to produce an application consisiting of four microservices, which interact with one another to generate objects using some defined logic. This application was to be produced and maintained using a fully automated CI/CD pipeline. The full tech stack required was as follows:  
* Kanban board for project tracking
* Git for version control
* Jenkins as a CI server
* Ansible for configuration management
* GCP cloud platform
* Docker as a containerisation tool
* Docker swarm for container orchestration
* NGINX as a reverse proxy  
  
## App Design:  
In response to this brief, I have chosen to develop a strategy game random event generator. This utilises a microservice architecture as follows:  
* Front-end (service 1): The service with which the user interacts. This service sends requests to the other services to generate random events, displays the generated events to the user, as well as storing them in a database.
* Name API (service 2): This service receives HTTP GET requests from service 1 and responds with a randomly selected event name chosen from the following list: [list here]
* Unit API (service 3): This service receives HTTP GET requests from service 1, and responds with a randomly selected unit type chosen from: [list here]
* Effect API (service 4): This service receives HTTP POST requests from service 1, which provide the randomly generated event names and unit types as JSON objects, service 4 has two dictionaries which use this data to determine the status effect associated with the event; the event name determines the magnitude of the status effect and the unit type determines which of the units' statistics are affected.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible. The images below show the front-end in action:  

![front-end-home](https://i.imgur.com/imVhUta.png) ![front-end-history](https://i.imgur.com/MugpPxv.png)

## CI/CD Pipeline:
This project utilises a full CI/CD pipeline to test, build, deploy and maintain the application. The major components of this pipeline are:
* Project tracking
* Version control
* Development environment
* CI server
* Deployment environment  

Project tracking was done using Trello. Tasks were assigned story points, acceptance criteria and a MoSCoW prioritisation and moved through the stages from project backlog to complete as the project progressed. 
![trello-board](https://i.imgur.com/hNSLsh4.png)
[here](https://trello.com/b/75rHr6yu/practical-project)

Git was used for version control, with the repository hosted on github. A feature-branch model was implemented in this project to insulate the stable version of the application from ongoing development. The branch structure was as follows:  
img here

The development environment used was a virtual machine, hosted on GCP, accessed via VSCode. 

Jenkins was used as a CI server. In response to a github webhook, Jenkins cloned down the repo and executed the pipeline script defined in the Jenkinsfile. This pipeline consists of 3 stages: test, build/push and deploy. The test stage executes a bash script which cycles through the directories for the four services and runs the tests using pytest. If the tests are successful, the build/push stage uses docker-compose to build the images for the different services, logs into docker using credentials configured on the Jenkins VM, and then pushes the images to Dockerhub. Finally, the deploy stage deploys the application, initially for development purposes this was done via docker-compose on the Jenkins machine, however the production-ready deployment uses docker swarm to deploy the application across three nodes (one manager and two workers). The result of this pipeline is shown below:  

![Jenks-pipeline](https://i.imgur.com/eUYHXy0.png)

Successful stages are shown in green, whilst failed stages are shown in red. As can be seen, if one stage fails all future stages are skipped, thus the images will only be built and pushed to Dockerhub if the unit tests pass, and the app will only be redeployed if the updated images are accessible from Dockerhub.