import boto3
import uuid
import requests

from config import cfg


def get_file_s3(file):
    """
    :param file: file to read from s3
    :return: local path to the file
    """

    s3_client = boto3.client('s3', aws_access_key_id=cfg['S3']['PUBLIC_KEY'], aws_secret_access_key=cfg['S3']['SECRET_KEY'])
    result = s3_client.get_object(Bucket=cfg['S3']['BUCKET'], Key='lake.mp4')
    bytes = result['Body'].read()

    # Write into /tmp/ using a hash to prevent collision and maintaining the file extension
    salt = uuid.uuid4()
    path = "/tmp/{salt}{file}".format(salt=salt, file=file)
    with open(path, 'wb') as f:
        f.write(bytes)
        f.close()
    return path


def put_file_to_s3(file):
    PREFIX = 'uploads'
    name = uuid.uuid4()
    s3_client = boto3.client('s3', aws_access_key_id=cfg['S3']['PUBLIC_KEY'], aws_secret_access_key=cfg['S3']['SECRET_KEY'])
    key='{prefix}/{name}.mp4'.format(prefix=PREFIX, name=name)
    with open(file, 'rb') as bytes:
        print('putting file %s' % file)
        print('putting key %s' % key)
        s3_client.put_object(
            Bucket=cfg['S3']['BUCKET'],
            Key=key,
            ACL='public-read',
            Body=bytes
        )

    s3_url = 'https://s3.amazonaws.com/{bucket}/{key}'.format(bucket=cfg['S3']['BUCKET'], key=key)
    print('writing file to s3 {url}'.format(url=s3_url))
    return s3_url


def get_file_public_url(file):
    # Write into /tmp/ using a hash to prevent collision and maintaining the file extension
    salt = uuid.uuid4()
    tmp_file_path = "/tmp/{salt}.{extension}".format(salt=salt, extension='mp4')
    with open(tmp_file_path, 'wb') as f:
        response = requests.get(file)
        f.write(response.content)
        f.close()
    print('writing file ({url}) to {output}'.format(url=file, output=tmp_file_path))
    return tmp_file_path


#get_file_public_url('http://donato.s3.amazonaws.com/prom.mp4')
#put_file_s3('/tmp/4cf03bf1-de24-45ea-a5da-e688d5585efd.mp4', 'abc')
