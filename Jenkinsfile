pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }


        stage('Install Dependencies') {
            steps {
                bat """
                    
                    pip install -r requirements.txt
        
                """
            }
        }

        stage('Build'){
         bat ''' python app.py'''
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

