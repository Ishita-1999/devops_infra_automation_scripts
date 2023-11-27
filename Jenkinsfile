pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhublogin')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t ishita1999/devops_knorex:flask .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push ishita1999/devops_knorex:flask'
      }
    }
  }
  steps(deploy) 
  {
                script {
                    // Pull the latest code
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "rm -rf devops_knorex"'
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "git clone https://github.com/Ishita-1999/devops_knorex.git"'
                    sh 'ssh -o StrictHostKeyChecking=no ishi@3.93.201.0 "kubectl apply -f /home/ishi/devops_knorex/knx-key-value-assignment.yaml"'
 
                }
            }
        
}
