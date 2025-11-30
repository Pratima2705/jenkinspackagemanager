pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                bat """
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python --version
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Build Package (wheel + sdist)') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    python -m build
                """
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
        }
    }

    post {
        always {
            bat """
                echo Build completed
            """
        }
    }
}
