import boto3

ec2 = boto3.resource('ec2')

response = ec2.create_instances(
    ImageId='ami-0a261c0e5f51090b1',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='mykey'
)
print(response)

