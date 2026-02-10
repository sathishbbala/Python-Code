import boto3

client = boto3.client('s3', region_name='ap-south-1')
client.create_bucket(Bucket='my-bucket-97904', CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'})    
client.upload_file('data/data.txt', 'my-bucket-97904', 'data.txt')

# s3 = boto3.resource('s3', region_name='ap-south-1')
# for bucket in s3.buckets.all():
#     print(bucket.name)


