import os
import boto3

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

s3 = session.resource('s3')
s3_client = session.client('s3')

filenames = [my_bucket_object.key for my_bucket_object in s3.Bucket('bageld-inputs').objects.all()]

# get all videos with dates
# read database of historical videos that have actually been played
# get all videos without dates
# keep top/bot tag in video so that that information can get written to the database
# optimize based on distance metrics


# player_name = videoFile.split(';')[1].replace('_',' ')
# tour = videoFile.split(';')[2]