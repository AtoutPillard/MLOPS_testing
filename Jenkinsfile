pipeline {
    agent any
    stages {
        stage("Login to Docker hub"){
            steps {
                withCredentials([usernamePassword(credentialsId: 'shinbidocker', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat "docker login -u $USERNAME -p $PASSWORD"
                }
                
            }
        }
        stage('Building and unit testing'){
            steps {
                bat "git checkout ${env.GIT_BRANCH}"
                dir('backend_rating') {
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Push to Develop') {
            steps {
                bat 'git checkout dev'
                bat 'git pull dev'
                bat "git merge ${env.GIT_BRANCH}"
                bat 'git commit -m "Merge feature branch into dev"'
                bat 'git push origin dev'
                bat "git branch -d ${env.GIT_BRANCH}"
            }
        }
        stage('User Acceptance') {
            input {
                message "Proceed to push to main"
                ok "Yes"
            }
            steps {
                bat 'git checkout main'
                bat 'git pull main'
                bat 'git merge dev'
                bat 'git commit -m "Merge dev branch into main"'
                bat 'git push origin main'
            }
        }
        stage('Pushing to Dockerhub') {
            steps {
                bat 'git checkout main'
                dir('backend_rating') {
                    bat 'docker build -t shinbi/prediction_api:latest .'
                    bat 'docker run -p 5000:5000 shinbi/prediction_api:latest'
                    bat 'docker push shinbi/prediction_api:latest' 
                }
                bat 'docker-compose up'
            }
        }
    }
}