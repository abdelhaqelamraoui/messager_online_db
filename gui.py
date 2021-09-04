

import tkinter as tk
from database import Database
import dblog as dl


class Gui(tk.Frame):

   label_auth = None
   canvas = None
   text_out = None
   text_in = None
   btn_read = None
   btn_write = None
   dbl = None

   def __init__(self, root):
      tk.Frame.__init__(self, root)
      root.title("Messager")
      root.geometry("400x400")
      root.resizable(0,0)
      self.root = root

      
      try:
         self.dbl = dl.Dblog()
      except Exception as e:
         print(e)

   def show(self):
      self.canvas = tk.Canvas(self.root, width=400, height=400)
      self.canvas.create_rectangle(3,3, 399, 397, outline='black', width=2)
      self.canvas.create_line(3,383, 398, 383, width=2)

      self.text_out = tk.Text(self.root, width=45, height=9, wrap=tk.WORD)
      # self.canvas.create_rectangle(3,3, 399, 397, outline='black', width=2)
      
      self.text_in = tk.Text(self.root, width=45, height=5)
      # self.canvas.create_rectangle(3,3, 399, 397, outline='black', width=2)

      self.btn_read = tk.Button(self.root, text='Read', font='Ubuntu 8',bg='#27743c',
      fg='#ffffff', activeforeground='white', activebackground='#004156', width=12, command=self.read)
      self.btn_write = tk.Button(self.root, text='Write', font='Ubuntu 8', bg='#27743c',
      fg='#ffffff', activeforeground='white', activebackground='#004156', width=12, command=self.write)
      auth = "By: Abdelhaq El Amraoui  Ⓒ2021  |  www.elam-2020.blogspot.com"
      self.label_auth = tk.Label(self.root, text=auth, font="Ubuntu-Mono 8", bg="#c3c4c4", width=600)
      

      self.label_auth.place(x=200, y=400, anchor='s')
      self.canvas.place(x=200, y =200, anchor='center')

      self.text_out.place(x=200, y=200, anchor='s')
      self.text_in.place(x=200, y=300, anchor='s')

      self.btn_read.place(x=100, y=350, anchor='s')
      self.btn_write.place(x=300, y=350, anchor='s')

      #show the las message
      self.read()


   def read(self):
      try:
         row = self.dbl.read()
         date = str(row[1])
         txt = str(row[2])
         msg = f"----------------------------------{date}\n{txt}"
         print('read >>>>>>>> ', txt)
         self.text_out.configure(state='normal')
         self.text_out.delete('1.0', 'end')
         self.text_out.insert('1.0', msg)
         self.text_out.configure(state='disabled')
      except Exception as e:
         print(e)


   def write(self):
      msg = self.text_in.get(1.0, tk.END + '-1c') # to get it without the extra newline 
      print('written >>>>>>>>> ', msg)
      try:
         self.dbl.update(msg)
      except Exception as e:
         print(e)

if __name__ == '__main__':
   window = tk.Tk()
   gui = Gui(root=window)
   gui.show()
   window.mainloop()