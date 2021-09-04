

from os import mkdir, path

class Log:
   log_file_name = './.log/.log'
   def __init__(self) -> None:
      if not path.exists('./.log'):
         mkdir('./.log')
         open(self.log_file_name, 'w').close()


   def push(self, rec):
      date = str(rec[1])
      txt = str(rec[2])
      with open(self.log_file_name, 'a') as f:
         f.write(date + '\n' + txt + '\n')
   

   def read(self):
      with open(self.log_file_name, 'r') as f:
         return f.read()

