

import mysql.connector


db = 'sql3434277'
usr = 'sql3434277'
prt = 3306
h = 'sql3.freesqldatabase.com'
pw = 'CqJDsbbAFN'

class Database:

   def __init__(self):
      """
      Check connection to the the dababase. If not succeded andException is raised.
      """
      try:
         self.conn = mysql.connector.connect(database=db, user=usr, password=pw, host=h, port= prt)
      except:
         raise Exception("Cannot connect to the database")

   def read(self):
      """
      Read the single record of the message table and return the fiels 'text'.\n
      Throws Exception("Writing Error")
      """
      query = "select * from message"
      try:
         cursor = self.conn.cursor()
         cursor.execute(query)
         records = cursor.fetchall()
         cursor.close()
         return records[0]
      except:
         raise Exception("Writing Error")

   def write(self, msg):
      """
      Inserts a record into the table message. id=1, date=now() and text = msg\n
      Throws Exception("Writing Error").
      """
      query = "INSERT INTO message values(1,NOW(),'{}');".format(msg)
      try:
         cursor = self.conn.cursor()
         cursor.execute(query)
         self.conn.commit()
         cursor.close()
      except:
         raise Exception("Writing Error")


   def update(self, msg):
      """
      Updates the single record in the table message with date=now() and text=msg\n
      Throws Exception('Empty text'), Exception("Error updating")
      """
      msg = str(msg).strip()
      if(not msg):
         raise Exception('Empty text')

      query = "Update message SET date = NOW(), text = '{}' where id = 1;".format(msg)
      try:
         cursor = self.conn.cursor()
         cursor.execute(query)
         self.conn.commit()
         cursor.close()
      except:
         raise Exception("Error updating")


   def init(self):
      """
      Creates the table 'message' in the data base if not existing.\n
      Throws Exception("Cannot init db")
      """
      query = "CREATE TABLE IF NOT EXISTS message (id INT PRIMARY KEY, date DATETIME, text VARCHAR(255)); "
      try:
         cursor = self.conn.cursor()
         cursor.execute(query)
         cursor.close()
      except:
         raise Exception("Cannot init db")