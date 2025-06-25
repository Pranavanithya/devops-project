pipeline {
    agent any

    environment {
        IMAGE_NAME = 'pranavanithya123/flask-app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Pranavanithya/devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'DOCKERHUB_CREDENTIALS',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    script {
                        sh 'echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin'
                        sh "docker push ${IMAGE_NAME}"
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo '🚀 Triggering Ansible deployment (add your logic here)...'
                // Add your Ansible command or SSH deployment here
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for errors.'
        }
    }
}

