import boto3
import logging
from botocore.exceptions import ClientError

def put_object(dest_bucket_name, dest_object_name, src_data):
    if isinstance(src_data, bytes):
        object_data = src_data
    elif isinstance(src_data, str):
        try:
            object_data = open(src_data, 'rb')
        # possible FileNotFoundError/IOError exception
        except Exception as e:
            logging.error(e)
            return False
    #else:
    #    logging.error('Type of ' + str(type(src_data)) + ' for the argument \'src_data\' is not supported.')
    #    return False
    # Put the object
    # s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=dest_bucket_name, Key=dest_object_name, Body=object_data)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        if isinstance(src_data, str):
            object_data.close()
    return True

# Let's use Amazon S3
s3 = boto3.resource('s3')

bucketName = 'video-recognizer-bucket' 
movieName = 'movies/titanic.mp4'
keyName = "TitanicScene1"
movie = open(movieName, 'rb')

# Upload a new file
# data = open('test.jpg', 'rb')
s3.Bucket(bucketName).put_object(Key=keyName, Body=movie)
