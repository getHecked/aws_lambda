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
                 sh 'aws lambda update-function-code --function-name snoop --zip-file fileb://lambda_function.zip'
          }
      }
      
      stage('Integration test') {
          steps {
                 sh 'docker run -t postman/newman:latest run "https://www.getpostman.com/collections/e8397d94506a6c6901bc"'
          }
      }
   }
}
