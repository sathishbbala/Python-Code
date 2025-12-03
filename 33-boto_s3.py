import boto3

REGION = "ap-south-1"
BUCKET_NAME = "sathish-boto3-demo"

s3 = boto3.client("s3", region_name=REGION)
print(s3.list_buckets())

#s3.create_bucket(Bucket = BUCKET_NAME)

print("Bucket created successfully")
