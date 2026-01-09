pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/devops-microservice"
        DOCKER_TAG = "latest"
        SERVER_IP = "EC2_PUBLIC_IP"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_GITHUB_USERNAME/devops-microservice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
            }
        }

        stage('Deploy to Server') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no ec2-user@$SERVER_IP "
                docker pull $DOCKER_IMAGE:$DOCKER_TAG &&
                docker stop microservice || true &&
                docker rm microservice || true &&
                docker run -d -p 5000:5000 --name microservice -e ENVIRONMENT=production $DOCKER_IMAGE:$DOCKER_TAG
                "
                '''
            }
        }
    }
}
