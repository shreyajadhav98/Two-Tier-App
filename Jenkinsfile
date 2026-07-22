pipeline {

    agent any

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Stop Existing Containers') {
            steps {
                sh '''
                docker compose down || true
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker compose build
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                docker compose up -d
                '''
            }
        }

        stage('Verify Running Containers') {
            steps {
                sh '''
                docker ps
                '''
            }
        }

    }

}