__author__ = 'Rajkumar Pillai'
"""
file: WordLadder.py

Description:This program prints the shortest list of words that connects two dictionary words
by changing single letter in the word to any other later by generating graph of every word in dictionary and
then displaying the path using BFS search
"""

from collections import defaultdict

# Initializing graph
graph=defaultdict(list)

def addEdge(graph,src,dest):
    '''
    Add an edge between two vertices in graph
    :param graph: The graph in which edges and vertices are to be included
    :param src:   The source vertex from which edge is to be connected
    :param dest:  The destination vertex to which edge is to be connected
    :return: None
    '''
    graph[src].append(dest)

def generate_graph(startingword,list_of_words,endingword):
    '''
    Generates graph with each word in dictionary as vertex and adds edge between connected words
    :param startingword:   The word whose single letter would be changed.
    :param list_of_words:  All the words in the dictionary
    :param endingword:     The target word which is to be reached by sequence of changes from starting word
    :return:
    '''

    for i in range(0,len(list_of_words)):

     testword=list_of_words[i]     # Testword is the word  which would be modified at particular position by single letter
     eachword = list_of_words[i]
     for j in range (0,len(testword)):
       testword = list_of_words[i]
       testword=testword[:j]+"*"+testword[j+1:]      # The modified testword with * at particular position
       connected_word(startingword,testword,list_of_words,endingword,eachword)


def connected_word(startingword,testword,list_of_words,endingword,eachword):
    '''
    Checks if newWord must be included in the path form startingword to endingword and adds an edge between them in graph
    :param startingword: The word whose single letter would be changed.
    :param testword:     Testword is the word  which would be modified at particular position by single letter
    :param list_of_words:  All the words in the dictionary
    :param endingword:     The target word which is to be reached by sequence of changes from starting word
    :param eachword:        To temporarily store the word that is already accepted in the path from starting to endingword
    :return:
    '''
    position=testword.find("*")
    for i in range(96,122):
        x=chr(i+1)
        newWord=testword[:position]+x+testword[position+1:]
        newWord=comparison(newWord,list_of_words,eachword)
        if newWord != False:
          acceptableword=newWord

          # Edge is added between acceptable and eachWord in sequence already accepted
          addEdge(graph,eachword,acceptableword)



def comparison(newWord,list_of_words,eachword):
    '''
    To check if the newWord is a word in dictionary.
    :param newWord:       The word obtained by changing a single letter in startingword
    :param list_of_words: All the words in dictionary
    :param eachword:      To temporarily store the word that is already accepted in the path from starting to endingword
    :return:              newWord   if word is acceptable word i.e would be used to reach endingword
    :return:             False if the word is not a connecting word between start and end word
    '''
    for words in list_of_words:
        if newWord == words and newWord !=eachword:
            return newWord

    return False

def find_path(startingword,endingword):
    '''
    To find the shortest route from starting word to ending word using BFS search algorithm
    :param startingword: The word whose single letter would be changed.
    :param endingword:   The target word which is to be reached by sequence of changes from starting word
    :return: Path        The sequence of words that connect startingword and endingword
    '''

    Queue = []
    Queue.append(startingword)      #Initialize queue with the starting word


    #The predecessor dictionary maps temp word to it's immediate predecessor which can used to keep track
    #of visited nodes as well as to find the path

    predecssor = {}
    predecssor[startingword] = None


    while len(Queue)>0:
        temp=Queue.pop(0)
        if temp==endingword:
            break
        for neighbour in graph.get(temp):
            if neighbour not in predecssor:
                predecssor[neighbour] = temp
                Queue.append(neighbour)

    # If ending word is in predecessor a path is found
    if endingword in predecssor:
            path=[]
            temp=endingword
            while temp !=startingword:
                path.append(temp)
                temp = predecssor[temp]
            path.append(startingword)
            return path[::-1]
    else:
            return None


def main():
    '''
    The main program which accepts the starting word and ending word
    :return: None
    '''
    filename="dictionary.txt"
    words=""
    with open(filename) as f:
        for line in f:
            words=words+line.strip(" ")
        Allwords=words.split("\n")

    startingword=input("Please enter the starting word:")
    endingword=input("Please enter the ending word:")

    # To store all words of dictionary in a list which is equal to length of startingword
    list_of_words =[]
    for i in range(0,len(Allwords)):
        if(len(Allwords[i])) == len(startingword):
            list_of_words.append(Allwords[i])

    generate_graph(startingword,list_of_words,endingword)


    print("The shortest list of words that connects the two given words are:")

    # To display the path from starting to ending word
    path=find_path(startingword,endingword)
    print(*path,sep="--->")



if __name__ =='__main__':
    main()


'''

Sample output 1:
Please enter the starting word:cold
Please enter the ending word:warm
The shortest list of words that connects the two given words are:
cold--->cord--->word--->ward--->warm

Sample Output 2:
Please enter the starting word:small
Please enter the ending word:short
The shortest list of words that connects the two given words are:
small--->shall--->shale--->share--->shore--->short

Sample Output 3:
Please enter the starting word:fool
Please enter the ending word:sage
The shortest list of words that connects the two given words are:
fool--->pool--->poll--->pall--->pale--->sale--->sage

'''
