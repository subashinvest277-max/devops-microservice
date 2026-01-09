pipeline {
    agent any

    environment {
        APP_NAME = "devops-microservice"
        DOCKER_IMAGE = "subashinvest27/devops-microservice"
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/subashinvest27/devops-microservice.git'
            }
        }

        stage('Verify Tools') {
            steps {
                sh '''
                    echo "Git version:"
                    git --version

                    echo "Docker version:"
                    docker --version || true

                    echo "Maven version:"
                    mvn -version || true
                '''
            }
        }

        stage('Build Application') {
            when {
                expression { fileExists('pom.xml') }
            }
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Docker Build') {
            when {
                expression { fileExists('Dockerfile') }
            }
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
