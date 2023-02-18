import os
import jenkins
import time

# Load environment variables
jenkins_server_url = os.environ.get('JENKINS_SERVER_URL')
jenkins_server_username = os.environ.get('JENKINS_SERVER_USERNAME')
jenkins_server_password = os.environ.get('JENKINS_SERVER_PASSWORD')
job_name = os.environ.get('JOB_NAME')
sonarqube_server_url = os.environ.get('SONARQUBE_SERVER_URL')
sonarqube_server_token = os.environ.get('SONARQUBE_SERVER_TOKEN')
github_url = os.environ.get('GITHUB_URL', 'https://github.com/joshking1/spring-boot-mongo-docker.git')

# Create a Jenkins server object
server = jenkins.Jenkins(jenkins_server_url, username=jenkins_server_username, password=jenkins_server_password)

# Clone the Git repository
print(f'Cloning the {job_name} repository...')
server.build_job(job_name, {'GIT_ACTION': 'clone', 'GIT_URL': github_url})

# Wait for the build to complete
while server.get_job_info(job_name)['lastBuild']['building']:
    time.sleep(10)

# Build the project
print(f'Building {job_name}...')
server.build_job(job_name)

# Wait for the build to complete
while server.get_job_info(job_name)['lastBuild']['building']:
    time.sleep(10)

# Run SonarQube analysis
print(f'Running SonarQube analysis for {job_name}...')
server.build_job(job_name, {'SONAR_HOST_URL': sonarqube_server_url, 'SONAR_AUTH_TOKEN': sonarqube_server_token})

# Wait for the build to complete
while server.get_job_info(job_name)['lastBuild']['building']:
    time.sleep(10)

# Get the build status
build_status = server.get_job_info(job_name)['lastBuild']['result']

# Print the build status
print(f'{job_name} build {build_status}')

# In this modified script, we have used the os.environ.get() method to load the values of our environment variables into variables with lowercase names. We've also added a default value for the GITHUB_URL variable, 
# In case it is not provided in the environment.To use this script, you would need to set the values of these environment variables before running the script. For example, you could set them in a shell script or in your terminal 
# session before running the Python script.