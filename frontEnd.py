from flask import Flask, render_template, request
app = Flask(__name__)
from CityDataScraper import *
from sorts import  *

@app.route('/')
def start():
   return render_template('enter_zip.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      result = result.to_dict()

      zip = result['Zipcode']
      radius = result['Radius']
      get_zipcodes(zip, radius)
      get_data_from_zipcodes()

      connection = psycopg2.connect(user="postgres",
                                    password="1985",
                                    host="localhost",
                                    port="5432",
                                    database="zipcode_data")
      cur = connection.cursor()
      cur.execute("SELECT * FROM zip_data")
      data = cur.fetchall()
      return render_template('result.html', data=data)


if __name__ == '__main__':
   app.run(debug = True)

#TODO Clear table after use