import psycopg2

try:
    connection = psycopg2.connect(
        dbname='postgres', user='postgres', password='fed123321',
        host='database-1.c5y0yxb0gkoy.eu-central-1.rds.amazonaws.com'
    )
    cursor = connection.cursor()
    postgres_insert_query = ''' INSERT INTO newtable (name,surname) VALUES (%s,%s)'''
    record_to_insert = ('Vetal', 'Fedin')
    cursor.execute(postgres_insert_query, record_to_insert)
    cursor.close()
    connection.commit()


except psycopg2.Error as error:
    print(f'An error occurred {error}')
