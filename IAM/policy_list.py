import boto3


def list_policy():
    iam = boto3.client('iam')

    policies = iam.get_paginator('list_policies')

    for response in policies.paginate(Scope='AWS'):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            policy_arn = policy['Arn']
        print(f'Policy name: {policy_name}, Arn:{policy_arn}')


list_policy()
