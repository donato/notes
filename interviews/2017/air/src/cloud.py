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


def put_file_s3(file, name):
    PREFIX = 'uploads'
    s3_client = boto3.client('s3', aws_access_key_id=cfg['S3']['PUBLIC_KEY'], aws_secret_access_key=cfg['S3']['SECRET_KEY'])
    with open(file, 'rb') as bytes:
        key='{prefix}/{name}.mp4'.format(prefix=PREFIX, name=name)
        print('putting file %s' % file)
        print('putting key %s' % key)
        s3_client.put_object(
            Bucket=cfg['S3']['BUCKET'],
            Key=key,
            Body=bytes
        )


def get_file_public_url(file):
    # Write into /tmp/ using a hash to prevent collision and maintaining the file extension
    salt = uuid.uuid4()
    tmp_file_path = "/tmp/{salt}.{extension}".format(salt=salt, extension='mp4')
    with open(tmp_file_path, 'wb') as f:
        response = requests.get(file)
        f.write(response.content)
        f.close()
    print(tmp_file_path)


#get_file_public_url('http://donato.s3.amazonaws.com/prom.mp4')
#put_file_s3('/tmp/4cf03bf1-de24-45ea-a5da-e688d5585efd.mp4', 'abc')
