import boto3


def terminate_instance(instance_id):
    ec2 = boto3.client('ec2')
    response = ec2.terminate_instances(InstanceIds=[instance_id, ])
    print(response)


terminate_instance('i-0e2ab181dc28001ba')
