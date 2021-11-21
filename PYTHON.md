# python test

# Table of contents

<!-- toc -->

- [initial python script](#initial-python-script)
- [create empty virtualenv](#create-empty-virtualenv)
- [MySQL](#mysql)
  * [Fix import](#fix-import)
  * [Fix error "boto3 client NoRegionError: You must specify a region"](#fix-error-boto3-client-noregionerror-you-must-specify-a-region)
  * [Fix error "botocore.exceptions.NoCredentialsError: Unable to locate credentials"](#fix-error-botocoreexceptionsnocredentialserror-unable-to-locate-credentials)
  * [DB MySQL privileges revoked](#db-mysql-privileges-revoked)
  * [final python script for mySQL](#final-python-script-for-mysql)
- [PostgreSQL](#postgresql)
  * [Add import](#add-import)
  * [final python script PostgreSQL](#final-python-script-postgresql)
- [Remarks](#remarks)

<!-- tocstop -->

## initial python script

```
python3 ./postgreSQL-intial.py
```

```python3
python -m postgreSQL-intial
# ModuleNotFoundError: No module named 'pymysql
```

## create empty virtualenv

```shell
virtualenv /opt/ansible/env39 -p python3.9
. /opt/ansible/env39/bin/activate
```

## MySQL
### Fix import

You have to install python package (in your virtualenv) before importing them

```shell
pip3 install pymysql
#or
pip3.9 install -r requirements.txt
```

### Fix error "boto3 client NoRegionError: You must specify a region"

Google gave me :

[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
[guide-configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration)

Missing config

```python3
  import boto3
  from botocore.config import Config

  my_config = Config(
      region_name = 'us-east-1',
      signature_version = 'v4',
      retries = {
          'max_attempts': 10,
          'mode': 'standard'
      }
  )

  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
  ssm_client = boto3.client('ssm', config=my_config)
  # or simpler
  ssm_client = boto3.client('ssm', region_name="us-east-1")
```

### Fix error "botocore.exceptions.NoCredentialsError: Unable to locate credentials"

TODO

Assuming the should be a json at http://project-env.cluster-qmcy3ndkwlkd.eu-west-1.rds.amazonaws.com/project-env/service_name
with a service name for get_service_name

Moreover there might be an issue project-env.cluster-qmcy3ndkwlkd.eu-west-1.rds.amazonaws.com is refering to eu-west-1 but there is region_name="us-east-1" in python file


I cannot ping both hosts :
 * project-env.cluster-qmcy3ndkwlkd.us-east-1.rds.amazonaws.com
 * project-env.cluster-qmcy3ndkwlkd.eu-west-1.rds.amazonaws.com

So it my be the PetClinic service mysql database that I should have created previously AKS.
But even thougt mysql should no be availble from external world.


### DB MySQL privileges revoked

[how-to-create-mysql-user-accounts-and-grant-privileges](https://linuxize.com/post/how-to-create-mysql-user-accounts-and-grant-privileges/)

```python3
cur.execute('GRANT ALL PRIVILEGES ON "{}".* TO "{}";'.format(service, DB_USER))
GRANT SUPER ON *.* TO nabla@'localhost' IDENTIFIED BY 'nabla';
```

### final python script for mySQL

```
python3 ./mySQL.py
```

## PostgreSQL

### Add import

You have to install python [postgresql](https://pypi.org/project/py-postgresql/) package (in your virtualenv) before importing them

pip3 install py-postgresql has less star

```shell
pip3 install psycopg2==2.9.2
#No module named 'ConfigParser'
pip install configparser
# https://www.journaldunet.fr/web-tech/developpement/1497411-comment-corriger-l-erreur-error-pg-config-executable-not-found-en-python/
sudo apt install libpq-dev
sudo apt-get install python3.9-dev
pip3 install psycopg2==2.9.2
```

```shell
pip3 install psycopg2-binary==2.9.2
#or
pip3.9 install -r requirements.txt
```

### final python script PostgreSQL

I found a python driver which looks very similar to mysql https://py-postgresql.readthedocs.io/en/latest/driver.html#establishing-a-connection

```
python3 ./postgreSQL.py
```

```python3
python -m postgreSQL
```

## Remarks

- There is for sure refactoring to be done to manage both database.
- mysqlpass is not encrypted

This [SSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html) service seems to be an API to get inventory on AWS.
I would expect a DevOps not to re invent the wheel and get direct access to this API directly.
There is CMDB tools for inventory [servicenow](https://www.servicenow.fr/products/servicenow-platform/configuration-management-database.html), Ansible get a [module](https://docs.ansible.com/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html) to access AWS and have basic [cmdb(https://ansible-cmdb.readthedocs.io/en/latest/usage/)].

I do not know terraform but I would expect (even more that Ansible), to be able to retrieve all AWS ressources directly and securely...
