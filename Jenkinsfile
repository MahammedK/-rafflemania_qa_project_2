pipeline {
    agent any
    stages {
        stage('Testing Services') {
            steps {
                sh "bash tests.sh"
            }
        }
        stage('Docker-compose') {
            steps {
                sh "docker-compose build --parallel"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~ansible_key docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~ansible_key nginx.conf swarm-manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }
}