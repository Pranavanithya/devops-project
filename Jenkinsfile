pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')  // Jenkins credentials ID
        IMAGE_NAME = 'pranavanithya123/flask-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Pranavanithya/devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh '''
                  cd ansible
                  ansible-playbook -i hosts playbook.yml
                '''
            }
        }
    }
}
