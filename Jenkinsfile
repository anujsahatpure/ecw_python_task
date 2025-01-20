pipeline {
    agent any
    environment {
        SONAR_SCANNER_HOME = '/opt/sonar-scanner'
        SONARQUBE_TOKEN = credentials('SONAR_TOKEN_PYTHON')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "main", url: 'https://github.com/anujsahatpure/ecw_python_task.git'
            }
        }

        stage('Setup Environment') {
            steps {
                // Install dependencies and setup virtual environment
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests here (pytest, unittest, etc.)
                script {
                    sh '. venv/bin/activate && pytest --maxfail=5 --disable-warnings --junitxml=report.xml'
                }
            }
        }

        stage('SonarQube Scan') {
            steps {
                // Run SonarQube analysis with the token
                script {
                    sh '''
                        $SONAR_SCANNER_HOME/bin/sonar-scanner \
                        -Dsonar.projectKey=ecw_python_project \
                        -Dsonar.sources=. \
                        -Dsonar.login=$SONARQUBE_TOKEN
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                // You can add any build steps here if needed (for example, packaging your app)
                echo "Build stage complete"
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload test results or any build artifacts you want to keep
                archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
            }
        }

        stage('Cleanup') {
            steps {
                // Clean up virtual environment
                sh 'rm -rf venv'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check logs for errors.'
        }
    }
}
