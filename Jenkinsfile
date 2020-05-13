pipeline {
   agent any

   stages {
      stage('Build') {
          steps {
              sh 'zip main.zip main'
          }
      }
      
      stage('Deliver') {
          steps {
                 sh '/usr/local/bin/aws lambda update-function-code --function-name goHello --zip-file fileb://main.zip'
          }
      }
      
      stage('Integration test') {
          steps {
                 sh 'docker run -t postman/newman:latest run "https://www.getpostman.com/collections/e8397d94506a6c6901bc"'
          }
      }
   }
}
