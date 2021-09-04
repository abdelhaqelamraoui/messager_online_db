
import database
import log


class Dblog:

   def __init__(self) -> None:
      try:
         self.db = database.Database()
         self.db.init()
         self.log = log.Log()
      except:
         raise Exception("Cannot inti dblog")


   def write(self, msg):
      try:
         self.db.write(msg)
      except:
         raise Exception("Error writing logdb")
      else:
         self.log.push(self.db.read())


   def read(self):
      try:
         rec = self.db.read()
      except:
         raise Exception("Error reading logdb")
      else:
         self.log.push(rec)
         return rec

   def update(self, msg):
      try:
         self.db.update(msg)
      except:
         raise Exception("Error updating logdb")
      else:
         self.log.push(self.db.read())