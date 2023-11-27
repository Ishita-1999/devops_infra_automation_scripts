pipeline {
    agent any

    environment {
        // Define your Docker Hub credentials
        DOCKERHUB_CREDENTIALS = credentials('dockerhublogin')
    }

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Pull the latest code
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "rm -rf devops_knorex"'
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "git clone https://github.com/Ishita-1999/devops_knorex.git"'
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "cd /home/ishi/devops_knorex && docker build -t ishita1999/devops_knorex:flask ."'
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "docker login -u ishita1999 -p Himanshu20June && docker push ishita1999/devops_knorex:flask"'
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "kubectl apply -f /home/ishi/devops_knorex/knx-key-value-assignment.yaml"'

                }
            }
        }
    }
}
