pipeline {
    agent any

    environment {
        SERVER_CREDS = credentials('server-creds')

    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                echo "server creds: ${SERVER_CREDS}"
                echo "server username: ${SERVER_CREDS_USR}"
                echo "server password: ${SERVER_CREDS_PWS}"
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying....New Feature Addded"
            }
        }
    }
}