pipeline {
    agent any

   stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/Pranavanithya/devops-project.git'
    }
}


        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("flask-app:latest")
                }
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app:latest'
            }
        }
    }
}
