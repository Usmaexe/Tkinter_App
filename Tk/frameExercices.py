from tkinter import *
from tkinter import ttk
from events import *

class FrameBuilder() :
	def __init__(self,w,defaultPadding, nbFrames,content, names, actions):
		self.frame = ttk.Frame(w.window)
		self.frame.grid()
		
		# Dictionary to manage frames and buttons:
		frames = {}
		buttons = {}
		
		for i in range(nbFrames):
			name = f"frame_{i}"
			function_name = actions[i]
			
			# here func keyword is used to specify the function to be called when the button is clicked
			# If lambda keyword is used the last assigned function will be called
			# cause lambda call the last method assigned when the button is clicked and not when the code is written
			##IF AN EXCEPTION OCCURED IS MOSTLY BECAUSE OF THE USE OF FRAME BUILDER(THE ACTUALL CLASS IN THE EVENT FILE)
			my_lambda = lambda event, framePa=self.frame, func=function_name: globals()[func](event, frame)
			
			frames[name] = ttk.Frame(self.frame, padding=defaultPadding)
			frames[name].grid(row=int((i / 2) + 1), column=(i % 2) + 1)
			
			ttk.Label(frames[name], text=f"{names[i]}").grid(row=1, column=1)
			buttons[name] = ttk.Button(frames[name], text=f"See {content}")
			buttons[name].bind('<Button-1>', my_lambda)
			buttons[name].grid(row=2, column=1)
	
	def remove(self):
		self.frame.grid_remove()
		
	
		