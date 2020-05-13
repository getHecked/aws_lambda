pipeline {
   agent any

   stages {
      stage('Build') {
          steps {
              sh 'zip snoop.zip snoop.py'
          }
      }
      
      stage('Deliver') {
          steps {
                 sh '/usr/local/bin/aws lambda update-function-code --function-name snoop --zip-file fileb://snoop.zip'
          }
      }
      
      stage('Integration test') {
          steps {
                 sh 'docker run -t postman/newman:latest run "https://www.getpostman.com/collections/e8397d94506a6c6901bc"'
          }
      }
   }
}
