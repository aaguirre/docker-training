FROM jenkins

USER root

RUN apt-get update \
    && apt-get install -y software-properties-common \
    && apt-add-repository -y ppa:ansible/ansible \
    && apt-get install -y ansible    

RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

RUN chmod +x /usr/local/bin/docker-compose

COPY plugins.txt /var/jenkins_home/plugins.txt

COPY jenkins_home/users/aaguirre /var/jenkins_home/users/aaguirre

COPY jenkins_home/jobs /var/jenkins_home/jobs

RUN /usr/local/bin/install-plugins.sh < /var/jenkins_home/plugins.txt    
