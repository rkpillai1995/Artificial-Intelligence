__author__ = 'Rajkumar Pillai'
"""
Author: Rajkumar Lenin Pillai

Description:This program generates optimal paths for orienteering during different seasons and prints the path on the 
map and prints the  total path length in meters to the terminal
"""




from PIL import Image, ImageDraw
import math
from collections import defaultdict
import heapq

#Initialising dictionaries for the cost value to be evaluated for the pixel
Gndictionary = {}
Hndictionary = {}
Fndictionary = {}
Nodegndictionary={}


# Keeps the neighbours of pixels in dictonary
neighbourdictionary = defaultdict(list)

# Keeps the neighbours of pixels in dictonary used in different seasons
neighbourdictionaryseasons=defaultdict(list)



def addEdge(neighbourdictionary ,src, dest):
    '''
    Used to store the next possible pixels from the current pixel
    :param neighbourdictionary: The dictionary in which the neigbours of a pixel are to be stored
    :param src: Current Pixel
    :param dest: Next possible pixel
    '''
    neighbourdictionary[src].append(dest)


def addEdgeseaons(neighbourdictionaryseaons ,src, dest):
    '''
    Used to store the next possible pixels from the current pixel used in different seasons
    :param neighbourdictionaryseaons: The dictionary in which the neigbours of a pixel are to be stored
    :param src:  Current Pixel
    :param dest: Next possible pixel
    '''
    neighbourdictionaryseasons[src].append(dest)

def allneighbours():
    '''
    This function stores all possible pixels for the current pixel by moving in 4-directions
    '''
    for i in range(0,500):
        for j in range(0,395):
            CurrentPixel = str(i) + " " + str(j)
            x=i+1
            y=j
            if x>=0 and x < 500 and y>=0   and y <395:
                Pixel= str(x) + " " + str(y)
                addEdge(neighbourdictionary,CurrentPixel,Pixel)


            x = i - 1
            y = j
            if x >= 0 and x < 500 and y >= 0 and y < 395:
                Pixel = str(x) + " " + str(y)
                addEdge(neighbourdictionary,CurrentPixel,Pixel)



            x = i
            y = j+1
            if x >= 0 and x < 500 and y >= 0 and y < 395:
                Pixel = str(x) + " " + str(y)
                addEdge(neighbourdictionary,CurrentPixel,Pixel)

            x = i
            y = j-1
            if x >= 0 and x < 500 and y >= 0 and y < 395:
                Pixel = str(x) + " " + str(y)
                addEdge(neighbourdictionary,CurrentPixel,Pixel)

def allneighbourseasons():
    '''
    This function stores all possible pixels for the current pixel by moving in 4-directions used in different seasons.
    '''
    for i in range(0,395):
        for j in range(0,500):
            CurrentPixel = str(i) + " " + str(j)
            x=i+1
            y=j
            if x>=0 and x < 395 and y>=0   and y <500:
                Pixel= str(x) + " " + str(y)
                addEdgeseaons(neighbourdictionaryseasons,CurrentPixel,Pixel)


            x = i - 1
            y = j
            if x>=0 and x < 395 and y>=0   and y <500:
                Pixel = str(x) + " " + str(y)
                addEdgeseaons(neighbourdictionaryseasons,CurrentPixel,Pixel)

            x = i
            y = j+1
            if x>=0 and x < 395 and y>=0   and y <500:
                Pixel = str(x) + " " + str(y)
                addEdgeseaons(neighbourdictionaryseasons,CurrentPixel,Pixel)

            x = i
            y = j-1
            if x>=0 and x < 395 and y>=0   and y <500:
                Pixel = str(x) + " " + str(y)
                addEdgeseaons(neighbourdictionaryseasons,CurrentPixel,Pixel)

def WaterPixelneighbours(RGBArray):
    '''
    This function fins the land pixels that are next to water
    :param RGBArray: Array containing RGB value of image
    :return: landNexttowater: the list of pixels which are next to water pixels
    '''
    landNexttowater=[]
    for i in range(0,395):
        for j in range(0,500):
            if RGBArray[i][j]!="(205, 0, 101)":
                CurrentPixel = str(i) + " " + str(j)
                x=i-1
                y=j
                if x>=0 and x < 395 and y>=0   and y <500:
                    Pixel= str(x) + " " + str(y)
                    if RGBArray[x][y] == "(0, 0, 255)":
                        landNexttowater.append(CurrentPixel)

                x = i + 1
                y = j
                if x >= 0 and x < 395 and y >= 0 and y < 500:
                    Pixel = str(x) + " " + str(y)
                    # print("Pixel",CurrentPixel,"and",x,y)
                    # print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        landNexttowater.append(CurrentPixel)

                x = i
                y = j + 1
                if x >= 0 and x < 395 and y >= 0 and y < 500:
                    Pixel = str(x) + " " + str(y)
                    # print("Pixel",CurrentPixel,"and",x,y)
                    # print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        landNexttowater.append(CurrentPixel)

                x = i
                y = j - 1
                if x >= 0 and x < 395 and y >= 0 and y < 500:
                    Pixel = str(x) + " " + str(y)
                    # print("Pixel",CurrentPixel,"and",x,y)
                    # print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        landNexttowater.append(CurrentPixel)



    return landNexttowater

def BFS_for_winter(wateredges,RGBArray):
    '''
    This function performs BFS search staring from pixels next to water surface and moving 7 pixels towards water
    :param wateredges: The list which contains pixels next to water which are non-water pixels
    :param RGBArray: Array containing RGB value of image
    :return: Allwateredges: The list that returns the list of pixels which form ice in winter and which are 7 pixels from land
    '''

    Queue = []
    Queue=Queue+wateredges # Initialize queue with the list of non-water pixels near to water
    # The predecessor dictionary maps temp node to it's immediate predecessor which can used to keep track
    # of visited nodes as well as to find the path
    im = Image.open('terrain.png')

    predecssor = {}
    predecssor[wateredges[0]] = None
    nextwateredges=[]
    Allwateredges=[]
    depth=0
    while len(Queue) > 0:

        temp = Queue.pop(0)

        if wateredges[(len(wateredges))-1] not in Queue:
            depth=depth+1
            wateredges=[]
            wateredges=wateredges+nextwateredges
            nextwateredges=[]


        if depth >= 7:
            break

        for neighbour in neighbourdictionaryseasons[temp]:


            if neighbour not in predecssor:
               x,y=readPixel(neighbour)

               if RGBArray[x][y] == "(0, 0, 255)" :
                predecssor[neighbour] = temp
                Queue.append(neighbour)
                nextwateredges.append(neighbour)
                Allwateredges.append(neighbour)

    return Allwateredges


def gofn(ParentPixel, CurrentPixel,ElevationArray,RGBArray,season):
        '''
        This function inserts the gn value of node in a dictionary
        :param ParentPixel: The parent of the current node
        :param CurrentPixel: The current node which is to be evaluated
        :param ElevationArray: The array which contains elevation correspong to pixels
        :param RGBArray: Array containing RGB value of image
        :param season: To keep track of different season of year
        :return: Total Gn value of node
        '''

        x1,y1=readPixel(ParentPixel)
        x2,y2=readPixel(CurrentPixel)

        parentgn = Gndictionary[ParentPixel]
        operationType="gn"
        gn=calculatedistance(x1,y1,x2,y2,ElevationArray,RGBArray,operationType,season)
        Nodegndictionary[CurrentPixel]=gn
        return gn + parentgn


def calculatedistance(x1,y1,x2,y2,ElevationArray,RGBArray,operationType,season):
    '''
    This function is the heuristic function which uses euclidean distance to evaluate the cost of reaching a node
    :param x1: x-cordinate of Parent pixel
    :param y1: y-cordinate of parent pixel
    :param x2: x-cordinate of current pixel
    :param y2: y-cordinate of current pixel
    :param ElevationArray: The array which conatains elevation correspoding to pixels
    :param RGBArray: Array containing RGB value of image
    :param operationType: To know whether gn or fn is to be calculated
    :param season: To keep track of different season of year
    :return: result: returns the gn or fn value
    '''
    if operationType=="gn":
        rgbValue = RGBArray[x2][y2]
        speed = typeOfTerrain(rgbValue,season)
        result=math.sqrt(  (( (x1-x2)*10.29)**2) + (((y1-y2)*7.55)**2)      +((ElevationArray[x1][y1] -ElevationArray[x2][y2])**2)                 )/speed


    if operationType == "hn":
        result=math.sqrt(  (((x1-x2)*10.29)**2) + (((y1-y2)*7.55)**2)      +((ElevationArray[x1][y1] -ElevationArray[x2][y2])**2)                     )/350

    return result

def hpirmeofn(hprimen, targetPixel,ElevationArray,RGBArray,season):
    '''
    Calcualtes the heuristic distance from each pixel to the goal pixel in  image
    :param hprimen: Array used to store the heuristic distance
    :param targetPixel: The goal pixel which is to reached
    :param ElevationArray: The array which contains elevation correspong to pixels
    :param RGBArray: Array containing RGB value of image
    :param season: To keep track of different season of year
    :return: hprimen
    '''
    x = targetPixel[0:4]
    y = targetPixel[4:7]
    x_target = int(x)
    y_target = int(y)
    operationType = "hn"

    for i in range(0, 500):
        for j in range(0, 395):
            hprimen[i][j] =   calculatedistance(x_target,y_target,i,j,ElevationArray,RGBArray,operationType,season)

    return hprimen

def readPixel(CurrentPixel):
    '''
    This function is used to seperate the x and y cordiante which are in string format
    :param CurrentPixel: The string from which x and y co-ordinate is to  be specified
    :return: x_curren : x-cordinate of pixel
    :return: y_current : y-cordinate of pixel
    '''
    position = CurrentPixel.find(" ")
    x = CurrentPixel[0:position]
    y = CurrentPixel[position:len(CurrentPixel)]
    x_current = int(x)
    y_current = int(y)


    return x_current,y_current

def elevation():
    '''
    The function which reads elevation file and stores the elevation value of pixel in a array
    :return: elevation: 2-D Array containing elevation value of pixel
    '''
    filename = "elevation.txt"
    ElevationList = []
    with open(filename) as f:
        for line in f:
            for ElevatiomNumbers in line.split():
                ElevationList.append(ElevatiomNumbers)

    rows = 500
    columns = 395

    elevation = [[0] * columns for i in range(rows)]
    p = 0
    q = 0
    for i in range(0, 200000, 400):
        for j in range(i, i + 395):
            elevation[p][q] = float(ElevationList[j])
            q = q + 1
        p = p + 1
        q = 0
    return elevation

def astarsearch(neighbourdictionary,CurrentPixel,targetPixel,hprimen,ElevationArray,RGBArray,season):
        '''
        This function performs the a* search on the input map with the start and goal nodes provided
        :param neighbourdictionary:  The dictionary which conatins the neighbour of each pixel
        :param CurrentPixel: The start pixel
        :param targetPixel: The goal pixel
        :param hprimen: The heuristic distance array of each pixel
        :param ElevationArray: The array which contains elevation correspong to pixels
        :param RGBArray:  Array containing RGB value of image
        :param season: To keep track of different season of year
        :return: pathfromstart: The list conatining path from start to goal
        '''

        heap = []
        heapq.heappush(heap, (0,CurrentPixel))  #  heapq which is used as a priority queue
        pathfromstart = {}                      #   Used to keep track of path from start Pixel
        TotalgnValue = {}                       #   Used to store the Gn value of node
        pathfromstart[CurrentPixel] = None
        TotalgnValue[CurrentPixel] = 0

        while len(heap)>0:

            Poppedelement = heapq.heappop(heap)
            current = Poppedelement[1]

            if current == targetPixel:
                break
            for childNode in neighbourdictionary[current]:
                Gndictionary[childNode]=gofn(current,childNode,ElevationArray,RGBArray,season)
                gnvalueofnode = Gndictionary[current] + Gndictionary[childNode]
                if childNode not in TotalgnValue or gnvalueofnode < TotalgnValue[childNode]:
                    TotalgnValue[childNode] = gnvalueofnode
                    x,y=readPixel(childNode)
                    hprimeofnValue = hprimen[x][y]
                    hn = hprimeofnValue
                    fn = gnvalueofnode + hn
                    heapq.heappush(heap, (fn, childNode))
                    pathfromstart[childNode] = current

        return pathfromstart


def reconstruct_path(pathfromstart, start, end):
    '''
    This function returns the path from start to end
    :param pathfromstart: The list conatining path from start to goal
    :param start: Starting Pixel
    :param end:  Goal Pixel
    :return: path: The path from start to goal
    '''
    currentNode = end
    path = []
    while currentNode != start:
        path.append(currentNode)
        currentNode = pathfromstart[currentNode]
    path.append(start)
    return path

def rgb_array(filename):
    '''
    The array that stores rgb value of image
    :param filename: The filename of image
    :return: rgbArray: The 2-D array containing the rgb value of image
    '''
    im = Image.open(filename)
    rgbIm = im.convert('RGB')
    rows = 500
    columns = 395
    rgb_array = [[0] * rows for i in range(columns)]
    pix = rgbIm.load()
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            rgb_array[x][y] = str(pix[x, y])

    #print(rgb_array[179][438])
    return rgb_array


def typeOfTerrain(rgbValue,season):
    '''
    This function assigns the speed for different type of terrain type
    :param rgbValue: rgbValue of image
    :param season: To keep track of different season of year
    :return: speedfactor: It is numerical speed constant assumed in each terrain
    '''
    if rgbValue == "(248, 148, 18)":
        speedfactor = 240


    elif rgbValue == "(255, 192, 0)":
        speedfactor =   150

    elif rgbValue == "(255, 255, 255)":

        if season=="fall":
            speedfactor =   60
        else:
            speedfactor = 120

    elif rgbValue == "(2, 208, 60)":
        speedfactor =   80

    elif rgbValue == "(2, 136, 40)":
        speedfactor =   20


    elif rgbValue == "(5, 73, 24)":
        speedfactor = 1

    elif rgbValue == "(0, 0, 255)":
        speedfactor = 1

    elif rgbValue == "(71, 51, 3)":
        speedfactor = 350

    elif rgbValue == "(0, 0, 0)":
        speedfactor = 20

    elif rgbValue == "(205, 0, 101)":
        speedfactor = 1

    elif rgbValue == "(0, 255, 255)":
        speedfactor = 170
    elif rgbValue == "(133, 99, 99)":
        speedfactor = 1
    return speedfactor

def BFS_mud(wateredges,RGBArray,ElevationArray):
    '''
    This function performs BFS search staring from water  pixels next to land surface and moving 15 pixels towards land
    and taking the corresponding elevation into account
    :param wateredges: The list which contains water pixels
    :param RGBArray: Array containing RGB value of image
    :param ElevationArray: The array which conatains elevation correspoding to pixels
    :return: Allwateredges: The list that contains the mud pixels
    '''


    Queue = []
    Queue = Queue + wateredges  # Initialize queue with the water

    # The predecessor dictionary maps temp pixel to it's immediate predecessor which can used to keep track
    # of visited nodes as well as to find the path

    predecssor = {}
    predecssor[wateredges[0]] = None
    nextwateredges = []
    Allwateredges = []
    depth = 0
    while len(Queue) > 0:

        temp = Queue.pop(0)

        if wateredges[(len(wateredges)) - 1] not in Queue:
            depth = depth + 1
            wateredges = []
            wateredges = wateredges + nextwateredges
            nextwateredges = []

        if depth >= 15:
            break

        for neighbour in neighbourdictionaryseasons[temp]:

            if neighbour not in predecssor:
                x, y = readPixel(neighbour)
                x1,y1=readPixel(temp)
                if RGBArray[x][y] == "(0, 0, 255)" and abs(ElevationArray[y1][x1]-ElevationArray[y][x]) <1.0:
                    predecssor[neighbour] = temp
                    Queue.append(neighbour)
                    nextwateredges.append(neighbour)
                    Allwateredges.append(neighbour)

    return Allwateredges


def waterPixels(RGBArray):
    '''
    This function finds all water pixels in image
    :param RGBArray: Array containing RGB value of image
    :return: waterpixelImage: The list of water pixels in image
    '''
    waterpixelinImage=[]
    for i in range(0,395):
        for j in range(0,500):
            if RGBArray[i][j]!="(205, 0, 101)":
                CurrentPixel = str(i) + " " + str(j)
                x=i-1
                y=j
                if x>=0 and x < 395 and y>=0   and y <500:
                    Pixel= str(x) + " " + str(y)
                    #print("Pixel",CurrentPixel,"and",x,y)
                    #print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        waterpixelinImage.append(Pixel)

                x = i + 1
                y = j
                if x >= 0 and x < 395 and y >= 0 and y < 500:
                    Pixel = str(x) + " " + str(y)
                    # print("Pixel",CurrentPixel,"and",x,y)
                    # print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        waterpixelinImage.append(Pixel)

                x = i
                y = j + 1
                if x >= 0 and x < 395 and y >= 0 and y < 500:
                    Pixel = str(x) + " " + str(y)
                    # print("Pixel",CurrentPixel,"and",x,y)
                    # print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        waterpixelinImage.append(Pixel)

                x = i
                y = j - 1
                if x >= 0 and x < 395 and y >= 0 and y < 500:
                    Pixel = str(x) + " " + str(y)
                    # print("Pixel",CurrentPixel,"and",x,y)
                    # print(RGBArray[x][y])
                    if RGBArray[x][y] == "(0, 0, 255)":
                        waterpixelinImage.append(Pixel)



    return waterpixelinImage

def showImage(filename,path):
    '''
    Used to output the image with path on screen
    :param filename: The file on which path is to be displayed
    :param path: Optimal path between points
    '''
    im = Image.open(filename)
    draw = ImageDraw.Draw(im)
    newImagePath = 'new.png'
    for item in path:
        x_new, y_new = readPixel(item)
        draw.point((x_new, y_new), fill=(255, 0, 0))
    im.save(newImagePath, 'png')
    im.show(newImagePath + 'new.png')


def summer(Imagefilename,Allpoints,hprimen,ElevationArray,season):
    '''
    The function which which finds optimal path using a* search in summer
    :param Imagefilename: Filename of the image file
    :param Allpoints: All points that are to be visited
    :param hprimen: The Array used to store the heuristic distance
    :param ElevationArray: The array which conatains elevation correspoding to pixels
    :param season: To keep track of different season of year
    '''
    RGBArray = rgb_array(Imagefilename)
    path = []
    for i in range(0, len(Allpoints) - 1):
        CurrentPixel = Allpoints[i]
        targetPixel = Allpoints[i + 1]
        a = astarsearch(neighbourdictionary, CurrentPixel, targetPixel, hprimen, ElevationArray, RGBArray,season)
        Currentpath = reconstruct_path(a, CurrentPixel, targetPixel)
        path = path + Currentpath
    print("Total-Path-length",Gndictionary[Allpoints[len(Allpoints)-1]],"meters")
    showImage(Imagefilename, path)

def winter(Imagefilename,Allpoints,hprimen,ElevationArray,RGBArray,season):
    '''
    The function which which finds optimal path using a* search in winter
    :param Imagefilename: Filename of the image file
    :param Allpoints: All points that are to be visited
    :param hprimen: The Array used to store the heuristic distance
    :param ElevationArray: The array which conatains elevation correspoding to pixels
    :param RGBArray: Array containing RGB value of image
    :param season: To keep track of different season of year
    '''
    allneighbourseasons()
    landNexttoWater = WaterPixelneighbours(RGBArray)
    edgeslist = list(set(landNexttoWater))
    path = []
    edgeslist = list(set(landNexttoWater))
    wateredges = []
    for i in range(0, len(edgeslist)):
        x_new, y_new = readPixel(edgeslist[i])
        if RGBArray[x_new][y_new] != "(0, 0, 255)":
            wateredges.append(edgeslist[i])

    RGBArray = rgb_array(Imagefilename)
    path = BFS_for_winter(wateredges, RGBArray)
    im = Image.open(Imagefilename)
    draw = ImageDraw.Draw(im)
    newImagePath = 'new.png'
    for item in path:
        x_new, y_new = readPixel(item)
        draw.point((x_new, y_new), fill=(0, 255, 255))
    im.save(newImagePath, 'png')
    # im.show(newImagePath,'png')

    RGBArray = rgb_array(newImagePath)
    path = []
    for i in range(0, len(Allpoints) - 1):
        CurrentPixel = Allpoints[i]
        targetPixel = Allpoints[i + 1]
        a = astarsearch(neighbourdictionary, CurrentPixel, targetPixel, hprimen, ElevationArray, RGBArray,season)
        Currentpath = reconstruct_path(a, CurrentPixel, targetPixel)
        path = path + Currentpath
    print("Total-Path-length",Gndictionary[Allpoints[len(Allpoints)-1]],"meters")
    showImage(newImagePath, path)

def spring(Imagefilename,Allpoints,hprimen,ElevationArray,RGBArray,season):
    '''
    The function which which finds optimal path using a* search in spring
    :param Imagefilename: Filename of the image file
    :param Allpoints: All points that are to be visited
    :param hprimen: The Array used to store the heuristic distance
    :param ElevationArray: The array which conatains elevation correspoding to pixels
    :param RGBArray: Array containing RGB value of image
    :param season: To keep track of different season of year
    '''
    allneighbourseasons()

    mudwaterPixels = WaterPixelneighbours(RGBArray)
    edgeslist = list(set(mudwaterPixels))
    wateredges = []
    for i in range(0, len(edgeslist)):
        x_new, y_new = readPixel(edgeslist[i])
        if RGBArray[x_new][y_new] != "(0, 0, 255)":
            wateredges.append(edgeslist[i])

    RGBArray = rgb_array(Imagefilename)

    muds = BFS_mud(wateredges, RGBArray, ElevationArray)

    im = Image.open(Imagefilename)
    draw = ImageDraw.Draw(im)
    for j in range(0, len(muds)):
        x_new, y_new = readPixel(muds[j])
        draw.point((x_new, y_new), fill=(133, 99, 99))

    newImagePath = 'new.png'
    im.save(newImagePath, 'png')
    # im.show(newImagePath + 'new.png')

    RGBArray = rgb_array(newImagePath)
    path = []
    for i in range(0, len(Allpoints) - 1):
        CurrentPixel = Allpoints[i]
        targetPixel = Allpoints[i + 1]
        a = astarsearch(neighbourdictionary, CurrentPixel, targetPixel, hprimen, ElevationArray, RGBArray, season)
        Currentpath = reconstruct_path(a, CurrentPixel, targetPixel)
        path = path + Currentpath
    print("Total-Path-length", Gndictionary[Allpoints[len(Allpoints) - 1]], "meters")
    showImage(newImagePath, path)

def fall(Imagefilename,Allpoints,hprimen,ElevationArray,RGBArray,season):
    '''
    The function which which finds optimal path using a* search in fall
    :param Imagefilename: Filename of the image file
    :param Allpoints: All points that are to be visited
    :param hprimen: The Array used to store the heuristic distance
    :param ElevationArray: The array which conatains elevation correspoding to pixels
    :param season: To keep track of different season of year
    '''
    path = []
    for i in range(0, len(Allpoints) - 1):
        CurrentPixel = Allpoints[i]
        targetPixel = Allpoints[i + 1]
        a = astarsearch(neighbourdictionary, CurrentPixel, targetPixel, hprimen, ElevationArray, RGBArray, season)
        Currentpath = reconstruct_path(a, CurrentPixel, targetPixel)
        path = path + Currentpath
    print("Total-Path-length", Gndictionary[Allpoints[len(Allpoints) - 1]], "meters")
    showImage(Imagefilename, path)


def main():
    '''
    The main program which accepts the season and the type of course

    :return: None
    '''
    filename=input("Please enter filename:'white.txt' or 'brown.txt' or 'red.txt': ")
    season=input("Please enter the season:'summer' or 'winter' or 'spring' or 'fall': ")
    #season="spring"
    #filename = "red.txt"

    points = ""
    with open(filename) as f:
        for line in f:
            points = points + line.strip(" ")
        Allpoints = points.split("\n")

    CurrentPixel = Allpoints[0]
    x,y=readPixel(CurrentPixel)

    targetPixel = Allpoints[1]

    # Initializing Manhattan distance towards goal '''
    rows = 500
    columns = 395
    hprimen = [[0] * columns for i in range(rows)]


    Imagefilename='terrain.png'
    ElevationArray = elevation()
    RGBArray = rgb_array(Imagefilename)
    hpirmeofn(hprimen, targetPixel, ElevationArray,RGBArray,season)


    ########''' Evaluating the start node
    gn = 0
    Gndictionary[CurrentPixel]= gn
    hprimeofnValue = hprimen[x][y]
    hn=hprimeofnValue
    Hndictionary[CurrentPixel] = hn
    Fndictionary[CurrentPixel] = gn+hn
    allneighbours()



    if season =="summer":
       summer(Imagefilename,Allpoints,hprimen,ElevationArray,season)

    if season =="winter":
        winter(Imagefilename, Allpoints, hprimen, ElevationArray, RGBArray,season)

    if season=="spring":
       spring(Imagefilename,Allpoints,hprimen,ElevationArray,RGBArray,season)

    if season=="fall":
        fall(Imagefilename, Allpoints, hprimen, ElevationArray, RGBArray, season)

if __name__ == '__main__':
    main()