pipeline {
  agent any
  stages {
    stage('pip install numpy') {
      steps {
        bat 'python -m pip install -r  requirements.txt'
      }
    }
  }
}
