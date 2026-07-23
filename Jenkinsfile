pipeline {
    agent any

    // Enable GitHub webhook triggering
    triggers {
        githubPush()
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling latest code from GitHub...'
                // Code checkout is automatically handled by Pipeline SCM
            }
        }

        stage('Stop & Clean Containers') {
            steps {
                echo 'Stopping existing containers...'
                sh 'docker compose down || true'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker images...'
                sh 'docker compose build'
            }
        }

        stage('Deploy (Docker Compose Up)') {
            steps {
                echo 'Deploying application...'
                sh 'docker compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying active containers...'
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Phase 10 automated deployment complete!'
            echo 'App live at: http://localhost:5000'
        }
        failure {
            echo 'FAILURE: Automation pipeline failed. Check console logs.'
        }
    }
}