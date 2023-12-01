def fsu(window,defaultPadding,nbFrames,names,actions):
	#Dictionnary to manage frames :
	frames = {}


	for i in range(nbFrames):
		name = f"frame_{i}"
		function_name = actions[i]
		my_lambda = lambda event, frame=frame0

		frames[name] = ttk.Frame(frame0,padding=defaultPadding)
	    frames[name].grid(row=1, column=1)
	    label = ttk.Label(frames[name], text=f"{names[i]}").grid(row=1, column=1)
	    button = ttk.Button(frames[name], text="see more")
	    button.bind('<Button-1>', )
		globals()[function_name] = lambda event, frame0, i=i : my_lambda

	    button.grid(row=2, column=1)
