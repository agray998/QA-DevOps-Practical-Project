pipeline {
    agent any
    stages {
        stage('Clone down repo dev branch') {
            steps {
                sh "git clone https://github.com/agray998/QA-DevOps-Practical-Project.git --branch dev"
                sh "cd QA-DevOps-Practical-Project"
            }
        }
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $docker_uname -p $docker_pword"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }
}