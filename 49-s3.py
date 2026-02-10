import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'boto3-test-97901'
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print("Bucket created") 
except ClientError as e:
    error_code = e.response['Error']['Code']

    if error_code in ['BucketAlreadyOwnedByYou']:
        print("Bucket already exists and is owned by you. Skipping.")
    else:
        raise
print("Bucket name:", bucket_name)  

import boto3

s3 = boto3.client('s3')

bucket_name = 'boto3-test-97901'
local_file_path = 'data/advertising.csv'
s3_key = 'uploads/advertising.csv'
s3.upload_file(local_file_path, bucket_name, s3_key)
print("Upload completed")

response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response.get('Contents', []):
    print(obj['Key'])