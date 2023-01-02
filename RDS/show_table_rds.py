import psycopg2

try:
    connection = psycopg2.connect(
        dbname='postgres', user='postgres', password='fed123321',
        host='database-1.c5y0yxb0gkoy.eu-central-1.rds.amazonaws.com'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM newtable')
    records = cursor.fetchall()

    for record in records:
        print(record)
    cursor.close()
    connection.close()



except psycopg2.Error as error:
    print(f'An error occurred {error}')
