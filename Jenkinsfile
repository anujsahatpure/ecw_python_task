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
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests with Coverage') {
            steps {
                script {
                    // Run tests with coverage reporting
                    sh '''
                        . venv/bin/activate
                        pytest --cov=app --cov-report=xml:coverage.xml --cov-report=html:coverage_html --junitxml=report.xml test_app.py
                    '''
                }
            }
        }
        stage('SonarQube Scan') {
            steps {
                script {
                    sh '''
                        $SONAR_SCANNER_HOME/bin/sonar-scanner \
                        -Dsonar.projectKey=ecw_python_project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.python.coverage.reportPaths=coverage.xml \
                        -Dsonar.token=$SONARQUBE_TOKEN
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                echo "Build stage complete"
            }
        }
        stage('Upload Artifacts') {
            steps {
                archiveArtifacts artifacts: 'coverage.xml, report.xml, coverage_html/**', allowEmptyArchive: true
            }
        }
        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'report.xml'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check logs for errors.'
        }
    }
}