pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps{
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running validation tests...'
              
                sh 'pip install pytest && pytest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t banking-app:${BUILD_NUMBER} .'
            }
        }
    }
}
