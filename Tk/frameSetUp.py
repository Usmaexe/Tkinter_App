from tkinter import ttk
from events import *

#This class is to build the second frame that is displayed when the show button is clicked on each section
class FrameBuilder :
	def __init__(self, w,defaultPadding, nbFrames,content, names, actions):
		frame0 = ttk.Frame(w.window)
		frame0.grid()

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
			my_lambda = lambda event, frame=frame0,win=w, func=function_name: globals()[func](event, frame,win)

			frames[name] = ttk.Frame(frame0, padding=defaultPadding)
			frames[name].grid(row=int((i / 2) + 1), column=(i % 2) + 1)

			ttk.Label(frames[name], text=f"{names[i]}").grid(row=1, column=1)
			buttons[name] = ttk.Button(frames[name], text=f"See {content}")
			buttons[name].bind('<Button-1>', my_lambda)
			buttons[name].grid(row=2, column=1)