pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup Python Env') {
      steps {
        sh '''
          python3 -m venv .venv || python -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip setuptools wheel
        '''
      }
    }

    stage('Install Dependencies') {
      steps {
        sh '''
          . .venv/bin/activate
          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          else
            echo "requirements.txt not found — skipping dependency install"
          fi
        '''
      }
    }

    stage('Build Package (wheel + sdist)') {
      steps {
        sh '''
          . .venv/bin/activate
          pip install --upgrade build
          # build produces files under dist/
          python -m build --sdist --wheel
        '''
      }
    }

    stage('Archive Artifacts') {
      steps {
        archiveArtifacts artifacts: 'dist/.whl, dist/.tar.gz', allowEmptyArchive: true
      }
    }
  }

  post {
    always {
      echo "Pipeline finished: ${currentBuild.currentResult}"
      // optional cleanup
      sh 'rm -rf .venv || true'
    }
  }
}
