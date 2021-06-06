pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                sh "ssh -i ~/.ssh/ansible_id_rsa jenkins@swarm-master && docker stack deploy --compose-file docker-compose.yaml event_generator"
            }
        }
    }
    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'front-end/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'name-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'unit-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'effect-api/coverage.xml', failNoReports: false
        }
    }
}