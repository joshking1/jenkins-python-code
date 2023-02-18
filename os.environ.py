import os

# Prompt the user to enter the values for the environment variables
jenkins_server_url = input("Enter the Jenkins server URL: ")
jenkins_server_username = input("Enter the Jenkins server username: ")
jenkins_server_password = input("Enter the Jenkins server password: ")
job_name = input("Enter the Jenkins job name: ")
sonarqube_server_url = input("Enter the SonarQube server URL: ")
sonarqube_server_token = input("Enter the SonarQube server token: ")
github_url = input("Enter the GitHub URL (optional, press Enter to use default): ") or 'https://github.com/joshking1/spring-boot-mongo-docker.git'

# Set the environment variables
os.environ['JENKINS_SERVER_URL'] = jenkins_server_url
os.environ['JENKINS_SERVER_USERNAME'] = jenkins_server_username
os.environ['JENKINS_SERVER_PASSWORD'] = jenkins_server_password
os.environ['JOB_NAME'] = job_name
os.environ['SONARQUBE_SERVER_URL'] = sonarqube_server_url
os.environ['SONARQUBE_SERVER_TOKEN'] = sonarqube_server_token
os.environ['GITHUB_URL'] = github_url

# Print a confirmation message
print("Environment variables set successfully.")
