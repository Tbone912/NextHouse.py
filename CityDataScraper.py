#The aim of this program is:  You type in the zipcode and radius and it will return the highest rates around.
import requests
from bs4 import BeautifulSoup
import re
from sorts import *

# zipcodeapi.com   3ZMYmUDmqB146es3Se3YoAQvV7aobJBDOlE1uCZZ3W0Ldprv5R35R3hYfJxjSbZr

def get_zipcodes(center_zipcode,radius):
    zips = requests.get('https://www.zipcodeapi.com/rest/3ZMYmUDmqB146es3Se3YoAQvV7aobJBDOlE1uCZZ3W0Ldprv5R35R3hYfJxjSbZr/radius.json/' + str(center_zipcode) + '/' + str(radius) + '/mile')
    #zips = requests.get('https://www.zipcodeapi.com/rest/3lkb3C3HA1EOLkWz16J1v1MkbK8nB328fLFp3O431v8OD8wfW57T9hYsDmDV93l5/radius.json/' + str(center_zipcode) + '/' + str(radius) + '/mile')
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")

    for i in range(0,len(zips.json()["zip_codes"])):
        cursor = connection.cursor()
        all_zips = zips.json()["zip_codes"][i]['zip_code']
        cursor.execute('INSERT INTO zip_data VALUES ('+all_zips+');')
        connection.commit()
    connection.close()

def get_data_from_zipcodes():
    connection = psycopg2.connect(user="postgres",
                                  password="1985",
                                  host="localhost",
                                  port="5432",
                                  database="zipcode_data")
    cursor = connection.cursor()
    cursor.execute("SELECT zipcode FROM zip_data")
    numrows = cursor.rowcount
    all_zips = cursor.fetchall()

    for zips in all_zips:
        first = str(zips[0])
        r = requests.get('http://www.city-data.com/zips/' + str(zips[0]) + '.html')
        if r.status_code == 200:
            # Extract the html from the request
            data = (r.text)
            # Parse html with Beautifulsoup
            soup = BeautifulSoup(data, 'html.parser')

            # find the percent of Bachelor's degrees in the zipcode
            try:
                pre_bachelor = soup.find("b", text=re.compile("Bachelor's degree or higher"))
                bachelor_rate = pre_bachelor.next_sibling
                bachelor_rate = bachelor_rate.replace('%', '')
                cursor.execute('UPDATE zip_data SET bachelor = ' + bachelor_rate + ' WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()
            except AttributeError:
                cursor.execute('UPDATE zip_data SET bachelor = null WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()

            #Insert population into table
            try:
                pre_population = soup.find("b", text=re.compile("Estimated zip code population in 2016"))
                population = pre_population.next_sibling
                population = population.replace(',', '')
                cursor.execute('UPDATE zip_data SET population = ' + population + ' WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()
            except AttributeError:
                cursor.execute('UPDATE zip_data SET population = null WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()

            #Insert population_density into table
            try:
                pre_population_density = soup.find("b", text=re.compile("Population density"))
                population_density = pre_population_density.next_sibling
                population_density = population_density.replace(',', '')
                cursor.execute('UPDATE zip_data SET population_density = ' + population_density + ' WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()
            except AttributeError:
                cursor.execute('UPDATE zip_data SET population_density = null WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()

            # Insert median house value into table
            try:
                pre_median_value = soup.find("b", text=re.compile("Estimated median house or condo value in 2016"))
                median_value = pre_median_value.next_sibling
                median_value = median_value.replace(',', '')
                median_value = median_value.replace('$', '')
                cursor.execute('UPDATE zip_data SET median_value = ' + median_value + ' WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()
            except AttributeError:
                cursor.execute('UPDATE zip_data SET median_value = null WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()

            # Insert median age into table
            try:
                pre_median_age = soup.find("b", text=re.compile("Median resident age"))
                median_age = pre_median_age.next_sibling.text
                sAge = slice(14, 16)
                median_age = (median_age[sAge])
                cursor.execute('UPDATE zip_data SET median_age = ' + median_age + ' WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()
            except AttributeError:
                cursor.execute('UPDATE zip_data SET median_age = null WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()


            # Insert Cost of Living into table
            try:
                pre_CoL = soup.find("b", text=re.compile("cost of living"))
                CoL = pre_CoL.next_sibling
                cursor.execute('UPDATE zip_data SET col = ' + CoL + ' WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()
            except AttributeError:
                cursor.execute('UPDATE zip_data SET col = null WHERE zipcode = ' + str(zips[0]) + ';')
                connection.commit()

        #delete zip codes that don't exist
        else:
            cursor.execute('DELETE FROM zip_data Where zipcode = ' + str(zips[0]) + ';')
            connection.commit()

    connection.close()


#get_zipcodes(30032,3)
#get_data_from_zipcodes()
#order_by_population_density()