pipeline {pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
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
                    pip install setuptools wheel build
                """
            }
        }

        stage('Build Package (Wheel & Sdist)') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    python -m build
                """
            }
        }

        stage('Archive Build Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
        }

    }

    post {
        always {
            bat """
                echo Cleaning workspace...
            """
            cleanWs()
        }
    }
}

