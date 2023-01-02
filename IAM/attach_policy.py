import boto3


def attach_policy(username, policy):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy,
    )
    print(response)

attach_policy('python', 'arn:aws:iam::295459712271:policy/ReadOnlyPolicy')
