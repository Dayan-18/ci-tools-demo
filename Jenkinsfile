// Same pipeline, Jenkins declarative syntax.
// Requires a Jenkins agent with Docker support.

pipeline {
    agent {
        docker { image 'python:3.12' }
    }

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest test_calculator.py -v --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
