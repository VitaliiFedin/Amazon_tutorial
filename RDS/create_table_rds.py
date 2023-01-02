import psycopg2

try:
    connection = psycopg2.connect(
        dbname='postgres', user='postgres', password='fed123321',
        host='database-1.c5y0yxb0gkoy.eu-central-1.rds.amazonaws.com'
    )
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE Newtable(id SERIAL PRIMARY KEY,name VARCHAR(255),surname VARCHAR(255))')
    cursor.close()
    connection.commit()


except psycopg2.Error as error:
    print(f'An error occurred {error}')

