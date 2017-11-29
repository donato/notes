import boto3
import uuid
import requests

from config import cfg


def put_file_to_s3(file):
    PREFIX = 'uploads'
    name = uuid.uuid4()
    s3_client = boto3.client('s3', aws_access_key_id=cfg['S3']['PUBLIC_KEY'], aws_secret_access_key=cfg['S3']['SECRET_KEY'])
    key='{prefix}/{name}.mp4'.format(prefix=PREFIX, name=name)
    with open(file, 'rb') as bytes:
        s3_client.put_object(
            Bucket=cfg['S3']['BUCKET'],
            Key=key,
            ACL='public-read',
            Body=bytes
        )

    s3_url = 'https://s3.amazonaws.com/{bucket}/{key}'.format(bucket=cfg['S3']['BUCKET'], key=key)
    return s3_url


def get_file_public_url(file):
    # Write into /tmp/ using a hash to prevent collision and maintaining the file extension
    salt = uuid.uuid4()
    tmp_file_path = "/tmp/{salt}.{extension}".format(salt=salt, extension='mp4')
    with open(tmp_file_path, 'wb') as f:
        response = requests.get(file)
        f.write(response.content)
        f.close()
    return tmp_file_path

