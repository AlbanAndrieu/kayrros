#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The following code connects to AWS using boto3 to retrieve a parameter from SSM.
That parameter is then used in the creation of a PostgreSQL DB as the name of the DB.
"""
import json

import psycopg2
# import postgresql

SSM_PATH = '/project-env'
DB_USER = 'project'
DB_PASS = '123456'


def get_ssm_connection():

    import boto3
    from botocore.config import Config

    my_config = Config(
        region_name='us-east-1',
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard',
        },
    )

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
    ssm_client = boto3.client('ssm', config=my_config)
    # ssm_client = boto3.client('ssm', region_name='us-east-1')
    return ssm_client


def get_service_name(path):
    ssm_client = get_ssm_connection()
    service_name = json.loads(
        ssm_client.get_parameter(
            Name=path + '/service_name',
        )['Parameter']['Value'],
    )
    return service_name


def get_db_connection():
    """
    Gets a connection to PostgreSQL DB
    """
    # Some PostgreSQL details for this Python test
    port = 5432
    dbname = None
    user = 'apostgresqluser'
    password = 'postgresqlpass'
    host = 'project-env.cluster-qmcy3ndkwlkd.eu-west-1.rds.amazonaws.com'

    # Try to obtain a connection to the db
    try:
        # https://py-postgresql.readthedocs.io/en/latest/driver.html#establishing-a-connection
        # conn = postgresql.open(host=host, user=user, password=password, port=port, database=dbname, connect_timeout=5)
        conn = psycopg2.open(
            host=host, user=user, password=password,
            port=port, database=dbname, connect_timeout=5,
        )
        return conn
    # except (Exception, postgresql.exceptions.ConnectionError) as error:
    except (Exception) as error:
        print(error)


def create_db(conn, service):
    """
    Creates the database and users, and modifies the user password if it's been
    changed
    """
    # TODO check that lib is working with ContextManager to close cursor
    with conn.cursor() as cur:
        # See https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
        # cur.execute("DROP DATABASE IF EXISTS  `{}`;".format(service))
        cur.execute('CREATE DATABASE `{}`;'.format(service))
        cur.execute(
            'CREATE USER "{}"  WITH ENCRYPTED PASSWORD "{}";'.format(
                DB_USER, DB_PASS,
            ),
        )
        # cur.execute('REVOKE ALL PRIVILEGES, GRANT OPTION FROM "{}" '.format(DB_USER))
        cur.execute(
            'GRANT ALL PRIVILEGES ON DATABASE "{}" TO "{}";'.format(
                service, DB_USER,
            ),
        )
        conn.commit()

    conn.close()
    return


def setup_service_db(service):
    conn = get_db_connection()
    create_db(conn, service)
    # TODO conn.close()
    return


def main():
    service = get_service_name(SSM_PATH)
    setup_service_db(service)


if __name__ == '__main__':
    main()
