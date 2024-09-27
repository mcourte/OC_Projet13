3. Deployment
=============

1. Prerequisites
----------------

    In order to perform the deployment and continuous integration of the app, the following accounts are required:

    GitHub account

    CircleCI account (linked to GitHub account)

    Docker account

    Render account

    Sentry account

2. Summary
----------

    The deployment of the app is automated by the CircleCI pipeline. When updates are pushed to the GitHub repository, the pipeline triggers the test suite and code linting for all project branches. If updates are made on the master branch, and if and only if the tests and linting pass, the workflow:

    Builds a Docker image and pushes it to DockerHub

    If and only if the previous step passes, deploys the app on Render

3. Configuration CircleCI
-------------------------

    After cloning the project, setting up the local virtual environment (see Local development) and creating the required accounts, set up a new project on CircleCI via "Set Up Project".

    Select the master branch as a source for the .circleci/config.yml file

    To run the CircleCI pipeline properly, set up the following environment variables (Project Settings > Environment Variables):

    - **ALLOWED_HOSTS** : enter allowed host 

    - **DEBUG** : select True or False

    - **DOCKERHUB_PASSWORD** : Docker account password

    - **DOCKERHUB_USERNAME** : Docker account username

    - **HOOK_RENDER** : api render for deploy

    - **SECRET_KEY** : Django secret key

    - **SENTRY_DSN** : Sentry project URL

4. Configuration Render
-----------------------

    On Render, now create your Web Service

    Then define environment variables on the Render Web Service :
    
    - **ALLOWED_HOSTS** : enter allowed host 

    - **DEBUG** : select True or False

    - **DOCKERHUB_PASSWORD** : Docker account password

    - **DOCKERHUB_USERNAME** : Docker account username

    - **SECRET_KEY** : Django secret key

    - **SENTRY_DSN** : Sentry project URL
        
    
   