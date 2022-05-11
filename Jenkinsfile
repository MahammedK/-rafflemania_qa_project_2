pipeline{
        agent any
        stages{
            stage('Testing Services'){
                steps{
                    sh "bash tests.sh"
                }
            }

            stage('Building and pushing images'){
                steps {
                    sh "ln -s rafflemania_qa_project_2/docker-compose.yaml build"
                }
            }
        }
}