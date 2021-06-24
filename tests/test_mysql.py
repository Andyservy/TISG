# print("This is my file to test Python's execution methods.")
# print("The variable __name__ tells me which context this file is running in.")
# print("The value of __name__ is:", repr(__name__))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import pymysql
#Since I am not very familiar with the layout manager,It ’s a fixed position,Causes the window to stretch less well
class myapp (wx.app):
 def __init__ (self):
  wx.app .__init__ (self)
  frame=wx.frame (parent=None, title="login", size=(532,420))
  #Set the icon in the upper left corner of the window
  #Where parameter type represents the type of picture,There are also ico, jpgm and other types
  icon_1=wx.icon (name="python1.png", type=wx.bitmap_type_png)
  frame.seticon (icon_1)
  panel=wx.panel (frame, -1)
  #Add images to panel
  image=wx.image ("python2.jpg", wx.bitmap_type_jpeg) .converttobitmap ()
  wx.staticbitmap (panel, -1, bitmap=image, pos=(0, 0))
  #Add static tags
  label_user=wx.statictext (panel, -1, "Account:", pos=(80,200))
  label_pass=wx.statictext (panel, -1, "Password:", pos=(80,240))
  #Add text input box
  self.entry_user=wx.textctrl (panel, -1, size=(200,30), pos=(130,200))
  #style for setting input
  self.entry_pass=wx.textctrl (panel, -1, size=(200,30), pos=(130,240), style=wx.te_password)
  #Add button
  self.but_login=wx.button (panel, -1, "login", size=(120,50), pos=(120,300))
  self.but_register=wx.button (panel, -1, "register", size=(120,50), pos=(260,300))
  #Set the color of the button
  self.but_login.setbackgroundcolour ("#0a74f7")
  self.but_register.setbackgroundcolour ("#282c34")
  #Binding events to buttons
  self.bind (wx.evt_button, self.on_but_login, self.but_login)
  self.bind (wx.evt_button, self.on_but_register, self.but_register)
  #
  frame.center()
  frame.show(True)
 #Define a message popup box function
 def show_message (self, word=""):
  dlg=wx.messagedialog (None, word, u"error", wx.yes_no | wx.icon_question)
  if dlg.showmodal () == wx.id_yes:
   #self.close (true)
   pass
  dlg.destroy ()
 def on_but_login (self, event):
  #Connect to the local database
  user_name=self.entry_user.getvalue ()
  pass_word=self.entry_pass.getvalue ()
  sql="" "select pass from student where name ="%s "" ""%(user_name)
  #Judge, check if the username and password are empty
  #Not empty after query and judgment
  #Otherwise, it will cause errors when the password or username is empty
  if user_name and pass_word:
   db=pymysql.connect (host="localhost", user="root",   password="zhang123", db="user", port=3306)
   #Use cursor () method to obtain the operation cursor
   cur=db.cursor ()
   try:
    cur.execute (sql) #execute SQL statement
    results=cur.fetchall () #Get all records of the query
    #The return value is in the form of a tuple
    #print (type (results))
    if results:
     #print (type (results [0] [0]))
     #print (results [0] [0])
     if results [0] [0] == pass_word:
      #Means login is successful,Follow-up can write the interface after successful login
      #Will not write here
      pass
      #print ("sucessful")
     else:
      self.show_message (word="password error")
    else:
     self.show_message (word="username does not exist")
   except exception as e:
    db.rollback ()
   finally:
    db.close () #Close the connection
  else:
   self.show_message (word="Account and password cannot be empty")
 def on_but_register (self, event):
  #Similar to the query above,Just get the relevant content and insert it into the database to make related operations
  #Content is similar to the above,No longer writing
  pass
if __name__ == "__ main__":
 app=myapp ()
 app.mainloop ()
