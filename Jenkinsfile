pipeline {
   agent any

   stages {
      stage('Build') {
          steps {
              sh 'zip lambda_function.zip lambda_function.py'
          }
      }
      
      stage('Deliver') {
          steps {
		sh"/usr/local/bin/aws lambda update-function-code --function-name http-api-gateway --zip-file fileb://lambda_function.zip"
          }
      }
      
      stage('Integration test') {
          steps {
                 sh 'docker run -t postman/newman:latest run "https://www.getpostman.com/collections/02b4e209c969a5a5c815"'
          }
      }
   }
}
