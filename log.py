

from os import mkdir, path

class Log:
   log_file_name = './.log/.log'
   def __init__(self) -> None:
      """
      Creates log dir and file if not existing
      """
      if not path.exists('./.log'):
         mkdir('./.log')
         open(self.log_file_name, 'w').close()


   def push(self, rec):
      """
      Adds a new message with its date to the log file
      """
      date = str(rec[1])
      txt = str(rec[2])
      with open(self.log_file_name, 'a') as f:
         f.write(date + '\n' + txt + '\n')
   

   def read(self):
      """
      Reads the content of the log file
      """
      with open(self.log_file_name, 'r') as f:
         return f.read()

