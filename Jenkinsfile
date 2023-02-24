pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage("Login to Docker hub"){
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
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
                bat 'git pull'
                bat "git merge ${env.GIT_BRANCH}"
                bat 'git push origin dev'
            }
        }
        stage('testing') {
            steps {
                script {
                    def inputName
                    def userInput = input(
                            id: 'userInput', message: 'Enter the version of the release:?',
                            parameters: [
                                string(defaultValue: 'None',
                                        description: 'Name of the version',
                                        name: 'Version')
                            ])

                    inputName = userInput.Version?:''
                    bat 'git checkout dev'
                    bat "git checkout -b release/version_${inputName}"
                    bat 'git merge dev'
                    bat "git push origin release/version_${inputName}"
                    bat 'git checkout main'
                    bat 'git pull'
                    bat "git merge release/version_${inputName}"
                    bat 'git push origin main'
                }
            }
        }
        stage('Pushing to Dockerhub') {
            steps {
                dir('backend_rating') {
                    bat 'docker build -t shinbi/prediction_api:latest .'
                    bat 'docker run -p 5000:5000 shinbi/prediction_api:latest'
                    bat 'docker push shinbi/prediction_api:latest' 
                }
                bat 'docker-compose up'
            }
        }
    }
    post {
        always {
            bat 'docker logout'
        }
    }
}
