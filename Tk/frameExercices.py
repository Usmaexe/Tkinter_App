from tkinter import *
from tkinter import ttk
from events import *

class FrameBuilder() :
	def __init__(self, w, defaultPadding:int, nbFrames:int, directory:str, actions:list[str]):
		self.frame = ttk.Frame(w.window)
		self.frame.grid()
		
		# Dictionary to manage frames and buttons:
		frames = {}
		buttons = {}
		
		for i in range(nbFrames):
			name = f"frame_{i}"
			path = directory + "/" + actions[i]
			
			##IF AN EXCEPTION OCCURED IS MOSTLY BECAUSE OF THE USE OF FRAME BUILDER(THE ACTUALL CLASS IN THE EVENT FILE)
			my_lambda = lambda event, framePa=self.frame, file=path: globals()["open"](event, framePa, file)
			
			frames[name] = ttk.Frame(self.frame ,padding=defaultPadding)
			frames[name].grid(row=i+1, column=1)
			
			buttons[name] = ttk.Button(frames[name], text=f"{actions[i]}")
			buttons[name].bind('<Button-1>', my_lambda)
			buttons[name].grid(row=1, column=1)
	
	def remove(self):
		self.frame.grid_remove()
		
	
		