from tkinter import * 

####################################
# customize these functions
####################################

def init(data):
    data.iconWidth = data.width/3
    data.iconHeight = data.height/3
    data.margin = data.width/10
    data.hasStarted = False
    data.AELogo = PhotoImage(file="AELogo.png")
    data.AFLogo = PhotoImage(file="AFLogo.png")
    data.NikeLogo = PhotoImage(file="NikeLogo.png")
    data.SLogo = PhotoImage(file="SupremeLogo.png")
    data.textSize = data.width//25
    resizeImage(data)

def mousePressed(event, data):
    if data.hasStarted == False:
        if event.x > data.margin and event.x < data.margin+data.iconWidth and \
        event.y > data.margin and event.y < data.margin+data.iconHeight:
            print("Run American Eagle")
            data.hasStarted = True
        elif event.x > data.width-data.margin-data.iconWidth and \
        event.x < data.width-data.margin and event.y > data.margin and \
        event.y < data.margin+data.iconHeight:
            print("Run Abercrombie & Fitch")
            data.hasStarted = True
        elif event.x > data.margin and event.x < data.margin+data.iconWidth and \
        event.y > data.height-data.margin-data.iconHeight and \
        event.y < data.height-data.margin:
            print("Run Nike")
            data.hasStarted = True
        elif event.x > data.width-data.margin-data.iconWidth and event.x < data.width-data.margin \
        and event.y > data.height-data.margin-data.iconHeight and event.y < data.height-data.margin:
            print("Run Supreme")
            data.hasStarted = True

def keyPressed(event, data):
    if data.hasStarted:
        if event.keysym == "r":
            print("restart")
            init(data)

def timerFired(data):
    pass
    
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)
    
def resizeImage(data):
    data.AELogo = data.AELogo.zoom(int(data.iconWidth)//100, int(data.iconHeight)//100)
    data.AELogo = data.AELogo.subsample(data.AELogo.width()//100, data.AELogo.height()//100)
    data.AFLogo = data.AFLogo.zoom(int(data.iconWidth)//100, int(data.iconHeight)//100)
    data.AFLogo = data.AFLogo.subsample(data.AFLogo.width()//120, data.AFLogo.height()//120)
    data.NikeLogo = data.NikeLogo.zoom(int(data.iconWidth)//50, int(data.iconHeight)//50)
    data.NikeLogo = data.NikeLogo.subsample(data.NikeLogo.width()//120, data.NikeLogo.height()//120)
    data.SLogo = data.SLogo.zoom(int(data.iconWidth)//50, int(data.iconHeight)//50)
    data.SLogo = data.SLogo.subsample(data.SLogo.width()//120, data.SLogo.height()//120)
    
def drawScreen(canvas, data):
    AEBrown = rgbString(191, 175, 155)
    AFMaroon = rgbString(88, 36, 40)
    NikeRed = rgbString(215, 31, 23)
    SupremeRed = rgbString(237, 28, 36)
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue", width=0)
    canvas.create_rectangle(data.margin, data.margin, 
        data.margin + data.iconWidth, data.margin + data.iconHeight, fill=AEBrown, width=0)
    canvas.create_rectangle(data.width-data.margin-data.iconWidth, data.margin,
        data.width-data.margin, data.margin+data.iconHeight, fill=AFMaroon, width=0)
    canvas.create_rectangle(data.margin, data.height-data.margin-data.iconHeight,
        data.margin+data.iconWidth, data.height-data.margin, fill="Black", width=0)
    canvas.create_rectangle(data.width-data.margin-data.iconWidth, data.height-data.margin-data.iconHeight,
        data.width-data.margin, data.height-data.margin, fill=SupremeRed, width=0)
    canvas.create_image(data.margin+data.iconWidth/2, data.margin+data.iconHeight/2, 
        image=data.AELogo)
    canvas.create_image(data.width-data.margin-data.iconWidth/2, data.margin+data.iconHeight/2, 
        image=data.AFLogo)
    canvas.create_image(data.margin+data.iconWidth/2, data.height-data.margin-data.iconHeight/2,
        image=data.NikeLogo)
    canvas.create_image(data.width-data.margin-data.iconWidth/2, data.height-data.margin-data.iconHeight/2,
        image=data.SLogo)
    canvas.create_text(data.width/2, data.margin/2, text="Welcome to 15-112 Virtual Closet!", font="Verdana %d" % data.textSize, fill="lime green")
    canvas.create_text(data.width/2, data.height/2, text="Select a Brand to Begin", font="Verdana %d" % data.textSize, fill="lime green")
    
    

def redrawAll(canvas, data):
    drawScreen(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)