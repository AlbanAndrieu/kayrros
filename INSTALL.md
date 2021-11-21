# install

# Table of contents

<!-- toc -->

- [basic](#basic)
- [virtualenv](#virtualenv)
- [AWS](#aws)
  * [awscli](#awscli)
  * [configure](#configure)
- [docker](#docker)

<!-- tocstop -->

```
git submodule add --force https://github.com/AlbanAndrieu/spring-petclinic.git

git pull && git submodule init && git submodule update && git submodule status
#git remote add upstream https://github.com/spring-projects/spring-petclinic.git
```

# basic

```shell
sudo apt-get install python3.9-dev
sudo apt install libpq-dev
sudo apt install terraform
 terraform --version
```

# virtualenv

```shell
virtualenv /opt/ansible/env39 -p python3.9
. /opt/ansible/env39/bin/activate
```

# AWS

See https://linuxhint.com/install_aws_cli_ubuntu/

## awscli

```shell
sudo apt-get install awscli
aws --version
pip3 install awscli --upgrade
```

## configure

```shell
aws configure
# eu-central-1
ls -lrt ~/.aws/
python -m awscli configure
```

```shell
aws help
python3 -m awscli help
```

# docker

Remove Work dns.
Changing the name server to 8.8.8.8 in the /etc/resolv.conf file

```shell
/etc/resolv.conf
```

sudo docker systemctl restart docker

```shell
docker pull nabla/ansible-jenkins-slave-docker:latest
```

```shell
cd spring-petclinic
sudo service docker restart
docker build -t petclinic-native .
docker run -d -p 8082:8080 petclinic-native

docker tag petclinic-native:latest nabla/petclinic-native
docker push nabla/petclinic-native:latest

docker save nabla/petclinic-native:latest | gzip > petclinic-native_latest.tar.gz

```




See https://hub.docker.com/repository/docker/nabla/petclinic-native

```shell
cd learn-terraform-docker-container/
terraform init
terraform apply
terraform destroy
```
