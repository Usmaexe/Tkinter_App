import subprocess
from tkinter import *
from tkinter import ttk, simpledialog, filedialog
from frameExercices import FrameBuilder
import windowSetUp

def frameReset(event,frame,newFrame):
    frame.grid()
    newFrame.remove()
    event.widget.grid_remove()
    #To adjust the positioning of return Button we should use the padding method

def showCryptage(event,frame,win):
    
    #Removing the Current Frame (Menu)
    frame.grid_remove()
    
    #The following Line of codes retrives the output of the ls command
    #Convert it to a list(exos)
    output = subprocess.check_output(["ls","Concepts/Cryptographie"],shell=True)
    exos=list((output.decode('utf-8')).split('\n'))
    try :
        exos.remove("")
        exos.remove("__pycache__")
    except Exception as e:
        print(e)
        
    
    # CREATING new frame layout
    newFrame = ttk.Frame(win.window)
    newFrame.grid(row=0,column=0)
    
    # THE RETURN BUTTON CREATED AND ADDED TO THE GRID
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1,sticky="NW")
    
    
    cryptageFrame = FrameBuilder(win, 10, len(exos), "Concepts/Cryptographie",exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event,frame,cryptageFrame))#Lambda function make sure that the function isn't called directly
    

def showAi(event, frame, win):
    #The following Line of codes retrives the output of the ls command
    #Convert it to a list(exos)
    output = subprocess.check_output(["ls","Concepts/NLP"],shell=True)
    exos=list((output.decode('utf-8')).split('\n'))
    try :
        exos.remove("")
        exos.remove("__pycache__")
    except Exception as e:
        print(e)
        
    frame.grid_remove()
    
    
    # CREATING new frame layout That will contain Buttons to open the files
    newFrame = ttk.Frame(win.window)
    newFrame.grid(row=0,column=0)
    
    #The return Button
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1,sticky="NW")
    
    NlpFrame = FrameBuilder(win, 10, len(exos), "Concepts/NLP",exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event,frame,NlpFrame))
    #Lambda function make sure that the function isn't called directly
    

def showFiles(event,frame, win):
    # The following Line of codes retrives the output of the ls command
    # Convert it to a list(exos)
    output = subprocess.check_output(["ls", "Concepts/Files_Managing"], shell=True)
    exos = list((output.decode('utf-8')).split('\n'))
    try:
        exos.remove("")
        exos.remove("__pycache__")
    except Exception as e:
        print(e)
    
    frame.grid_remove()
    
    # CREATING new frame layout That will contain Buttons to open the files
    newFrame = ttk.Frame(win.window)
    newFrame.grid(row=0, column=0)

    # The return Button
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1, sticky="NW")
    
    FilesFrame = FrameBuilder(win, 10, len(exos), "Concepts/Files_Managing", exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event, frame, FilesFrame))
    # Lambda function make sure that the function isn't called directly


def showPOO(event,frame, win):
    # The following Line of codes retrives the output of the ls command
    # Convert it to a list(exos)
    output = subprocess.check_output(["ls", "Concepts/OOP"], shell=True)
    exos = list((output.decode('utf-8')).split('\n'))
    print(exos)
    try:
        exos.remove("")
        exos.remove("__pycache__")
    except Exception as e:
        print(e)
    
    frame.grid_remove()
    
    # CREATING new frame layout That will contain Buttons to open the files
    newFrame = ttk.Frame(win.window)
    newFrame.grid(row=0, column=0)
    
    # The return Button
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1, sticky="NW")
    
    OopFrame = FrameBuilder(win, 10, len(exos), "Concepts/OOP", exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event, frame, OopFrame))
    # Lambda function make sure that the function isn't called directly


def showTkinter(event,frame, win):
    frame.grid_remove()
    # The following Line of codes retrives the output of the ls command
    # Convert it to a list(exos)
    output = subprocess.check_output(["ls", "Concepts/Tkinter"], shell=True)
    exos = list((output.decode('utf-8')).split('\n'))
    print(exos)
    try:
        exos.remove("")
        exos.remove("__pycache__")
    except Exception as e:
        print(e)

    frame.grid_remove()

    # CREATING new frame layout That will contain Buttons to open the files
    newFrame = ttk.Frame(win.window)
    newFrame.grid(row=0, column=0)

    # The return Button
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1, sticky="NW")

    TkinterFrame = FrameBuilder(win, 10, len(exos), "Concepts/Tkinter", exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event, frame, TkinterFrame))
    # Lambda function make sure that the function isn't called directly


def showAlgorithms(event,frame, win):
    frame.grid_remove()
    # The following Line of codes retrives the output of the ls command
    # Convert it to a list(exos)
    output = subprocess.check_output(["ls", "Concepts/Algos"], shell=True)
    exos = list((output.decode('utf-8')).split('\n'))
    print(exos)
    try:
        exos.remove("")
        exos.remove("__pycache__")
    except Exception as e:
        print(e)
    
    frame.grid_remove()
    
    # CREATING new frame layout That will contain Buttons to open the files
    newFrame = ttk.Frame(win.window)
    newFrame.grid(row=0, column=0)
    
    # The return Button
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1, sticky="NW")
    
    AlgosFrame = FrameBuilder(win, 10, len(exos), "Concepts/Algos", exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event, frame, AlgosFrame))
    # Lambda function make sure that the function isn't called directly


def CreateNew(window):
    #1ST LINE : CREATE THE NEW WINDOW, 2ND LINE : SET DIMENSIONS AND POSITION ON THE SCREEN TO IT
    conceptName = simpledialog.askstring(title="New Concept",prompt="Enter a value")
    fileTypes = [
        ("PDF files", "*.pdf"),
        ("Python files", "*.py"),
        ("Jupyter Notebook files", "*.ipynb"),
        ("All files", "*.*")
    ]
    #Default mode is read
    filesNames = filedialog.askopenfilenames(title="Select Files",filetypes=fileTypes,initialfile="Help/Guide.txt")
    
    print(conceptName)
    if filesNames :
        for file in filesNames :
            print(file)
    