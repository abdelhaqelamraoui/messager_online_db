
import database
import log


class Dblog:

   def __init__(self) -> None:
      """
      Test connection to the database. Init it if connection was successful.\n
      Inits log file.\n
      Throws Exception("Cannot inti dblog")
      """
      try:
         self.db = database.Database()
         self.log = log.Log()
      except:
         raise Exception("Cannot inti dblog")
      else:
         self.db.init()


   def write(self, msg):
      """
      
      """
      try:
         self.db.write(msg)
      except:
         raise Exception("Error writing logdb")
      else:
         self.log.push(self.db.read())


   def read(self):
      """
      Reads fro the database and add the record to the log file.\
      Throws  Exception("Error reading logdb")
      """
      try:
         rec = self.db.read()
      except:
         raise Exception("Error reading logdb")
      else:
         self.log.push(rec)
         return rec


   def update(self, msg):
      """
      Update a record with msg ang add it to the log file.\n
      Throws  Exception("Error updating logdb")
      """
      try:
         self.db.update(msg)
      except:
         raise Exception("Error updating logdb")
      else:
         self.log.push(self.db.read())