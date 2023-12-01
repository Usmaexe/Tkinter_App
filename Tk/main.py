from windowSetUp import *
from menuSetUp import SetUp as msu
from widgetStyling import *




#COMPLETE modularing the project and set behaviour to the show more button
if __name__ == "__main__" :
    #Local Variables
    defaultPadding=50
    nbFrames = 5

    #Root window SetUp
    window,center_x,center_y = SetUp()
    #center_x and center_y are variables that will be used in the padding of the window

    #Menu SetUp
    window = msu(window)

    #Frame SetUp
    window = fsu(window,defaultPadding)

    #Calling Methodes of windowSetUps to place the widget and to set its internal padding :
    window = Dimensions(window,center_x,center_y)
    window = Padding(window, [center_x, center_y, nbFrames, defaultPadding])

    #The styling method configure the style of certain widgets
    styling()

    #defined method to display the method options of a widget
        #hl.stylename_elements_options('TFrame')

    window.mainloop()

