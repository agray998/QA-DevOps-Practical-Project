# QA-DevOps-Practical-Project  
This repository contains my deliverable for the QA DevOps practical project.
## Contents:  
*  [Project Brief](#Project-Brief)
*  [Project Planning](#Project-Planning)
*  [App Design](#App-Design)
*  [CI/CD Pipeline](#CI/CD-Pipeline)
*  [Known Issues](#Known-Issues)
*  [Future Work](#Future-Work)

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

## Project Planning:
When planning this project, a full risk assessment was undertaken in order to identify hazards associated with this project; this is shown below:

![RA](https://i.imgur.com/qJS8FBj.png)

Since users are not submitting any information to this app, the main focus of this risk assessment was on operational risks: i.e. those associated with building and deployment. As can be seen, for each hazard, the probability and impact factor were quantified before and after the implementation of control measures in order to guide development.

## App Design:  
In response to this brief, I have chosen to develop a strategy game random event generator. This utilises a microservice architecture as follows:  
* Front-end (service 1): The service with which the user interacts. This service sends requests to the other services to generate random events, displays the generated events to the user, as well as storing them in a database.
* Name API (service 2): This service receives HTTP GET requests from service 1 and responds with a randomly selected event name chosen from a list of names using random.choice().
* Unit API (service 3): This service receives HTTP GET requests from service 1, and responds with a randomly selected unit type chosen from a list, again by random.choice().
* Effect API (service 4): This service receives HTTP POST requests from service 1, which provide the randomly generated event names and unit types as JSON objects, service 4 has two dictionaries which use this data to determine the status effect associated with the event; the event name determines the magnitude of the status effect and the unit type determines which of the units' statistics are affected.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible. The images below show the front-end in action:  

![front-end-home](https://i.imgur.com/imVhUta.png) ![front-end-history](https://i.imgur.com/MugpPxv.png)

The first image shows the home page, this was originally the only route the front end had, to make the page more readable a history page was added to display the full history of generated events, so the home page could be limited to just the current event and the five most recent events; this history page is shown in the second image above. The events generated were stored in a database, the entity diagram (ED) for this is shown below:

![ED](https://i.imgur.com/0dN4mk6.png)

Currently, the database is stored in an sqlite file, due to issues connecting the app to a MySQL service, the overall microservice architecture is thus:

![Architecture](https://i.imgur.com/42mJcPR.png)

## CI/CD Pipeline:
This project utilises a full CI/CD pipeline to test, build, deploy and maintain the application. The major components of this pipeline are:
* Project tracking
* Version control
* Development environment
* CI server
* Deployment environment  

Project tracking was done using Trello. Tasks were assigned story points, acceptance criteria and a MoSCoW prioritisation and moved through the stages from project backlog to complete as the project progressed. 

![trello-board](https://i.imgur.com/hNSLsh4.png)  

For more details, the trello board can be accessed [here](https://trello.com/b/75rHr6yu/practical-project)

Git was used for version control, with the repository hosted on github. A feature-branch model was implemented in this project to insulate the stable version of the application from ongoing development. The branch structure was as follows:  

![Branch-model](https://i.imgur.com/ZRUkDvL.png)

The development environment used was a Ubuntu virtual machine, hosted on GCP, accessed via VSCode. 

Jenkins was used as a CI server. In response to a github webhook, Jenkins cloned down the repo and executed the pipeline script defined in the Jenkinsfile. This pipeline consists of 4 main stages: test, build/push,deploy and post-build actions. The test stage executes a bash script which cycles through the directories for the four services and runs unit tests using pytest. The front-end and all APIs had unit tests written to test all areas of functionality. To test the HTTP requests made by the front-end, requests_mock was used to simulate responses from the APIs. To test the functionality of the APIs themselves, the random.choice function was patched with unittest.mock to ensure reproducible test performance. The results of the tests are published in xml format using j-unit and cobertura, these reports show percent code coverage as well as trends in test results over time:  

![cov-report](https://i.imgur.com/Iz5vh4z.png)

As can be seen here, 100% coverage was achieved for all tests; this ensured that all of the functions of the app worked exactly as intended.

If the tests are successful, the build/push stage uses docker-compose to build the images for the different services, logs into docker using credentials configured on the Jenkins VM, and then pushes the images to Dockerhub. The use of a Jenkins pipeline, with this stage-by-stage breakdown, makes optimisation of the project easier. For example, initially all pip installs, for tests and deployment, were done using one requirements file, which meant that testing modules were being installed when building the images; since this was not necessary and since the build/push stage was the longest stage in the pipeline the requirements were separated into a requirements.txt file, containing only the pip installs needed to run the app, and a test_requirements.txt file, which contained all requirements including testing modules. This eliminated unnecessary pip installs during the build stage and reduced the average build/push time over three pipeline runs from around two-and-a-half minutes to around one minute and fifty seconds, a reduction of around 27%:

| Run | Before separation of pip installs | After separation of pip installs |
| --- | --------------------------------- | -------------------------------- |
| 1   | 02:12                             | 01:45                            |
| 2   | 02:33                             | 01:53                            |
| 3   | 02:48                             | 01:48                            |

Following the build and push, the deploy stage deploys the application. First the docker-compose.yaml and nginx.conf files are copied to the manager node by secure copy (scp). Then, an ansible playbook is used to run three roles: the first installs docker on the swarm machines if it is not present already and adds jenkins to the docker group, the second initialises a swarm on the manager node and uses the Ansible docker stack module to deploy the application, and the third adds the worker node to the swarm. This creates an overlay network as follows:

![Swarm](https://i.imgur.com/RmMd02R.png)

Finally, in the post-build stage, the j-unit and cobertura test reports are published. The result of this pipeline is shown below:  

![Jenks-pipeline](https://i.imgur.com/wXi0QuL.png)

Successful stages appear green, unstable builds are indicated by yellow stages, and failures are indicated via red stages. If a stage fails, later stages will be skipped, preventing failed versions from being deployed, this can be seen here:  

![pipeline-w-failure](https://i.imgur.com/eUYHXy0.png)

The overall structure of the CI/CD pipeline is:

![CI/CD](https://i.imgur.com/OCDefsv.png)

## Known Issues:
* Due to the use of an sqlite database, data is not persisted between services. Future work would address this as a matter of priority

## Future Improvements:  
The first future improvement would, as mentioned, be the use of a database which can persist data. The app could also be further improved in future sprints by using a locally hosted Nexus repository to speed up deployment, as the images would then not have to be fetched from Dockerhub, and by using another NGINX service as an external load balancer, to provide a single point of entry to the application.
