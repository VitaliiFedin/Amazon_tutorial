import boto3

rds = boto3.client('rds')

response = rds.create_db_instance(
    DBName='MyDB2',
    DBInstanceIdentifier='MyDB2',
    AllocatedStorage=20,
    DBInstanceClass='db.t3.micro',
    Engine='mysql',
    MasterUsername='vetal',
    MasterUserPassword='fed123321',
    Port=3306,
    PubliclyAccessible=True,
    StorageType='gp2'
)
print(response)
