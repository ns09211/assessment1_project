import mysql.connector as SQL
from datetime import datetime
import json

conn = SQL.connect( user='dummyUser',
                    password='dummyUser01',
                    host='db-intern.ciupl0p5utwk.us-east-1.rds.amazonaws.com')
c = conn.cursor()
c.execute("USE db_intern;")

def new_user(data):
    try:
        query = "INSERT INTO userData VALUES ('{0}','{1}','{2}','{3}','{4}')".format(data["Username"], data["Email"],data["Phone"], data["Password"],datetime.now())
        c.execute(query)
        conn.commit()
        return "User added Successfully"
    except Exception as e:
        print "[ERROR]: "+ str(e)
        return "User adding Failed"

def update_user(data):
    try:
        query = "UPDATE userData SET userName='{0}',phoneNo='{1}',password='{2}',dateTime='{3}' WHERE emailid='{4}'".format(data["Username"], data["Phone"], data["Password"],datetime.now(), data["Email"])
        c.execute(query)
        conn.commit()
        return "User updated Successfully"
    except Exception as e:
        print "[ERROR]: "+ str(e)
        return "User updation Failed"

def form_request(data, search=None):
    query = "select * from userData where emailid = '{0}'".format(data["Email"])
    c.execute("USE db_intern;")
    c.execute(query)
    record = c.fetchall()
    if search:
        query = "select * from userData where emailid = '{0}'".format(data["Email"])
        c.execute(query)
        record = c.fetchall()
        if len(record) == 1:
            response = {}
            for k,v in zip(["Username","Email","Phone","Password","Time"],record[0]):
                response[k] = str(v)
            response = json.dumps(response)
        else:
            response = "User Not Found"
    else:
        if len(record) == 1:
            response = update_user(data)
        else:
            response = new_user(data)
    return response

if __name__ == "__main__":
    print db_init()
