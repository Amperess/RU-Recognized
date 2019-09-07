import boto3
import logging
from botocore.exceptions import ClientError

def put_object(bucket_name, key_name, data):
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)

# Let's use Amazon S3
s3 = boto3.resource('s3')

bucketName = 'video-recognizer-bucket' 
movieName = 'movies/titanic.mp4'
keyName = "TitanicScene1"
movie = open(movieName, 'rb')

# Upload a new file
put_object(Key=keyName, Body=movie)
