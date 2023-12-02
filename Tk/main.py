from windowSetUp import *
from widgetStyling import *
from frameSetUp import Frame

#COMPLETE modularing the project and set behaviour to the show more button
if __name__ == "__main__" :

    #Local Variables
    defaultPadding=50
    nbFrames = 5

    
    # Root Window SetUp
    root = Window("Assets/windowLogo.ico", "Python's Concepts", "#ffffff", int(350 * 1.6), int(400 * 2.4))

    # MENU SetUp
    root.Menu()


    # FRAME SetUp
    names = ["Cryptage","AI","POO","Files","Tkinter","Algorithms"]
    actions = ["showCryptage","showAi","showPOO","showFiles","showAlgorithms","showTkinter"]
    #icons = []
    frame = Frame(root,defaultPadding, 6, names, actions)

    # SPACE MANAGING
    #Calling Methodes of windowSetUps to place the widget and to set its internal padding :
    #NB : The centering of the window should always be after the creation of the menu
    center_x,center_y = root.Dimensions()
    root.Padding([center_x, center_y, nbFrames, defaultPadding])

    # STYLE method configure the style of certain widgets
    styling()

    #defined method to display the method options of a widget
        #hl.stylename_elements_options('TFrame')

    root.window.mainloop()

