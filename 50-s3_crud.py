# import boto library
import boto3
from botocore.exceptions import ClientError

# instantiate s3 resource
s3 = boto3.client('s3', region_name='ap-south-1')   
bucket_name = 'boto3-test-97901'

# create bucket
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

# upload file
local_file_path = 'data/data.txt'
s3_key = 'uploads/data.txt'
s3.upload_file(local_file_path, bucket_name, s3_key)
print("Upload completed")

# read and print the contents of the file from the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response.get('Contents', []):
    print(obj['Key'])

