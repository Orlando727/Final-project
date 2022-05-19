from json.tool import main
import sqlite3
from datetime import datetime, timedelta
from unicodedata import name
from dateutil import parser
import smtplib, ssl
 

class SqlParse:
    
    def __init__(self) -> None:
        pass
        
    def get_data_in_db(self, db_name: str, command: str) -> object:
        connect = sqlite3.connect(db_name)
        cursor_obj = connect.cursor()
        cursor_obj.execute(command)
        rows = cursor_obj.fetchall()
        yield rows 
 

class TimeDataCheck:
    def __init__(self) -> None:
        pass
            
    def get_data_from_db(self, data):
        current_time = datetime.now()
        deadline_time = current_time + timedelta(hours=6)
        try:
            for some in data:
                new_var = parser.parse(some[2])
                if deadline_time > new_var:
                    
                    return some
        except:
            raise ValueError("Данные распакованы неправильно, забыл *")    
                


data_base_variable = SqlParse()

    
data_base_data =  data_base_variable.get_data_in_db("db.sqlite3", 
                                                    'SELECT id, title, due_date FROM task_manager_app_taskmanageritem')

time_data_check = TimeDataCheck()
send_message = time_data_check.get_data_from_db(*data_base_data)


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "tuletestmail@gmail.com"
receiver_email = "tule_85@mail.ru"
password = input("Type your password and press enter: ")
message = "Your task item{}, is going to expire".format(send_message)



context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)