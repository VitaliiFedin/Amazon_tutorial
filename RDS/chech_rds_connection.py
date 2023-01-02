import psycopg2

try:
    connection = psycopg2.connect(
        dbname='postgres', user='postgres', password='fed123321',
        host='database-1.c5y0yxb0gkoy.eu-central-1.rds.amazonaws.com'
    )
    print('Connected successfully')

except psycopg2.Error as error:
    print(f'Error occurred {error}')




