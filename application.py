from flask import Flask,request
from boto.dynamodb2.table import Table
from flask import Flask,render_template
##from flask import Markup
import MySQLdb
import jinja2
import os
import boto

import csv
from datetime import datetime
import time
#import pandas as pd
import random
#import memcache
import sys


application = Flask(__name__)


@application.route('/back',methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main4():
    return main_main()
    '''return render_template('query.html',
                           title='MAIN',
                           user='mj')'''

@application.route('/new_customer',methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main123():
    user = {'nickname': 'Miguel'}  # fake user
    mj1=['MJ','Jain','PJ']
    return render_template('new_customer.html',
                           title='New Customer',
                           user=mj1)


@application.route('/sign', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main1():
    print "mj entered"
    my_res=[]
    name=request.form['name']
    contact=request.form['contact']

    print "fetching records from My SQL"
    print "mj updated"
    print "name= ",name
    print "contact=",contact
    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()
    cursor.execute('insert into Customer (Name,Contact_Number) values(%s,%s)',(name,contact))
    db.commit();
    ##
    my_res = [];
    for row in cursor.fetchall():
            my_res.append(dict([('loc',row[0]),
                                 ('mag',row[1]),
                                 ('id',row[2])
                                 ]))

    return render_template('results.html',
                           title='results',
                           my_res=my_res)

@application.route('/cartype', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def c_type():

    return render_template('Car_Type.html',
                           title='Car Type',
                           my_res="mj")

@application.route('/type', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_type():
    print "mj entered car type"
    my_res=[]
    operation=request.form['operation']
    print "operation ",operation

    daily_rate=int(request.form['daily_rate'])
    print "daily rate",daily_rate
    weekly_rate=int(request.form['weekly_rate'])
    print "weekly_rate",weekly_rate
    c_type=str(request.form['type'])
    print "Car type",c_type

    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()
    if operation=='new':

        cursor.execute('insert into Vehicle_Type (Type,Daily_Rate,Weekly_Rate) values(%s,%s,%s)',(c_type,daily_rate,weekly_rate))
        db.commit();

    else:
        cursor.execute("Update Vehicle_Type set Daily_Rate= %s , Weekly_Rate= %s where Type= '%s' " % (daily_rate,weekly_rate,c_type))
        db.commit();


    return render_template('type_results.html',
                           title='results',
                           my_res=my_res)


    #user = {'nickname': 'Miguel'}  # fake user

@application.route('/car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_template():

    return render_template('Car.html',
                           title='Car Type',
                           my_res="mj")

@application.route('/new_car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car():
    print "mj entered new car"
    my_res=[]
    operation=request.form['operation']
    print "operation ",operation

    car_model=request.form['model']
    print "model:",car_model

    car_year=request.form['year']
    print "Car Year:",car_year

    c_type=str(request.form['type'])
    print "Car type",c_type

    availablity=request.form['availablity']
    print "availablity ",availablity

    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()

    if operation=='new':

        cursor.execute('insert into Car_Details (Model,Year,Type,Available) values(%s,%s,%s,%s)',(car_model,car_year,c_type,availablity))
        db.commit();

    return render_template('new_car_results.html',
                           title='results',
                           my_res=my_res)


@application.route('/daily', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def daily_rent():
    print "entered daily rent"
    return render_template('Daily_Rental.html',
                           title='Car Type',
                           my_res="mj")


'''
@application.route('/chk_car_available', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_available():
    print "mj entered car available"
    my_res=[]
    my_res1=[]
    cust_id=str(request.form['cust_id'])
    print "cust_id:",cust_id

    my_res.append(cust_id)
    my_res1.append(cust_id)

    location=request.form['location']
    print "location:",location

    my_res.append(location)

    c_type=str(request.form['type'])
    print "Car type",c_type

    my_res.append(c_type)

    car_name=request.form['model']
    print "car_name:",car_name


    my_res.append(car_name)
    my_res1.append(car_name)

    num_days=int(request.form['days'])
    print "days:",num_days

    my_res.append(str(num_days))

    start_date=request.form['start_date']
    print "start_date:",start_date
    my_res.append(str(start_date))
    #return_date = pd.to_datetime(start_date) + pd.DateOffset(days=num_days)
    return_date = pd.to_datetime(start_date) + pd.DateOffset(days=num_days)
    print "Return Date:",return_date.date()
    my_res.append(str(return_date.date()))

    print "final my res: ",my_res




    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()

    #if operation=='new':


    query='select Daily_Rate from Vehicle_Type where Type ='+"'"+c_type+"'"
    print query
    #cursor.execute("SELECT name, phone_number FROM coworkers WHERE name=%s AND clue > %s LIMIT 5", (name, clue_threshold))

    cursor.execute(query)
    rate=0
    res=cursor.fetchall()

    for row in res:
        print "Row :",row[0]
        rate=row[0]
    bill=rate*num_days
    print "Final Bill Amt:",bill
    my_res1.append(str(bill))

    query1='select Rent_Id from Daily_Rental order by Rent_Id desc limit 1'
    rows_count=cursor.execute(query1)
    res1=cursor.fetchall()
    rent_id=0
    #print "Res1 :",res1[0]
    if rows_count==0:
        print "No Rent id so assigning new"
        rent_id=1
    else:
        for row in res1:
            print "Row in rent for :",row[0]
            rent_id=int(row[0])+1

    print "Rent Id= ",rent_id
    my_res1.append(str(rent_id))
    #query='select Daily_Rate from Vehicle_Type where Type ='+"'"+t+"'"
    query='select Vehicle_Id from Car_Details where Model= '+"'"+car_name+"'"+' And TYPE='"'"+c_type+"'"
    print "vehicle_id query: ",query
    cursor.execute(query)
    res1=cursor.fetchall()
    #print "res1 vehicle id: ",res1[0]
    v_id=0
    for row in res1:
            print "Vehicle id :",row[0]
            v_id=str(row[0])
    print "Vehicle id :",v_id
    print "System Date: ",datetime.today().date()
    print "Start Date:",my_res[5]
    if my_res[5]==str(datetime.today().date()):
        stat='Current'
    else:
        stat='Scheduled'
    my_res1.append(str(stat))
    my_res1.append("Confirmed")
    #yourdatetime.date() == datetime.today().date()+c_type+"'"
    query='insert into Daily_Rental (Rent_Id,Cust_Id,Vehicle_Id,Location,No_Of_Days,Start_Date,Return_Date,Amount_Due,Booking_Status) VALUES '
    print query
    query2='('+ my_res1[3] +',' + my_res1[0] +','+ v_id + ",'"+ my_res[1]+"',"+my_res[4]+",'"+my_res[5]+"','"+my_res[6]+"',"+my_res1[2]+",'"+stat+"')"
    f=query+query2
    print "final query insert: ",f
    cursor.execute(f)
    db.commit();


      #  db.commit();

    return render_template('results_daily_rental.html',
                           title='results',
                           my_res=my_res,my_res1=my_res1)

'''
@application.route('/weekly', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def daily_rent1():
    print "entered daily rent"
    return render_template('Weekly_Rental.html',
                           title='Car Type',
                           my_res="mj")

'''
@application.route('/weekly_car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_available1():
    print "mj entered car available1"
    my_res=[]
    my_res1=[]
    cust_id=str(request.form['cust_id'])
    print "cust_id:",cust_id

    my_res.append(cust_id)
    my_res1.append(cust_id)

    location=request.form['location']
    print "location:",location

    my_res.append(location)

    c_type=str(request.form['type'])
    print "Car type",c_type

    my_res.append(c_type)

    car_name=request.form['model']
    print "car_name:",car_name


    my_res.append(car_name)
    my_res1.append(car_name)

    num_weeks=int(request.form['weeks'])
    print "weeks:",num_weeks

    my_res.append(str(num_weeks))

    start_date=request.form['start_date']
    print "start_date:",start_date
    my_res.append(str(start_date))
    return_date = pd.to_datetime(start_date) + pd.DateOffset(weeks=num_weeks)
    print "Return Date:",return_date.date()
    my_res.append(str(return_date.date()))

    print "final my res: ",my_res




    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()

    #if operation=='new':


    query='select Weekly_Rate from Vehicle_Type where Type ='+"'"+c_type+"'"
    print query
    #cursor.execute("SELECT name, phone_number FROM coworkers WHERE name=%s AND clue > %s LIMIT 5", (name, clue_threshold))

    cursor.execute(query)
    rate=0
    res=cursor.fetchall()

    for row in res:
        print "Row :",row[0]
        rate=row[0]
    bill=rate*num_weeks
    print "Final Bill Amt:",bill
    my_res1.append(str(bill))

    query1='select max(Rent_Id) from Weekly_Rental order by Rent_Id desc limit 1'
    rows_count=cursor.execute(query1)
    res1=cursor.fetchall()
    rent_id=0
    #print "Res1 :",res1[0]
    if rows_count==0:
        print "No Rent id so assigning new"
        rent_id=1
    else:
        for row in res1:
            print "Row in rent for :",row[0]
            rent_id=int(row[0])+10

    print "Rent Id= ",rent_id
    my_res1.append(str(rent_id))
    #query='select Daily_Rate from Vehicle_Type where Type ='+"'"+t+"'"
    query='select Vehicle_Id from Car_Details where Model= '+"'"+car_name+"'"+' And TYPE='"'"+c_type+"'"
    print "vehicle_id query: ",query
    cursor.execute(query)
    res1=cursor.fetchall()
    #print "res1 vehicle id: ",res1[0]
    v_id=0
    for row in res1:
            print "Vehicle id :",row[0]
            v_id=str(row[0])
    print "Vehicle id :",v_id
    print "System Date: ",datetime.today().date()
    print "Start Date:",my_res[5]
    if my_res[5]==str(datetime.today().date()):
        stat='Current'
    else:
        stat='Scheduled'
    my_res1.append(str(stat))
    my_res1.append("Confirmed")
    #yourdatetime.date() == datetime.today().date()+c_type+"'"
    query='insert into Weekly_Rental (Rent_Id,Cust_Id,Vehicle_Id,Location,No_Of_Weeks,Start_Date,Return_Date,Amount_Due,Booking_Status) VALUES '
    print query
    query2='('+ my_res1[3] +',' + my_res1[0] +','+ v_id + ",'"+ my_res[1]+"',"+my_res[4]+",'"+my_res[5]+"','"+my_res[6]+"',"+my_res1[2]+",'"+stat+"')"
    f=query+query2
    print "final query insert: ",f
    cursor.execute(f)
    db.commit();


      #  db.commit();

    return render_template('results_weekly_rental.html',
                           title='results',
                           my_res=my_res,my_res1=my_res1)
'''
@application.route('/return', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def daily_rent2():
    print "entered daily rent"
    return render_template('Return_Car.html',
                           title='Car Type',
                           my_res="mj")

@application.route('/return_car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_type1():
    print "mj entered car type"
    my_res=[]

    cust_id=str(request.form['cust_id'])
    print "cust_id:",cust_id
    rent_id=str(request.form['rent_id'])
    print "rent_id:",rent_id
    my_res.append(rent_id)
    my_res.append(cust_id)
    booking_type=request.form['booking_type']
    print "booking_type ",booking_type


    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()
    if booking_type=='daily':
        query="update Daily_Rental SET Booking_Status='Completed' WHERE Rent_Id="+rent_id+' And Cust_Id='+cust_id
        print "update query daily: ",query
        cursor.execute(query)
        db.commit()
        query="select Amount_Due from Daily_Rental where Rent_Id="+rent_id+' And Cust_Id='+cust_id
        cursor.execute(query)
        res1=cursor.fetchall()
        for row in res1:
            print "Amt Due :",row[0]
            bill=row[0]



    elif booking_type=='weekly':
        query="update Weekly_Rental SET Booking_Status='Completed' WHERE Rent_Id="+rent_id+' And Cust_Id='+cust_id
        print "update query weekly: ",query
        cursor.execute(query)
        db.commit()
        query="select Amount_Due from Weekly_Rental where Rent_Id="+rent_id+' And Cust_Id='+cust_id
        cursor.execute(query)
        res1=cursor.fetchall()
        for row in res1:
            print "Amt Due :",row[0]
            bill=row[0]

    print "Final Amount due: ",bill
    my_res.append(bill)
    my_res.append('Completed')
    print "my res: ",my_res


    return render_template('return_car_results.html',
                           title='results',
                           my_res=my_res)



@application.route('/')
# Configure the Jinja2 environment.
def main_main():
    user = {'nickname': 'Miguel'}  # fake user
    mj1=['MJ','Jain','PJ']
    return render_template('main_file.html',
                           title='Home',
                           user=mj1)


# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()