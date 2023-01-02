import boto3

rds = boto3.client('rds')

response = rds.delete_db_instance(
    DBInstanceIdentifier='database-1',
    SkipFinalSnapshot=True,
)
print(response)
