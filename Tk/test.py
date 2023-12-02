from frameSetUp import *
from windowSetUp import *
from widgetStyling import *


names = ["Cryptatest","test","Ptest"]
actions = ["showCryptage","showAi","showPOO","showFiles","showAlgorithms","showTkinter"]
defaultPadding=50

if __name__ == '__main__':
	# Root Window SetUp
	root = Window("Assets/windowLogo.ico", "Python's Concepts", "#ffffff", int(350 * 1.6), int(400 * 2.4))

	# MENU SetUp
	root.Menu()

	# FRAME SetUp

	frame = FrameBuilder(root, defaultPadding, len(names), names, actions)

	# SPACE MANAGING
	# Calling Methodes of windowSetUps to place the widget and to set its internal padding :
	# NB : The centering of the window should always be after the creation of the menu
	center_x, center_y = root.Dimensions()
	root.Padding([center_x, center_y, defaultPadding])

	# STYLE method configure the style of certain widgets
	styling()

	root.window.mainloop()