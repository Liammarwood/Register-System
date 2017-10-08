

#Register System!!!

#############################################################
#############################################################
import re
import tkinter as Tkinter # Imports the module of Tkinter to create a GUI
from tkinter import *

fields = ['First Name', 'Last Name', 'Gender', 'Number']# Sets the default headings of the file
the_class = [] # Creates a default class list but its empty

# Validates Phone Numbers
def rule(value):
    global child, error
    rule = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')
    if not rule.search(value):
        child[3] = 'None'
        msg = "Invalid mobile number"
        
        willow = Text(error,height=1, width=22)
        willow.pack()
        willow.insert(END,msg)

def genders():
    global child, error
    if child[2] == 'female':
        child[2] == child[2]
    elif child[2] == 'Female':
        child[2] == child[2]
    elif child[2] == 'F':
        child[2] == child[2]
    elif child[2] == 'f':
        child[2] == child[2]
    elif child[2] == 'Male':
        child[2] == child[2]
    elif child[2] == 'male':
        child[2] == child[2]
    elif child[2] == 'm':
        child[2] == child[2]
    elif child[2] == 'M':
        child[2] == child[2]
    else:
        error = Tk()
        child[2] = 'N'+'\A'
        t = Text(error,height=1, width=22)
        t.pack()
        t.insert(END,'Invalid Gender')

def upload_a_class(): # Uploading a class
    global classnumber, filename, the_class,entries, win # Makes all the local varibles global so it can be used elsewhere
    the_class = []
    win = Tk() # Makes a varible for the window called win
    entries = [] # Ceates an empty list for the user inputs 
    fields =['Filename','Class Size'] # creates a list with the varible names which will be needed 
    title = Label(win , text = 'Enter the .csv Filename')# Creates a label called title in the window
    title.grid(row = 0) # places this label at the top of the window
    y = 0 # creates a varible which will control the row change
    for field in fields: # loops for the amount of the fields eg 4
        y = y + 1 #  Adds one to the y varible
        row = Frame(win) # Adds a frame to the window
        lab = Label(row, width=15, text=field, anchor='w') #adds the fields into the window as a label
        ent = Entry(row)# places the label frame and entry into the window
        row.grid()#
        lab.grid(row = y , column = 0)#
        ent.grid(row= y, column = 1)#
        entries.append((field, ent)) #adds the fields and ent to the list entries
    b1 = Button(win, text='Enter Filename', command = (lambda: uploadname(entries)))# creates a button which will make the uploadname function run
    b1.grid(row=3, column=0)
    b3 = Button(win, text='Upload File', command = (lambda: collect())) # creates a button that makes the collect function run
    b3.grid(row=3, column=1)
    b2 = Button(win, text='Quit', command = win.destroy) # creates a button which quits the menu option and closes the window 
    b2.grid(row=3, column =2)
    return entries # returns the value entries 
    
    
def uploadname(entries): # creates a varible only in the procedure
    global filename, classsize # creates the varible global around the file
    userinput = [] # creates a empty list
    for entry in entries: # loop for the amount of entries need eg 4
      text  = entry[1].get() # gets the users inputs and places into a varible
      entry[1].delete(0, 'end') # deltete the values in the entry boxes
      userinput.append(text) # adds the text varible to the empty list which was created
    filename = userinput[0] # makes a varible that we need in other procedure of filename
    classsize = int(userinput[1]) # makes a varible that we need in other procedure of classsize

def collect(): # procedure to collect the file from its source
    global classsize,filename,entries,win # creates the local variblles global
    import csv # Imports the csv operations 
    import os # Imports the os operations
    exsit = os.path.exists(filename +".csv")# If a file called the users input exsits = true
    if exsit: # if statement determaning whether a file exsits 
        filename = filename # creates the filename into filename
        with open(filename + '.csv') as f: # opens the filename varible adding the .csv at the end for the file type
            reader = csv.reader(f) # creates a varible for the csv operation to read the file
            for  x in range(classsize+1): # creates a loop to loop for the amount of the varible classsize add 1 because of the titles 
                the_class.append(next(reader)) # adds each row that has been read by the varible to the class list
        the_class.pop(0) # gets rid of the first index item in the list of the_class
        win.destroy() # Deletes the window of win
        class_display() # runs the procedure of class_display
    else:
        wins = Tk() # creates another window called wins
        s =Label(wins,text= 'Upload not complete') # adds the label to the newer window 
        s.pack(side=TOP) # puts the label to top of the window 
        v =Label(wins,text= 'File not Found')# adds the label to the newer window 
        v.pack(side=TOP)  # puts the label to top of the window
        win.destroy() # deletes the origninal window

def take_register(): # Creates a procedyre to take a register
    global the_class # makes the class a global 
    entries=[] # makes the entries lsit empty 
    reg = Tk() # creates a new window called reg
    y = 0 # varible for the row
    z = 0 # varible index position 
    if the_class == []: #if statement the class list is empty
        f = Label(reg, text='No data') #creates a label to tell the user there is no data
        f.grid(row=0,column=1) 
    else: 
        for x in the_class: # loop for the amount of positions in the list class
            name = the_class[z][0] + " " + the_class[z][1] #name varible equals the z index and 0 position and 1 position so it equals the first and secound name
            rej = Frame(reg)#creates a frame in the reg
            lab = Text(rej, height=1, width=20) # creates a text box
            lab.insert(END, name)#adds the fields into the window as a label
            yes = 'Y'
            ent = Checkbutton(rej, text = '', varible = yes) # creates an entry box 
            rej.grid()
            lab.grid(row = y , column = 0) # makes the position of the text and 
            ent.grid(row = y , column = 1)# entry box to a row of y value
            entries.append((ent)) # adds the ent to the entries list 
            y = y + 1 # adds 1 to the varible
            z = z + 1 # adds 1 to the varible
        b1 = Button(reg, text='Enter Register',command=(lambda :attendence(entries))) # creates a button to enter the register 
        b1.grid(column = 0) 
    b2 = Button(reg, text='Quit', command = reg.destroy) # creates a button to quit the window 
    b2.grid(column =1)

def attendence(entries): # procedure to gather the entryboxes value 
    y = 0 # varible equals 0
    for index in range(len(entries)): # loop to add the vlues to the class list
        text = entries[0].get() # creates a  varible with the entrys data in 
        entries.pop(0) #deletes the entry box value 
        the_class[y][4]=text # adds the value to the sub list of the corrosponding child
        y = y + 1 # adds one to the varible so it will move to the next sublist
      

def move_data():  # procedure to move class data
    global entries, filename # makes the varibles global
    isitthere() #runs the procedure
    win = Tk() # creates a new window
    entries = [] # creates an empty list
    row = Frame(win) # adds a frame to the window
    lab = Label(row, width=15, text='Enter Filename', anchor='w') #adds the fields into the window as a label
    filename = Entry(row) # adds a entry box
    row.grid() # places the fram in the grid 
    lab.grid(row = 1 , column = 0) # adds the label to the left 
    filename.grid(row= 1, column = 1) # adds the filename next to the label
    entries.append((filename)) # adds the filename to the entries list
    b1 = Button(win, text='Create File',command=(lambda: movedatafile())) # creates a button to run move data file procedure
    b1.grid(row = 2) 
    
    
def movedatafile(): # creates a procedure to save the data to a file
    global entries, fields # makes the varible a global
    file = [] # creates an empty list
    for entry in entries: # loop to get the entries from the file 
        text  = entry.get() # gets the entry box  value into a varible
        entry.delete(0, 'end') # deltes the value out of the entry box
        file.append (text) # adds the entry to the filelist
        filename = file[0] # makes the file list varible position 0 to the varible filename
    file = open(filename+".csv" , 'w')#Opens up a new csv file and names it whatever the varible filename is
    with open (filename+".csv","w")as file: # With the file opened as a file does whatever in the indent
        fields.append('Present Y/N') # adds a new heading to the list
        file.write(str(fields)[1:-1] + "\n")#writes the titles to the fields so they are on the top row
        for i in range(0,len(the_class)):# for the length of the list nclass
            file.write(str(the_class[i])[1:-1] + "\n")#Writes the list nclass to the file
    file.close()# Closes the file
        
        
# Creates the child entry window form
def enter_child_form(root, fields):
   global the_class # creates the_class varible global 
   the_class = [] # clears all the data from the list of the class
   entries = [] # clears all the data from the list of the entries
   for field in fields: # loops for the amount of the fields eg 4
      row = Frame(root)# adds a new frame to the window
      lab = Label(row, width=15, text=field, anchor='w') #adds the fields into the window as a label
      ent = Entry(row) # adds a entry box to the window 
      row.pack(side=TOP, fill=X, padx=5, pady=5) # packs the row to the top
      lab.pack(side=LEFT) # packs the lab to the left
      ent.pack(side=RIGHT, expand=YES, fill=X) # packs the ent to the right 
      entries.append((field, ent)) # adds the ent and fields to the entries list
   return entries

def enter_child(): 
    if __name__ == '__main__':
        win = Tk()
        ents = enter_child_form(win, fields)
        win.bind('<Return>', (lambda event, e=ents: fetch(e)))   
        b1 = Button(win, text='Enter Child',command=(lambda e=ents: fetch(e)))# adds the buttons to the window 
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(win, text='Quit', command=win.destroy)# adds the buttons to the window to close it 
        b2.pack(side=LEFT, padx=5, pady=5)

def isitthere(): # Checks whether there is any data in  the list
   global the_class # makes the varible global
   if len(the_class) == 0:
      the_class = ['No class data avalible']
   else:
      the_class = the_class
   return the_class

def fetch(entries):# Gathering the values entered into the sytem
   global child
   child = [] # Sets the class 1 list to empty
   for entry in entries: # loop for the amount of entries need eg 4
      text  = entry[1].get() # gets the users inputs and places into a varible
      entry[1].delete(0, 'end') # Deletes the users input from the entry box
      child.append (text) # adds all the entries into the childs own list
   genders()
   rule(child[3])
   the_class.append(child) # adds the childs details into the class list

def search():
   global entries, win # makes the varible global in the document  
   win = Tk() # opens up a new window called win
   entries = [] # clears 
   system = Label(win, text= 'Search The Class') # adds a label to the gui window
   system.pack(side=TOP)
   b1 = Button(win, text='Search',command=enquire) #adds a button the the window
   b1.pack(side=BOTTOM, padx=5, pady=5)
   b2 = Button(win, text='Quit', command=win.destroy) # adds a quit button to the window 
   b2.pack(side=BOTTOM, padx=5, pady=5)
   isitthere() # runs the is it there procedure
   lab = Label(win, width=15, text="Enter Child's Name", anchor='w') #adds the fields into the window as a label
   ent = Entry(win) # adds a entry  box to the window
   lab.pack(side=TOP)
   ent.pack(side=BOTTOM, expand=YES, fill=X )
   entries.append((ent))#adds the ent to the list ready to get the values
   return entries

def enquire(): # gathers the entry box value for search 
   schild = [] #creates empty list
   for entry in entries: #loop to search the entry box
      text  = entry.get() # assigns the value from the box to a varible
      entry.delete(0, 'end')# clears the entry box
      schild.append (text) # adds the varible to the list
   findchild(schild[0]) # carrys out the procedure using the schild[0] as reference

def findchild(child):# procedural scope child is the same as schild[0]
   win = Tk() # creates new window
   lab = Label(win,text = 'Childs Details:') # creates a label e.g. title
   xchild = [] # creates an empty list
   position = 0 #create a varible for the position of a list later
   childfound = False # creates a boolean 
   length = 0 
   while childfound == False: # loop for while the boolean varible is 
      length = length + 1 # adds one to the varible for the list length
      if length > len(the_class): # if statement to find out whether the child is in the list 
         found = Label(win, width=15, text="This Child Isnt In The Register", anchor='w') # adds label if the length is longer than the lsit
         found.pack(side=BOTTOM)
      else:
         s = child in the_class[position] 
         if s == True: # if statement for if the child is in the class
               xchild.append(the_class[position][0])# adds first name to the xchild list
               xchild.append(the_class[position][1])# adds last name to the xchild list
               xchild.append(the_class[position][2])# adds the gender to the xchild list
               xchild.append(the_class[position][3])# adds the number to the xchild list
               T = Text(win, height=2, width=30) # creates a text box
               T.pack()
               T.insert(END, xchild[0:4]) # inserts the xchild into the text box
               #found = Text(win, width=15, text=xchild, anchor='w')
               #found.pack(side=BOTTOM)
               childfound = True
         else:
            position = position + 1

def class_display(): # displays all of the class
    isitthere() # runs the procedure
    win = Toplevel() 
    system = Label(win, text= 'Display Class')# add a label to the window 
    system.pack(side=TOP)
    b2 = Button(win, text='Quit', command=win.destroy)# add a button to the window to delete window 
    b2.pack(side=BOTTOM, padx=5, pady=5)
    position = 0
    for x in the_class: # creates a loop to display all the class
        syst = Label(win, text= the_class[position]) # creartes a label of the class one sublist
        syst.pack(side=TOP)
        position = position + 1

# MAIN PROGRAM     
root = Tk() # creates a root window

greeting = Tkinter.Label(text="Register System")
greeting.pack()

# Creates a text box to tell the user to quit
instruction = Tkinter.Label(text="Press the the <Esc> key to quit")
instruction.pack()

# Main window butons and running the procedure
button = Tkinter.Button(text="New Class", command= enter_child)# Change to new_class # WORKS
button.pack(side='bottom', fill='both')

button = Tkinter.Button(text="Take a register", command= take_register) # WORKS TO A DEGREE
button.pack(side='bottom', fill='both')

button = Tkinter.Button(text="Search For a Child", command= search)#search procedure #WORKS
button.pack(side='bottom', fill='both')

button = Tkinter.Button(text="Upload a Class", command= upload_a_class)
button.pack(side='bottom', fill='both')

button = Tkinter.Button(text="Display a Class", command= class_display) # display # WORKS
button.pack(side='bottom', fill='both')

button = Tkinter.Button(text="Save a Class", command= move_data)
button.pack(side='bottom', fill='both')

button = Tkinter.Button(text="Edit A Child", command= '')
button.pack(side='bottom', fill='both')
# runs the program
root.mainloop()
