import psycopg2


def  order_by_bachelors():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    mycursor = connection.cursor()
    sql = "SELECT * FROM zip_data ORDER BY bachelor DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def  order_by_popuations():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    mycursor = connection.cursor()
    sql = "SELECT * FROM zip_data ORDER BY population DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def  order_by_median_value():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    mycursor = connection.cursor()
    sql = "SELECT * FROM zip_data ORDER BY median_value DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def  order_by_population_density():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    mycursor = connection.cursor()
    sql = "SELECT * FROM zip_data ORDER BY population_density DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def  order_by_median_age():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    mycursor = connection.cursor()
    sql = "SELECT * FROM zip_data ORDER BY median_age DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def  order_by_col():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    mycursor = connection.cursor()
    sql = "SELECT * FROM zip_data ORDER BY col DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def delete_all_rows():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM zip_data;')
    connection.commit()
    connection.close()

delete_all_rows()