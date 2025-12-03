import json, boto3
client = boto3.client('sts')
response = client.get_caller_identity()
print(type(response))
print(json.dumps(response, indent=4))

s3 = boto3.client('s3')
print(s3.list_buckets())
