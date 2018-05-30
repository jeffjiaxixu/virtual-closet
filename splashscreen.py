from tkinter import * 
from CVStuff import *
from OOPy import *
from allTheInfo import *
import PIL
from PIL import ImageTk
####################################
# customize these functions
####################################

def init(data):
    #specify dimension in main menu
    data.iconWidth = data.width/3
    data.iconHeight = data.height/3
    data.margin = data.width/10
    data.hasStarted = False
    data.startWebcam = False
    data.runHelpMenu = False
    #all the logos
    data.AELogo = PhotoImage(file="AELogo.png")
    data.AFLogo = PhotoImage(file="PSLogo.png")
    data.NikeLogo = PhotoImage(file="NikeLogo.png")
    data.SLogo = PhotoImage(file="SupremeLogo.png")
    data.textSize = data.width//25
    data.timer = 0
    #running each company
    data.waitAE = False
    data.waitAF = False
    data.waitNike = False
    data.waitSupreme = False
    data.runAE = False
    data.runAF = False
    data.runNike = False
    data.runSupreme = False
    data.runShirtMenu = False
    data.runGlassesMenu = False
    data.runInfoMenu = False
    #dimension of submenu
    data.menuMargin = data.width/20
    data.menuCellWidth = (data.width-data.menuMargin*2)/3
    data.menuCellHeight = (data.height-data.menuMargin*4)/3
    data.menuButtonHeight = data.height/6
    data.rightArrow = PhotoImage(file="rightArrow.png")
    data.leftArrow = PhotoImage(file="leftArrow.png")
    #color of icons on main menu
    data.AEBrown = rgbString(191, 175, 155)
    data.AFMaroon = rgbString(88, 36, 40)
    data.NikeRed = rgbString(215, 31, 23)
    data.SupremeRed = rgbString(237, 28, 36)
    #indicate the cell selected
    data.highlightedShirtCell = (3, 3)
    data.highlightedGlassesCell = (3, 3)
    data.selectedGlasses = 9
    data.selectedShirt = 9
    #sizing charts for info menu
    data.AESizingChart = ImageTk.PhotoImage(Image.open("AESizeChart.png"))
    data.AFSizingChart = ImageTk.PhotoImage(Image.open("AFSizeChart.png"))
    data.NikeSizingChart = ImageTk.PhotoImage(Image.open("NikeSizeChart.png"))
    data.SupremeSizingChart = ImageTk.PhotoImage(Image.open("SupremeSizeChart.png"))
    #all the AE shirts for menu display
    data.AEDis1 = ImageTk.PhotoImage(Image.open("./AEShirts/AE1.png"))
    data.AEDis2 = ImageTk.PhotoImage(Image.open("./AEShirts/AE2.png"))
    data.AEDis3 = ImageTk.PhotoImage(Image.open("./AEShirts/AE3.png"))
    data.AEDis4 = ImageTk.PhotoImage(Image.open("./AEShirts/AE4.png"))
    data.AEDis5 = ImageTk.PhotoImage(Image.open("./AEShirts/AE5.png"))
    data.AEDis6 = ImageTk.PhotoImage(Image.open("./AEShirts/AE6.png"))
    data.AEDis7 = ImageTk.PhotoImage(Image.open("./AEShirts/AE7.png"))
    data.AEDis8 = ImageTk.PhotoImage(Image.open("./AEShirts/AE8.png"))
    data.AEDis9 = ImageTk.PhotoImage(Image.open("./AEShirts/AE9.png"))
    #all the Pacsun shirts for menu display
    data.AFDis1 = ImageTk.PhotoImage(Image.open("./AFShirts/AF1.png"))
    data.AFDis2 = ImageTk.PhotoImage(Image.open("./AFShirts/AF2.png"))
    data.AFDis3 = ImageTk.PhotoImage(Image.open("./AFShirts/AF3.png"))
    data.AFDis4 = ImageTk.PhotoImage(Image.open("./AFShirts/AF4.png"))
    data.AFDis5 = ImageTk.PhotoImage(Image.open("./AFShirts/AF5.png"))
    data.AFDis6 = ImageTk.PhotoImage(Image.open("./AFShirts/AF6.png"))
    data.AFDis7 = ImageTk.PhotoImage(Image.open("./AFShirts/AF7.png"))
    data.AFDis8 = ImageTk.PhotoImage(Image.open("./AFShirts/AF8.png"))
    data.AFDis9 = ImageTk.PhotoImage(Image.open("./AFShirts/AF9.png"))
    #all the J Crew shirts for menu display
    data.NikeDis1 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike1.png"))
    data.NikeDis2 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike2.png"))
    data.NikeDis3 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike3.png"))
    data.NikeDis4 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike4.png"))
    data.NikeDis5 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike5.png"))
    data.NikeDis6 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike6.png"))
    data.NikeDis7 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike7.png"))
    data.NikeDis8 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike8.png"))
    data.NikeDis9 = ImageTk.PhotoImage(Image.open("./NikeShirts/Nike9.png"))
    #all the Scotch & Soda shirts for menu display
    data.SupremeDis1 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme1.png"))
    data.SupremeDis2 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme2.png"))
    data.SupremeDis3 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme3.png"))
    data.SupremeDis4 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme4.png"))
    data.SupremeDis5 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme5.png"))
    data.SupremeDis6 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme6.png"))
    data.SupremeDis7 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme7.png"))
    data.SupremeDis8 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme8.png"))
    data.SupremeDis9 = ImageTk.PhotoImage(Image.open("./SupremeShirts/Supreme9.png"))
    #all the glasses for menu display
    data.GDis1 = ImageTk.PhotoImage(Image.open("./Glasses/G1.png"))
    data.GDis2 = ImageTk.PhotoImage(Image.open("./Glasses/G2.png"))
    data.GDis3 = ImageTk.PhotoImage(Image.open("./Glasses/G3.png"))
    data.GDis4 = ImageTk.PhotoImage(Image.open("./Glasses/G4.png"))
    data.GDis5 = ImageTk.PhotoImage(Image.open("./Glasses/G5.png"))
    data.GDis6 = ImageTk.PhotoImage(Image.open("./Glasses/G6.png"))
    data.GDis7 = ImageTk.PhotoImage(Image.open("./Glasses/G7.png"))
    data.GDis8 = ImageTk.PhotoImage(Image.open("./Glasses/G8.png"))
    data.GDis9 = ImageTk.PhotoImage(Image.open("./Glasses/G9.png"))
    #all the AE shirts raw files to be used in OpenCV
    data.AECV1 = "./AEShirts/AE1.png"
    data.AECV2 = "./AEShirts/AE2.png"
    data.AECV3 = "./AEShirts/AE3.png"
    data.AECV4 = "./AEShirts/AE4.png"
    data.AECV5 = "./AEShirts/AE5.png"
    data.AECV6 = "./AEShirts/AE6.png"
    data.AECV7 = "./AEShirts/AE7.png"
    data.AECV8 = "./AEShirts/AE8.png"
    data.AECV9 = "./AEShirts/AE9.png"
    #all the Pacsun shirts raw files to be used in OpenCV
    data.AFCV1 = "./AFShirts/AF1A.png"
    data.AFCV2 = "./AFShirts/AF2A.png"
    data.AFCV3 = "./AFShirts/AF3A.png"
    data.AFCV4 = "./AFShirts/AF4A.png"
    data.AFCV5 = "./AFShirts/AF5A.png"
    data.AFCV6 = "./AFShirts/AF6A.png"
    data.AFCV7 = "./AFShirts/AF7A.png"
    data.AFCV8 = "./AFShirts/AF8A.png"
    data.AFCV9 = "./AFShirts/AF9A.png"
    #all the J Crew shirts raw files to be used in OpenCV
    data.NikeCV1 = "./NikeShirts/Nike1A.png"
    data.NikeCV2 = "./NikeShirts/Nike2A.png"
    data.NikeCV3 = "./NikeShirts/Nike3A.png"
    data.NikeCV4 = "./NikeShirts/Nike4A.png"
    data.NikeCV5 = "./NikeShirts/Nike5A.png"
    data.NikeCV6 = "./NikeShirts/Nike6A.png"
    data.NikeCV7 = "./NikeShirts/Nike7A.png"
    data.NikeCV8 = "./NikeShirts/Nike8A.png"
    data.NikeCV9 = "./NikeShirts/Nike9A.png"
    #all the Scotch & Soda shirts raw files to be used in OpenCV
    data.SupremeCV1 = "./SupremeShirts/Supreme1A.png"
    data.SupremeCV2 = "./SupremeShirts/Supreme2A.png"
    data.SupremeCV3 = "./SupremeShirts/Supreme3A.png"
    data.SupremeCV4 = "./SupremeShirts/Supreme4A.png"
    data.SupremeCV5 = "./SupremeShirts/Supreme5A.png"
    data.SupremeCV6 = "./SupremeShirts/Supreme6A.png"
    data.SupremeCV7 = "./SupremeShirts/Supreme7A.png"
    data.SupremeCV8 = "./SupremeShirts/Supreme8A.png"
    data.SupremeCV9 = "./SupremeShirts/Supreme9A.png"
    #all the glasses raw files to be used in OpenCV
    data.GCV1 = "./Glasses/G1A.png"
    data.GCV2 = "./Glasses/G2A.png"
    data.GCV3 = "./Glasses/G3A.png"
    data.GCV4 = "./Glasses/G4A.png"
    data.GCV5 = "./Glasses/G5A.png"
    data.GCV6 = "./Glasses/G6A.png"
    data.GCV7 = "./Glasses/G7A.png"
    data.GCV8 = "./Glasses/G8A.png"
    data.GCV9 = "./Glasses/G9A.png"
    #list of images for use in info screen
    data.AEDisList=[data.AEDis1, data.AEDis2, data.AEDis3, data.AEDis4, data.AEDis5, data.AEDis6, data.AEDis7, 
    data.AEDis8, data.AEDis9]
    data.AFDisList=[data.AFDis1, data.AFDis2, data.AFDis3, data.AFDis4, data.AFDis5, data.AFDis6, data.AFDis7, 
    data.AFDis8, data.AFDis9]
    data.NikeDisList=[data.NikeDis1, data.NikeDis2, data.NikeDis3, data.NikeDis4, data.NikeDis5, data.NikeDis6, 
    data.NikeDis7, data.NikeDis8, data.NikeDis9]
    data.SupremeDisList=[data.SupremeDis1, data.SupremeDis2, data.SupremeDis3, data.SupremeDis4, data.SupremeDis5, 
    data.SupremeDis6, data.SupremeDis7, data.SupremeDis8, data.SupremeDis9]
    data.GDisList = [data.GDis1, data.GDis2, data.GDis3, data.GDis4, data.GDis5, data.GDis6, data.GDis7, 
    data.GDis8, data.GDis9]
    #glasses logos for info screen
    data.oliverPeople = ImageTk.PhotoImage(Image.open("./glasses/oliverPeople.png"))
    data.michaelKors = ImageTk.PhotoImage(Image.open("./glasses/michaelKors.png"))
    data.gucci = ImageTk.PhotoImage(Image.open("./glasses/gucci.png"))
    data.persol = ImageTk.PhotoImage(Image.open("./glasses/persol.png"))
    data.sunglassesHut = ImageTk.PhotoImage(Image.open("./glasses/sunglassesHut.png"))
    data.GLogoDict = {"Oliver People": data.oliverPeople, "Michael Kors": data.michaelKors, "Gucci": data.gucci, 
    "Persol": data.persol, "Sunglasses Hut": data.sunglassesHut}
    #list of images for use in OpenCV
    data.AEList=[data.AECV1, data.AECV2, data.AECV3, data.AECV4, data.AECV5, data.AECV6, data.AECV7, 
    data.AECV8, data.AECV9, 0]
    data.AFList=[data.AFCV1, data.AFCV2, data.AFCV3, data.AFCV4, data.AFCV5, data.AFCV6, data.AFCV7, 
    data.AFCV8, data.AFCV9, 0]
    data.NikeList=[data.NikeCV1, data.NikeCV2, data.NikeCV3, data.NikeCV4, data.NikeCV5, data.NikeCV6, data.NikeCV7, 
    data.NikeCV8, data.NikeCV9, 0]
    data.SupremeList=[data.SupremeCV1, data.SupremeCV2, data.SupremeCV3, data.SupremeCV4, data.SupremeCV5, 
    data.SupremeCV6, data.SupremeCV7, data.SupremeCV8, data.SupremeCV9, 0]
    data.GList=[data.GCV1, data.GCV2, data.GCV3, data.GCV4, data.GCV5, data.GCV6, data.GCV7, data.GCV8, data.GCV9, 0]
    #make the list into a dictionary that I can call from
    data.AEDict = dict()
    data.AFDict = dict()
    data.NikeDict = dict()
    data.SupremeDict = dict()
    data.GDict = dict()
    data.AEDisDict = dict()
    data.AFDisDict = dict()
    data.NikeDisDict = dict()
    data.SupremeDisDict = dict()
    data.GDisDict = dict()
    createDict(data)
    resizeImage(data)

def mousePressed(event, data):
    #when the user start the app by clicking on a brand
    if data.hasStarted == False:
        if event.x > data.margin and event.x < data.margin+data.iconWidth and \
        event.y > data.margin and event.y < data.margin+data.iconHeight:
            print("Run American Eagle")
            data.hasStarted = True
            data.waitAE = True
            data.startWebcam = True
            data.runShirtMenu = True
        elif event.x > data.width-data.margin-data.iconWidth and \
        event.x < data.width-data.margin and event.y > data.margin and \
        event.y < data.margin+data.iconHeight:
            print("Run Abercrombie & Fitch")
            data.hasStarted = True
            data.waitAF = True
            data.startWebcam = True
            data.runShirtMenu = True
        elif event.x > data.margin and event.x < data.margin+data.iconWidth and \
        event.y > data.height-data.margin-data.iconHeight and \
        event.y < data.height-data.margin:
            print("Run Nike")
            data.hasStarted = True
            data.waitNike = True
            data.startWebcam = True
            data.runShirtMenu = True
        elif event.x > data.width-data.margin-data.iconWidth and event.x < data.width-data.margin \
        and event.y > data.height-data.margin-data.iconHeight and event.y < data.height-data.margin:
            print("Run Supreme")
            data.hasStarted = True
            data.waitSupreme = True
            data.startWebcam = True
            data.runShirtMenu = True
        #check mouse click to open help menu
        if data.runHelpMenu == False:
            if event.x > data.width/2-data.margin and event.x < data.width/2+data.margin and \
            event.y > data.height-data.margin*4/5 and event.y < data.height-data.margin/5:
                data.runHelpMenu = True
        #check mouse click to close help menu
        elif data.runHelpMenu:
            if event.x > data.width/2-data.margin and event.x < data.width/2+data.margin and \
            event.y > data.height-data.margin*4/5 and event.y < data.height-data.margin/5:
                data.runHelpMenu = False
    #check for mousePressed in clothes menu
    if data.runAE or data.runAF or data.runNike or data.runSupreme and data.runInfoMenu == False:
        findSelectedClothes(data, event.x, event.y)
        findHighLightedCell(data)
        if data.runShirtMenu:
            if event.x > data.width-data.menuMargin and event.x < data.width and \
            event.y > data.height/2-data.menuButtonHeight/2 and event.y < data.height/2+data.menuButtonHeight/2:
                data.runShirtMenu = False
                data.runGlassesMenu = True
        elif data.runGlassesMenu:
            if event.x > 0 and event.x < data.menuMargin and event.y > data.height/2-data.menuButtonHeight/2 \
            and event.y < data.height/2+data.menuButtonHeight/2:
                data.runShirtMenu = True
                data.runGlassesMenu = False
        #check for mouse click on return button
        if event.x > data.width-data.menuMargin*2 and event.x < data.width \
        and event.y > data.height-data.menuMargin and event.y < data.height:
            init(data)
    if data.runInfoMenu:
        if event.x > data.width-data.menuMargin*2 and event.x < data.width \
        and event.y > data.height-data.menuMargin and event.y < data.height:
            data.runInfoMenu = False

#runs OpenCV code with selected input when called
def runWebcam(data):
    if data.startWebcam:
        if data.runAE:
            runCV(data.AEDict[data.selectedShirt], data.GDict[data.selectedGlasses])
        elif data.runAF:
            runCV(data.AFDict[data.selectedShirt], data.GDict[data.selectedGlasses])
        elif data.runNike:
            runCV(data.NikeDict[data.selectedShirt], data.GDict[data.selectedGlasses])
        elif data.runSupreme:
            runCV(data.SupremeDict[data.selectedShirt], data.GDict[data.selectedGlasses])

def keyPressed(event, data):
    if data.hasStarted:
        #press r to restart
        if event.keysym == "r":
            print("Restart")
            init(data)
        #press s to start webcam
        elif event.keysym == "s":
            runWebcam(data)
        elif event.keysym == "i":
            data.runInfoMenu = True
        if data.runInfoMenu:
            if event.keysym == "b":
                data.runInfoMenu = False

def timerFired(data):
    if data.waitAE:
        data.timer += 1
        if data.timer % 2 == 0:
            data.runAE = True
    elif data.waitAF:
        data.timer += 1
        if data.timer % 2 == 0:
            data.runAF = True
    elif data.waitNike:
        data.timer += 1
        if data.timer % 2 == 0:
            data.runNike = True
    elif data.waitSupreme:
        data.timer += 1
        if data.timer % 2 == 0:
            data.runSupreme = True

#find which shirt and glasses are selected by mouse click
def findSelectedClothes(data, x, y):
    if x > data.menuMargin and x < data.menuMargin+data.menuCellWidth and \
    y > data.menuMargin*3 and y < data.menuMargin*3+data.menuCellHeight:
        if data.runShirtMenu:
            data.selectedShirt = 0
        elif data.runGlassesMenu:
            data.selectedGlasses = 0
    elif x > data.menuMargin+data.menuCellWidth and x < data.menuMargin+data.menuCellWidth*2 \
    and y > data.menuMargin*3 and y < data.menuMargin*3+data.menuCellHeight:
        if data.runShirtMenu:
            data.selectedShirt = 1
        elif data.runGlassesMenu:
            data.selectedGlasses = 1
    elif x > data.menuMargin+data.menuCellWidth*2 and x < data.menuMargin+data.menuCellWidth*3 \
    and y > data.menuMargin*3 and y < data.menuMargin*3+data.menuCellHeight:
        if data.runShirtMenu:
            data.selectedShirt = 2
        elif data.runGlassesMenu:
            data.selectedGlasses = 2
    elif x > data.menuMargin and x < data.menuMargin+data.menuCellWidth and \
    y > data.menuMargin*3+data.menuCellHeight and y < data.menuMargin*3+data.menuCellHeight*2:
        if data.runShirtMenu:
            data.selectedShirt = 3
        elif data.runGlassesMenu:
            data.selectedGlasses = 3
    elif x > data.menuMargin+data.menuCellWidth and x < data.menuMargin+data.menuCellWidth*2 \
    and y > data.menuMargin*3+data.menuCellHeight and y < data.menuMargin*3+data.menuCellHeight*2:
        if data.runShirtMenu:
            data.selectedShirt = 4
        elif data.runGlassesMenu:
            data.selectedGlasses = 4
    elif x > data.menuMargin+data.menuCellWidth*2 and x < data.menuMargin+data.menuCellWidth*3 \
    and y > data.menuMargin*3+data.menuCellHeight and y < data.menuMargin*3+data.menuCellHeight*2:
        if data.runShirtMenu:
            data.selectedShirt = 5
        elif data.runGlassesMenu:
            data.selectedGlasses = 5
    elif x > data.menuMargin and x < data.menuMargin+data.menuCellWidth and \
    y > data.menuMargin*3+data.menuCellHeight*2 and y < data.menuMargin*3+data.menuCellHeight*3:
        if data.runShirtMenu:
            data.selectedShirt = 6
        elif data.runGlassesMenu:
            data.selectedGlasses = 6
    elif x > data.menuMargin+data.menuCellWidth and x < data.menuMargin+data.menuCellWidth*2 \
    and y > data.menuMargin*3+data.menuCellHeight*2 and y < data.menuMargin*3+data.menuCellHeight*3:
        if data.runShirtMenu:
            data.selectedShirt = 7
        elif data.runGlassesMenu:
            data.selectedGlasses = 7
    elif x > data.menuMargin+data.menuCellWidth*2 and x < data.menuMargin+data.menuCellWidth*3 \
    and y > data.menuMargin*3+data.menuCellHeight*2 and y < data.menuMargin*3+data.menuCellHeight*3:
        if data.runShirtMenu:
            data.selectedShirt = 8
        elif data.runGlassesMenu:
            data.selectedGlasses = 8

#find where to draw the highlighted cell in both shirt and glasses menu
def findHighLightedCell(data):
    #shirt menu
    if data.selectedShirt == 0:
        data.highlightedShirtCell = (0, 0)
    elif data.selectedShirt == 1:
        data.highlightedShirtCell = (1, 0)
    elif data.selectedShirt == 2:
        data.highlightedShirtCell = (2, 0)
    elif data.selectedShirt == 3:
        data.highlightedShirtCell = (0, 1)
    elif data.selectedShirt == 4:
        data.highlightedShirtCell = (1, 1)
    elif data.selectedShirt == 5:
        data.highlightedShirtCell = (2, 1)
    elif data.selectedShirt == 6:
        data.highlightedShirtCell = (0, 2)
    elif data.selectedShirt == 7:
        data.highlightedShirtCell = (1, 2)
    elif data.selectedShirt == 8:
        data.highlightedShirtCell = (2, 2)
    #glasses menu
    if data.selectedGlasses == 0:
        data.highlightedGlassesCell = (0, 0)
    elif data.selectedGlasses == 1:
        data.highlightedGlassesCell = (1, 0)
    elif data.selectedGlasses == 2:
        data.highlightedGlassesCell = (2, 0)
    elif data.selectedGlasses == 3:
        data.highlightedGlassesCell = (0, 1)
    elif data.selectedGlasses == 4:
        data.highlightedGlassesCell = (1, 1)
    elif data.selectedGlasses == 5:
        data.highlightedGlassesCell = (2, 1)
    elif data.selectedGlasses == 6:
        data.highlightedGlassesCell = (0, 2)
    elif data.selectedGlasses == 7:
        data.highlightedGlassesCell = (1, 2)
    elif data.selectedGlasses == 8:
        data.highlightedGlassesCell = (2, 2)
    
#create a dictionary of pictures
def createDict(data):
    for i in range(len(data.AEList)):
        data.AEDict[i] = data.AEList[i]
        data.AFDict[i] = data.AFList[i]
        data.NikeDict[i] = data.NikeList[i]
        data.SupremeDict[i] = data.SupremeList[i]
        data.GDict[i] = data.GList[i]
    for j in range(len(data.AEDisList)):
        data.AEDisDict[j] = data.AEDisList[j]
        data.AFDisDict[j] = data.AFDisList[j]
        data.NikeDisDict[j] = data.NikeDisList[j]
        data.SupremeDisDict[j] = data.SupremeDisList[j]
        data.GDisDict[j] = data.GDisList[j]

#get color from rgb string
#SOURCE: 15-112 course website
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

#resize image to fit the icons
def resizeImage(data):
    #first enlarge the image by the size of the icon
    #then shrink the image by the size the original image
    data.AELogo = data.AELogo.zoom(int(data.iconWidth)//100, int(data.iconHeight)//100)
    data.AELogo = data.AELogo.subsample(data.AELogo.width()//100, data.AELogo.height()//100)
    data.AFLogo = data.AFLogo.zoom(int(data.iconWidth)//100, int(data.iconHeight)//100)
    data.AFLogo = data.AFLogo.subsample(data.AFLogo.width()//120, data.AFLogo.height()//120)
    data.NikeLogo = data.NikeLogo.zoom(int(data.iconWidth)//50, int(data.iconHeight)//50)
    data.NikeLogo = data.NikeLogo.subsample(data.NikeLogo.width()//120, data.NikeLogo.height()//120)
    data.SLogo = data.SLogo.zoom(int(data.iconWidth)//40, int(data.iconHeight)//40)
    data.SLogo = data.SLogo.subsample(data.SLogo.width()//120, data.SLogo.height()//120)

#use recursion to insert linebreaks in long urls
def linebreakURL(s):
    if len(s) < 20:
        return s
    else:
        return s[0:20] + "\n" + linebreakURL(s[20:])

#insert a line break after the fourth word in an item name
#item names are generally not that long so this is ok
def linebreakItemName(s):
    spaceCounter = 0
    for i in range(len(s)):
        if s[i] == " ":
            spaceCounter += 1
        if spaceCounter == 4:
            break
    if spaceCounter < 4:
        return s
    else:
        return s[:i] + "\n" + s[i:]

#draw the main menu
def drawScreen(canvas, data):
    #create the square icon backgrounds
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue", width=0)
    canvas.create_rectangle(data.margin, data.margin, 
        data.margin + data.iconWidth, data.margin + data.iconHeight, fill=data.AEBrown, width=0)
    canvas.create_rectangle(data.width-data.margin-data.iconWidth, data.margin,
        data.width-data.margin, data.margin+data.iconHeight, fill="White", width=0)
    canvas.create_rectangle(data.margin, data.height-data.margin-data.iconHeight,
        data.margin+data.iconWidth, data.height-data.margin, fill="White", width=0)
    canvas.create_rectangle(data.width-data.margin-data.iconWidth, data.height-data.margin-data.iconHeight,
        data.width-data.margin, data.height-data.margin, fill="Honeydew2", width=0)
    #create the logos for each brand
    canvas.create_image(data.margin+data.iconWidth/2, data.margin+data.iconHeight/2, 
        image=data.AELogo)
    canvas.create_image(data.width-data.margin-data.iconWidth/2, data.margin+data.iconHeight/2, 
        image=data.AFLogo)
    canvas.create_image(data.margin+data.iconWidth/2, data.height-data.margin-data.iconHeight/2,
        image=data.NikeLogo)
    canvas.create_image(data.width-data.margin-data.iconWidth/2, data.height-data.margin-data.iconHeight/2,
        image=data.SLogo)
    #create instruction texts
    canvas.create_text(data.width/2, data.margin/2, text="Welcome to 15-112 Virtual Closet!", 
    font="Verdana %d" % data.textSize, fill="lime green")
    canvas.create_text(data.width/2, data.height/2, text="Select a Brand to Begin", font="Verdana %d" % data.textSize, 
    fill="lime green")
    #create help menu button
    canvas.create_rectangle(data.width/2-data.margin, data.height-data.margin*4/5, data.width/2+data.margin,
    data.height-data.margin/5, fill="thistle3", width=0)
    canvas.create_text(data.width/2, data.height-data.margin/2, text="Help", font="Verdana 15", fill="SpringGreen4")

#draw the help menu
def drawHelpMenu(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue")
    canvas.create_text(data.width/2, data.margin, text="Help", font="Verdana 25", fill="lime green")
    canvas.create_text(data.width/2, data.height/2, 
    text="Click to select clothing \nPress S to start \nPress Q to quit webcam \nPress I for more information \nPress R to return to main menu", font="Verdana 20")
    canvas.create_rectangle(data.width/2-data.margin, data.height-data.margin*4/5, data.width/2+data.margin,
    data.height-data.margin/5, fill="thistle3", width=0)
    canvas.create_text(data.width/2, data.height-data.margin/2, text="Return", font="Verdana 15", fill="SpringGreen4")
    
#draw the menu background based on the color of the company
def drawMenuBoard(canvas, data, company):
    if company == "AE":
        background = data.AEBrown
    elif company == "AF":
        background = "White"
    elif company == "Nike":
        background = "White"
    elif company == "Supreme":
        background = "Honeydew2"
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue")
    for row in range(3):
        for col in range(3):
            canvas.create_rectangle(data.menuMargin+data.menuCellWidth*col,
            data.menuMargin*3+data.menuCellHeight*row,
            data.menuMargin+data.menuCellWidth*(col+1),
            data.menuMargin*3+data.menuCellHeight*(row+1), fill=background, width=5)
    canvas.create_text(data.width/2, data.menuMargin, text="What do you want to try?",
    font="Verdana %d" % data.textSize, fill="lime green")
    canvas.create_text(data.width/2, data.menuMargin*2, text="Click Arrow for More Options",
    font="Verdana %d" % int(data.textSize/1.7), fill="DarkSlateGray1")
    #draw a button to return to main menu
    canvas.create_rectangle(data.width-data.menuMargin*2, data.height-data.menuMargin, data.width, 
    data.height, fill="thistle3", width=0)
    canvas.create_text(data.width-data.menuMargin, data.height-data.menuMargin/2, text="Return", font="Verdana 10", 
    fill="SpringGreen4")     

#draw the buttons to switch between shirt and glasses menu
def drawMenuButton(canvas, data):
    if data.runShirtMenu and data.runInfoMenu == False:
        canvas.create_rectangle(data.width-data.menuMargin, data.height/2-data.menuButtonHeight/2,
        data.width, data.height/2+data.menuButtonHeight/2, fill="thistle3")
        canvas.create_image(data.width-data.menuMargin/2, data.height/2, image=data.rightArrow)
    elif data.runGlassesMenu and data.runInfoMenu == False:
        canvas.create_rectangle(0, data.height/2-data.menuButtonHeight/2, data.menuMargin,
        data.height/2+data.menuButtonHeight/2, fill="thistle3")
        canvas.create_image(data.menuMargin/2, data.height/2, image=data.leftArrow)
    
#draw a menu of American Eagle clothes
def drawAEClothes(canvas, data):
    canvas.create_image(data.menuMargin+data.menuCellWidth/2, data.menuMargin*3+data.menuCellHeight/2,
    image=data.AEDis1)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.AEDis2)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.AEDis3)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.AEDis4)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.AEDis5)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.AEDis6)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.AEDis7)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.AEDis8)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.AEDis9)

#draw a menu of Pacsun clothes
def drawAFClothes(canvas, data):
    canvas.create_image(data.menuMargin+data.menuCellWidth/2, data.menuMargin*3+data.menuCellHeight/2,
    image=data.AFDis1)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.AFDis2)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.AFDis3)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.AFDis4)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.AFDis5)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.AFDis6)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.AFDis7)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.AFDis8)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.AFDis9)

#draw a menu of J Crew clothes
def drawNikeClothes(canvas, data):
    canvas.create_image(data.menuMargin+data.menuCellWidth/2, data.menuMargin*3+data.menuCellHeight/2,
    image=data.NikeDis1)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.NikeDis2)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.NikeDis3)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.NikeDis4)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.NikeDis5)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.NikeDis6)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.NikeDis7)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.NikeDis8)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.NikeDis9)

#draw a menu of Scotch & Soda clothes
def drawSupremeClothes(canvas, data):
    canvas.create_image(data.menuMargin+data.menuCellWidth/2, data.menuMargin*3+data.menuCellHeight/2,
    image=data.SupremeDis1)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.SupremeDis2)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.SupremeDis3)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.SupremeDis4)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.SupremeDis5)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.SupremeDis6)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.SupremeDis7)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.SupremeDis8)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.SupremeDis9)

#draw a menu of glasses
def drawGlasses(canvas, data):
    canvas.create_image(data.menuMargin+data.menuCellWidth/2, data.menuMargin*3+data.menuCellHeight/2,
    image=data.GDis1)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.GDis2)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2, 
    data.menuMargin*3+data.menuCellHeight/2, image=data.GDis3)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.GDis4)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.GDis5)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight+data.menuCellHeight/2, image=data.GDis6)
    canvas.create_image(data.menuMargin+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.GDis7)
    canvas.create_image(data.menuMargin+data.menuCellWidth+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.GDis8)
    canvas.create_image(data.menuMargin+data.menuCellWidth*2+data.menuCellWidth/2,
    data.menuMargin*3+data.menuCellHeight*2+data.menuCellHeight/2, image=data.GDis9)

#highlight the cell being selected
def drawHighLightedCell(canvas, data):
    if data.runShirtMenu:
        if data.highlightedShirtCell != (3, 3):
            col, row = data.highlightedShirtCell
            canvas.create_rectangle(data.menuMargin+data.menuCellWidth*col,             
            data.menuMargin*3+data.menuCellHeight*row, data.menuMargin+data.menuCellWidth*(col+1),
            data.menuMargin*3+data.menuCellHeight*(row+1), outline="goldenrod2", width=5)
    elif data.runGlassesMenu:
        if data.highlightedGlassesCell != (3, 3):
            col, row = data.highlightedGlassesCell
            canvas.create_rectangle(data.menuMargin+data.menuCellWidth*col,             
            data.menuMargin*3+data.menuCellHeight*row, data.menuMargin+data.menuCellWidth*(col+1),
            data.menuMargin*3+data.menuCellHeight*(row+1), outline="goldenrod2", width=5)

#draw info screen on each item
def drawInfoScreen(canvas, data):
    #draw background and title
    canvas.create_rectangle(0, 0, data.width, data.height, fill="dark slate blue")
    canvas.create_text(data.width/2, data.margin/2, text="Want to learn more?", font="Verdana 20", fill="lime green")
    #draw a button to return to selection menu
    canvas.create_rectangle(data.width-data.menuMargin*2, data.height-data.menuMargin, data.width, 
    data.height, fill="thistle3", width=0)
    canvas.create_text(data.width-data.menuMargin, data.height-data.menuMargin/2, text="Return", font="Verdana 10", 
    fill="SpringGreen4")
    #draw info menu for shirts
    if data.runShirtMenu:
        if data.runAE:
            #small image of shirt
            canvas.create_image(data.width/4-data.margin/2, data.height/4, image=data.AEDisDict[data.selectedShirt])
            #item name
            canvas.create_text(data.width*14/21, data.height/4-data.height/20, 
            text=linebreakItemName(AEInfoDict[data.selectedShirt][0]), font="Verdana 12 bold", fill="Black")
            #price
            canvas.create_text(data.width*14/21, data.height/4+data.height/20, text=AEInfoDict[data.selectedShirt][1],
            font="Verdana 15", fill="SpringGreen4")
            #url
            canvas.create_text(data.width*3/4+data.margin/2, data.height/2+data.margin, 
            text="You can find this at:\n"+linebreakURL(AEInfoDict[data.selectedShirt][2]), font="Verdana 10", 
            fill="Black")
            #sizing chart
            canvas.create_image(data.width/3, data.height*3/4, image=data.AESizingChart)
        elif data.runAF:
            canvas.create_image(data.width/4-data.margin/2, data.height/4, image=data.AFDisDict[data.selectedShirt])
            canvas.create_text(data.width*14/21, data.height/4-data.height/20, 
            text=linebreakItemName(AFInfoDict[data.selectedShirt][0]), font="Verdana 12 bold", fill="Black")
            canvas.create_text(data.width*14/21, data.height/4+data.height/20, text=AFInfoDict[data.selectedShirt][1],
            font="Verdana 15", fill="SpringGreen4")
            canvas.create_text(data.width*3/4+data.margin/2, data.height/2+data.margin, 
            text="You can find this at:\n"+linebreakURL(AFInfoDict[data.selectedShirt][2]), font="Verdana 10", 
            fill="Black")
            canvas.create_image(data.width/3, data.height*3/4, image=data.AFSizingChart)
        elif data.runNike:
            canvas.create_image(data.width/4-data.margin/2, data.height/4, image=data.NikeDisDict[data.selectedShirt])
            canvas.create_text(data.width*14/21, data.height/4-data.height/20, 
            text=linebreakItemName(NikeInfoDict[data.selectedShirt][0]), font="Verdana 12 bold", fill="Black")
            canvas.create_text(data.width*14/21, data.height/4+data.height/20, text=NikeInfoDict[data.selectedShirt][1],
            font="Verdana 15", fill="SpringGreen4")
            canvas.create_text(data.width*3/4+data.margin/2, data.height/2+data.margin, 
            text="You can find this at:\n"+linebreakURL(NikeInfoDict[data.selectedShirt][2]), font="Verdana 10", 
            fill="Black")
            canvas.create_image(data.width/3, data.height*3/4, image=data.NikeSizingChart)
        elif data.runSupreme:
            canvas.create_image(data.width/4-data.margin/2, data.height/4, 
            image=data.SupremeDisDict[data.selectedShirt])
            canvas.create_text(data.width*14/21, data.height/4-data.height/20, 
            text=linebreakItemName(SupremeInfoDict[data.selectedShirt][0]), font="Verdana 12 bold", fill="Black")
            canvas.create_text(data.width*14/21, data.height/4+data.height/20, 
            text=SupremeInfoDict[data.selectedShirt][1], font="Verdana 15", fill="SpringGreen4")
            canvas.create_text(data.width*3/4+data.margin/2, data.height/2+data.margin, 
            text="You can find this at:\n"+linebreakURL(SupremeInfoDict[data.selectedShirt][2]), font="Verdana 10", 
            fill="Black")
            canvas.create_image(data.width/3, data.height*3/4, image=data.SupremeSizingChart)
    #draw info menu for glasses
    elif data.runGlassesMenu:
        logo = data.GLogoDict[GInfoDict[data.selectedGlasses][3]]
        canvas.create_image(data.width/4, data.height/4, image=data.GDisDict[data.selectedGlasses])
        canvas.create_text(data.width*14/21, data.height/4-data.height/20, 
        text=linebreakItemName(GInfoDict[data.selectedGlasses][0]), font="Verdana 12 bold", fill="Black")
        canvas.create_text(data.width*14/21, data.height/4+data.height/20, text=GInfoDict[data.selectedGlasses][1],
        font="Verdana 15", fill="SpringGreen4")
        canvas.create_text(data.width*3/4+data.margin/2, data.height/2+data.margin, 
        text="You can find this at:\n"+linebreakURL(GInfoDict[data.selectedGlasses][2]), font="Verdana 10", 
        fill="Black")
        #logo of glasses brand
        canvas.create_image(data.width/3, data.height*3/4-data.margin, image=logo)
    
def redrawAll(canvas, data):
    if data.hasStarted == False:
        drawScreen(canvas, data)
        if data.runHelpMenu:
            drawHelpMenu(canvas, data)
    else:
        if data.runAE:
            drawMenuBoard(canvas, data, "AE")
            if data.runShirtMenu:
                drawAEClothes(canvas, data)
            elif data.runGlassesMenu:
                drawGlasses(canvas,data)
        elif data.runAF:
            drawMenuBoard(canvas, data, "AF")
            if data.runShirtMenu:
                drawAFClothes(canvas, data)
            elif data.runGlassesMenu:
                drawGlasses(canvas, data)
        elif data.runNike:
            drawMenuBoard(canvas, data, "Nike")
            if data.runShirtMenu:
                drawNikeClothes(canvas, data)
            elif data.runGlassesMenu:
                drawGlasses(canvas, data)
        elif data.runSupreme:
            drawMenuBoard(canvas, data, "Supreme")
            if data.runShirtMenu:
                drawSupremeClothes(canvas, data)
            elif data.runGlassesMenu:
                drawGlasses(canvas, data)
        if data.runInfoMenu:
            drawInfoScreen(canvas, data)
        if data.runInfoMenu == False:
            drawHighLightedCell(canvas, data)
        drawMenuButton(canvas, data)

#from 15-112 course website
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