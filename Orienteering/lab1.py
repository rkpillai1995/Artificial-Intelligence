
from PIL import Image,ImageDraw
import  math
global hprimen
global rgb_array
global elevation
global visited
global StartingPoint
global openset
global closedset
global closedsetElementFn
dictionary={}
tempdictionary={}

#CurrentPixel=""
#dictionary.setdefault(CurrentPixel,[])

from collections import defaultdict



tree=defaultdict(list)


def addEdge(tree,src,dest):
    '''
    Add an edge between current state and next possible state
    :param tree: The tree in which edges and vertices are to be included between a expression and it's next possible expresssion
    :param src:   The current state from which edge is to be connected
    :param dest:  The child state to which edge is to be connected obtained by swap or changeOperator operation
    :return: None
    '''
    tree[src].append(dest)



def gofn(ParentPixel,x,y,CurrentPixel_elevation,direction,CurrentPixel):

    '''
    if (direction=="up-right"):
     gn=math.sqrt(105.8841+57.0025+pow(CurrentPixel_elevation,2))
     return gn
    if (direction=="up-left"):
     gn=math.sqrt(105.8841+57.0025+pow(CurrentPixel_elevation,2))
     return gn
    if (direction=="bottom-right"):
     gn=math.sqrt(105.8841+57.0025+pow(CurrentPixel_elevation,2))
     return gn
    if (direction=="bottom-left"):
     gn=math.sqrt(105.8841+57.0025+pow(CurrentPixel_elevation,2))
     return gn

    #treeValues=list(tree.values())
    #print(treeValues)
    #print(CurrentPixel)
    for k,v in tree.items():
            #if CurrentPixel == v[0] or CurrentPixel == k:
       print((v))
    '''

    #print("asf" ,ParentPixel)
    myDict_values = list(tempdictionary.values())
    #current_value = myDict_values[i][0]


    #print(parentgn)
    '''
    
    for k, v in tree.items():

        if CurrentPixel in v:
            print(CurrentPixel)
    '''
    if (direction=="up"):
     #parentgn=
     heuristicInfo = tempdictionary[ParentPixel]
     parentgn = heuristicInfo[0]
     gn=7.55
     return gn+parentgn
    if (direction=="right"):
     heuristicInfo = tempdictionary[ParentPixel]
     parentgn = heuristicInfo[0]
     gn=10.29
     return gn+parentgn
    if (direction=="bottom"):
     heuristicInfo = tempdictionary[ParentPixel]
     parentgn = heuristicInfo[0]
     gn=7.55
     return gn+parentgn
    if (direction=="left"):
     heuristicInfo = tempdictionary[ParentPixel]
     parentgn = heuristicInfo[0]
     gn=10.29
     return gn+parentgn




def typeOfTerrain(rgbValue,x,y):
    #print(len(rgbValue))

    if rgbValue=="(248,148,18) ":
        speedfactor=3.0
        steepness=float(elevation[x][y])
        return speedfactor*steepness

    if rgbValue == "(255,192,0) ":
        speedfactor = 4.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness

    if rgbValue == "(255,255,255) ":
        speedfactor = 5.0
        steepness = float(elevation[x][y])

        return speedfactor * steepness

    if rgbValue == "(2,208,60) ":
        speedfactor = 6.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness
    if rgbValue == "(2,136,40) ":
        speedfactor = 7.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness

    if rgbValue == "(5,73,24) ":
        speedfactor = 999.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness
    if rgbValue == "(0,0,255) ":
        speedfactor = 999.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness
    if rgbValue == "(71,51,3) ":
        speedfactor = 1.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness
    if rgbValue == "(0,0,0) ":
        speedfactor = 2.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness
    if rgbValue == "(205,0,101) ":
        speedfactor = 999.0
        steepness = float(elevation[x][y])
        return speedfactor * steepness

def NextPixel(CurrentPixel):

    #newPixel = min(dictionary, key=dictionary.get)


    CurrentPixelValue=tempdictionary[CurrentPixel]
    CurrentPixelfn=CurrentPixelValue[2]
    #print(CurrentPixelfn)
    myDict_values = list(tempdictionary.values())
    myDict_keys=list(tempdictionary.keys())
    minimumValue=999999999999999

    #print(myDict_values[4][0])
    #currentPixelFn=tempdictionary[CurrentPixel]
    #print(myDict_values[0][2])
    #print(currentPixelGn[0])
    #print()

    #for i in range(0,len(closedset)):
    #    closedsetElement = closedset[i]
    #    closedsetElementValue = tempdictionary[closedsetElement]
    #    print(closedsetElementValue)

    newPixel=""
    for i in range(0,len(myDict_keys)):
      current_value=myDict_values[i][2]
      #print("Current vale ",currentPixelFn[2])
      #print(closedsetElementFn)
      #if current_value != CurrentPixelfn and current_value not in closedsetElementFn:
      if current_value != CurrentPixelfn and current_value not in closedsetElementFn:
        minimumValue=min(minimumValue,current_value)
        #print("minimum Value ",minimumValue)
    #print("-------",myDict_values[0])
    #print([k for k, v in dictionary.items() if v[0] == minimumValue])
    for k, v in tempdictionary.items():
        if v[2] == minimumValue :
            newPixel=k

    dictionary.update(tempdictionary)

    '''
    print("1st Dictionary is :",dictionary)
    tempdictionary.clear()
    tempdictionary["hi"] = "hello"
    print("New temp dict",tempdictionary)
    dictionary.update(tempdictionary)
    print("New Dictionary is :", dictionary)
    '''
    #global closedsetElementFn

    #tempdictionary.clear()
    global closedset
    closedset.append(newPixel)
    #print(newPixel)
    closedsetElementValue = tempdictionary[newPixel]
    closedsetElementFn.append(closedsetElementValue[2])
    #print("Hello",type(closedsetElementFn))
    return  newPixel

def NextPossiblePixel(ParentPixel,x_current, y_current, elevation, direction):



      CurrentPixel=str(x_current)+" "+str(y_current)
      #print(closedset)
      if CurrentPixel not in closedset:
        #print(CurrentPixel)
        #dictionary[ParentPixel].append(CurrentPixel)
    # factor=0
    #treeKeys = list(tree.keys())
    # print(treeKeys)
    #if CurrentPixel not in treeKeys:
        #print("Inside Current",CurrentPixel)
        x, y = x_current, y_current
        Pixel_elevation = elevation[x][y]
        CurrentPixel_elevation = float(Pixel_elevation)
        gn = gofn(ParentPixel,x,y,CurrentPixel_elevation,direction,CurrentPixel)
        hprimeofn = hprimen[x][y]

        rgbValue= rgb_array[x][y]
        factor = typeOfTerrain(rgbValue,x,y)

        #print(type(rgbValue))
        hn=factor*hprimeofn
        tempdictionary[CurrentPixel] = [gn]
        tempdictionary[CurrentPixel].append(hn)
        fn=gn+hn
        tempdictionary[CurrentPixel].append(fn)
        global openset
        openset.append(CurrentPixel)
        #print("asf",openset)



def ExploreNewPixel(newPixel,elevation,targetPixel):

    while newPixel != targetPixel:


        CurrentPixel = newPixel
        ParentPixel=CurrentPixel
        x = CurrentPixel[0:4]
        y = CurrentPixel[4:7]
        x_current = int(x)
        y_current = int(y)
        # print(y_current)






        ############################
        NextPossiblePixel(ParentPixel,x_current + 1, y_current, elevation, direction="right")
        NextPossiblePixel(ParentPixel,x_current - 1, y_current, elevation, direction="left")
        NextPossiblePixel(ParentPixel,x_current, y_current + 1, elevation, direction="up")
        NextPossiblePixel(ParentPixel,x_current, y_current - 1, elevation, direction="bottom")
        '''
        NextPossiblePixel(x_current + 1, y_current - 1, elevation)
        NextPossiblePixel(x_current - 1, y_current - 1, elevation)
        NextPossiblePixel(x_current + 1, y_current + 1, elevation)
        NextPossiblePixel(x_current - 1, y_current + 1, elevation)
        '''
        print(tempdictionary)

        newPixel = NextPixel(CurrentPixel)
        print("New Pixel is: ", newPixel)
        if CurrentPixel !=newPixel:
            addEdge(tree, CurrentPixel, newPixel)
            #addEdge(tree, CurrentPixel, "asdasdsad")
        #print(tree)



        #return


def rgblist():

        im = Image.open('terrain.png')

        rgbIm=im.convert('RGB')
        pix=rgbIm.load()
        width,height=im.size
        #print(width,height)
        #print(pix[0,])
        #Wpixel_values = list(rgbIm.getdata())
        #print(pixel_values[])
        rows = 500
        columns = 395
        rgb_array = [[0] * columns for i in range(rows)]

        RGBValue=""
        for x in range(0,height):
            #print("Row number is :",x)

            for y in range(0,width):
                r,g,b =rgbIm.getpixel((y,x))
                RGBValue += "(" + str(r) + "," + str(g) + "," + str(b) + ") "
                rgb_array[x][y]=RGBValue
                #print("Pos(",x,")","(",y,")",rgb_array[x][y])
                RGBValue = ""
        return rgb_array




def hpirmeofn(hprimen,targetPixel):
    x = targetPixel[0:4]
    y = targetPixel[4:7]
    x_target = int(x)
    y_target = int(y)

    for i in range(0,500):
        for j in range(0,395):
            hprimen[i][j]=math.sqrt((x_target-i)**2+(y_target-j)**2)
    return hprimen


def main():
    filename = "elevation.txt"
    newImagePath = 'C:\\Users\\RAJKUMAR\\PycharmProjects\\Lab1\\new.png'
    '''
    words = ""
    with open(filename) as f:
        for line in f:
            words = words + line.strip(" ")
        Allwords = words.split("\n")
    #print(Allwords[0])
    '''


    ElevationList=[]
    with open(filename) as f:
        for line in f:
            for ElevatiomNumbers in line.split():
                ElevationList.append(ElevatiomNumbers)

    #print(ElevationList[0])

    rows=500
    columns=395
    global elevation
    elevation=[[0]*columns for i in range(rows)]
    #print(elevation)



    p=0
    q=0
    for i in range(0,200000,400):
        for j in range(i,i+395):
          elevation[p][q]=ElevationList[j]
          q=q+1
        p=p+1
        q=0


    #print(elevation[1][0])
    ########################################################




    #############################################################




    filename = "points.txt"

    points = ""
    with open(filename) as f:
        for line in f:
            points = points + line.strip(" ")
            #print(points)
        Allpoints = points.split("\n")


    CurrentPixel = Allpoints[0]
    #CurrentPixel = "230 327"
    global  StartingPoint
    StartingPoint=Allpoints[0]

    global openset
    openset = []

    global closedsetElementFn
    closedsetElementFn=[]


    global closedset
    closedset=[CurrentPixel]
    #print(openset)


    x = CurrentPixel[0:4]
    y = CurrentPixel[4:7]
    x_current = int(x)
    y_current = int(y)
    # print(y_current)


    Pixel_elevation = elevation[x_current][y_current]

    # dictionary[CurrentPixel]=[Pixel_elevation]




    #targetPixel = "247 350"
    targetPixel = Allpoints[1]
    rows = 500
    columns = 395
    global hprimen
    hprimen = [[0] * columns for i in range(rows)]

    hprimen=hpirmeofn(hprimen,targetPixel)
    #print("This is ",hprimen[241][355])
    #hn=hprimen[x_current][y_current]
    global rgb_array
    rgb_array=rgblist()

    CurrentPixel_elevation = float(Pixel_elevation)
    gn = 0
    hprimeofn = hprimen[x_current][y_current]

    rgbValue = rgb_array[x_current][y_current]
    factor = typeOfTerrain(rgbValue, x_current, y_current)

    # print(type(rgbValue))
    hn = factor * hprimeofn
    tempdictionary.setdefault(CurrentPixel, []).append(gn)
    tempdictionary.setdefault(CurrentPixel, []).append(hn)

    tempdictionary.setdefault(CurrentPixel, []).append(gn+hn)
    ParentPixel=CurrentPixel

    dictionary.setdefault(ParentPixel, [])

    closedsetElementValue = tempdictionary[CurrentPixel]
    closedsetElementFn.append(closedsetElementValue[2])

    ############################
    NextPossiblePixel(ParentPixel,x_current+1,y_current,elevation,direction="right")

    NextPossiblePixel(ParentPixel,x_current - 1, y_current, elevation, direction="left")
    NextPossiblePixel(ParentPixel,x_current, y_current + 1, elevation, direction="up")
    NextPossiblePixel(ParentPixel,x_current, y_current - 1, elevation, direction="bottom")
    '''
    NextPossiblePixel(x_current + 1, y_current - 1, elevation, direction="bottom-right")
    NextPossiblePixel(x_current - 1, y_current - 1, elevation, direction="bottom-left")
    NextPossiblePixel(x_current + 1, y_current + 1, elevation, direction="up-right")
    NextPossiblePixel(x_current - 1, y_current + 1, elevation, direction="up-left")
    '''
    print(tempdictionary)

    newPixel=NextPixel(CurrentPixel)
    print("New Pixel is: ",newPixel)
    '''
    x = newPixel[0:4]
    y = newPixel[4:7]
    x_new = int(x)
    y_new = int(y)
    '''
    addEdge(tree, CurrentPixel, newPixel)
    #addEdge(tree,CurrentPixel,"230 328")




    ExploreNewPixel(newPixel,elevation,targetPixel)

    #for i in range (2,len(Allpoints)):
    '''
    print("################################################Round1@#############################################################################################################################################")

    CurrentPixel = Allpoints[1]
    #CurrentPixel = "230 327"

    openset = []

    closedsetElementFn=[]


    closedset=[CurrentPixel]


    x = CurrentPixel[0:4]
    y = CurrentPixel[4:7]
    x_current = int(x)
    y_current = int(y)
    # print(y_current)


    Pixel_elevation = elevation[x_current][y_current]

    # dictionary[CurrentPixel]=[Pixel_elevation]




    #targetPixel = "247 350"
    targetPixel = Allpoints[2]


    CurrentPixel_elevation = float(Pixel_elevation)
    gn = 0
    hprimeofn = hprimen[x_current][y_current]

    rgbValue = rgb_array[x_current][y_current]
    factor = typeOfTerrain(rgbValue, x_current, y_current)

    # print(type(rgbValue))
    hn = factor * hprimeofn
    tempdictionary.setdefault(CurrentPixel, []).append(gn)
    tempdictionary.setdefault(CurrentPixel, []).append(hn)

    tempdictionary.setdefault(CurrentPixel, []).append(gn+hn)
    ParentPixel=CurrentPixel

    dictionary.setdefault(ParentPixel, [])

    closedsetElementValue = tempdictionary[CurrentPixel]
    closedsetElementFn.append(closedsetElementValue[2])

    ############################
    NextPossiblePixel(ParentPixel,x_current+1,y_current,elevation,direction="right")

    NextPossiblePixel(ParentPixel,x_current - 1, y_current, elevation, direction="left")
    NextPossiblePixel(ParentPixel,x_current, y_current + 1, elevation, direction="up")
    NextPossiblePixel(ParentPixel,x_current, y_current - 1, elevation, direction="bottom")
    '''
    #NextPossiblePixel(x_current + 1, y_current - 1, elevation, direction="bottom-right")
    #NextPossiblePixel(x_current - 1, y_current - 1, elevation, direction="bottom-left")
    #NextPossiblePixel(x_current + 1, y_current + 1, elevation, direction="up-right")
    #NextPossiblePixel(x_current - 1, y_current + 1, elevation, direction="up-left")
    '''
    print(tempdictionary)

    newPixel=NextPixel(CurrentPixel)
    print("New Pixel is: ",newPixel)
    '''
    x = newPixel[0:4]
    y = newPixel[4:7]
    x_new = int(x)
    y_new = int(y)
    '''
    addEdge(tree, CurrentPixel, newPixel)
    #addEdge(tree,CurrentPixel,"230 328")




    ExploreNewPixel(newPixel,elevation,targetPixel)
    '''''

    print("################################################Round222222222@#############################################################################################################################################")

    #'''
    im = Image.open('terrain.png')

    draw = ImageDraw.Draw(im)
    pix = im.load()
    #pix[x_new,y_new]=(255,0,0)
    treeKeys = list(tree.keys())
    #for i in range( len(closedset)-1,-1,-1):
    for i in range(0,len(closedset)):
        #print(closedset[i])

        newPixel=closedset[i]
        x = newPixel[0:4]
        y = newPixel[4:7]
        x_new = int(x)
        y_new = int(y)
        draw.point((x_new, y_new), fill=(255, 0, 0))
        im.save(newImagePath, 'png')
    im.show(newImagePath+'new.png')
    #print(dictionary)

    #print(tree)
    #'''
if __name__== '__main__':
      main()





