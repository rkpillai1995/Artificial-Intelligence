__author__ = 'Rajkumar Pillai'
"""
file: predict.py
CSCI-630:  Found of Intelligent Systems 
Author: Rajkumar Lenin Pillai

Description: This program uses the decision tree built from the training data and  gives the prediction 
for the language of sentences and stores in output file. 
"""
class Tree(object):
    '''
    Initialising the decision tree
    '''
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None




def readfile(filename):
    '''
    Reads the sentences of the file
    :param filename: The name of the file from which senetences are to be read
    :return: sentences: List of all sentences
    '''
    sentences=[]
    with open(filename) as textFile:
        for line in textFile:
            lines = line.split()
            sentences.append(lines[0:15])

    return sentences

def containsde(sentence):
    '''
    Checks whether the sentence contains the word de
    :param sentence: The sentence on which the checking needs to be done
    :return: result : True if the sentence contains de and False otherwise
    '''
    if "de".casefold() in sentence :
        # print(sentence)
        result = "True"
    else:
        result = "False"
    return result

def containsij(sentence):
    '''
    Checks is the substring ij is present in senetence
    :param sentence: The sentence on which the operation is performed
    :return: result :  True if sentence has words with ij as substring and False otherwise
    '''
    substringij = "ij"
    for i in range(0, len(sentence)):
        if sentence[i].find(substringij) == -1:
            # print(sentence)
            result = "False"

        else:
            result = "True"
            break
    return result

def noofes(sentence):
    '''
    Counts the no of e's present in given sentence
    :param sentence: The sentence on which the operation is performed
    :return: False if the no of e's is less than 13 and True otherwise
    '''
    ecounter = 0
    for i in range(0, len(sentence)):
        ecounter = ecounter + sentence[i].count('e')
    # print(ecounter)
    if ecounter <= 13:
        result = "False"
    else:
        result = "True"

    return result

def containshet(sentence):
    '''
    Checks if the sentence contains the word 'het'
    :param sentence: The sentence on which the checking needs to be done
    :return: result: True if the sentence contains het and False otherwise
    '''
    if  "het".casefold() in sentence:
        # print(sentence)
        result = "True"
    else:
        result = "False"
    return result

def containsvan(sentence):
    '''
    Checks if the word van is present in sentence
    :param sentence: The sentence on which the checking is performed
    :return: result : True if the sentence  has word van and False otherwise
    '''
    if  "van".casefold() in sentence:
        # print(sentence)
        result = "True"
    else:
        result = "False"
    return result

def containsoo(sentence):
    '''
    Checks is the substring oo is present in senetence
    :param sentence: The sentence on which the operation is performed
    :return: result :  True if sentence has words with oo as substring and False otherwise
    '''
    substringij = "oo"
    for i in range(0, len(sentence)):
        if sentence[i].find(substringij) == -1:
            # print(sentence)
            result = "False"

        else:
            result = "True"
            break
    return result

def containsee(sentence):
    '''
    Checks is the substring ee is present in senetence
    :param sentence: The sentence on which the operation is performed
    :return: result : True if sentence has words with ee as substring and False otherwise
    '''
    substringij = "ee"
    for i in range(0, len(sentence)):
        if sentence[i].find(substringij) == -1:
            # print(sentence)
            result = "False"

        else:
            result = "True"
            break
    return result


def evaluationofattribute(sentence):
    '''
    Popluates a list of all feautes for each sentence
    :param sentence: The sentences for which the features values are calculated
    :return: attributelist : The list of features for each senetence
    '''
    attributelist=[]
    #print(len(sentence))
    for i in range(0, len(sentence)):



        ############## -----Containsde call
        resultofde=containsde(sentence[i])


        ############## -----Containsij
        resultofij = containsij(sentence[i])

        ############## -----Noofe's
        resultofes = noofes(sentence[i])

        ############## -----Containshet call
        resultofhet = containshet(sentence[i])

        ############## -----Containsvan call
        resultofvan = containsvan(sentence[i])

        ############## -----Containsoo call
        resultofoo = containsoo(sentence[i])

        ############## -----Containsee call
        resultofee = containsee(sentence[i])

        ############## -----Calculation of attribute rows
        rowofattributevalues=[resultofde]+[resultofij]+[resultofvan]+[resultofoo]+[resultofee]+[resultofhet]+[resultofes]
        attributelist.append(rowofattributevalues)

    return attributelist

def modelaftertraining():

    '''
    Builds the decision tree learned fromt the trainng data
    :return:  The decision Tree nodes
    '''
    containsde = Tree()
    containsde.right = Tree()
    containsde.right.data = "nl"
    ##print(containsde.right.data)

    Noofij = Tree()
    Noofij.right = Tree()
    Noofij.right.data = "nl"

    containsvan = Tree()
    containsvan.right = Tree()
    containsvan.right.data = "nl"

    containsoo = Tree()
    containsoo.left = Tree()
    containsoo.left.data = "en"

    containsee = Tree()
    containsee.left = Tree()
    containsee.left.data = "en"

    containshet = Tree()
    containshet.right = Tree()
    containshet.right.data = "nl"

    Noofes = Tree()
    Noofes.right = Tree()
    Noofes.right.data = "en"
    Noofes.left = Tree()
    Noofes.left.data="en"

    return containsde,Noofij,containsvan,containsoo,containsee,containshet,Noofes

def checkattributefunction(Eachsentence):
    '''
    Predicts the type of language for each sentence
    :param Eachsentence: The sentence whose language is to be predicted
    :return: The label for the type of language
    '''
    containsde, Noofij, containsvan, containsoo, containsee, containshet, Noofes = modelaftertraining()

    for i in range(0,len(Eachsentence)):
        if Eachsentence[i]=="True":
            return containsde.right.data

        elif Eachsentence[i]=="False":

            if Eachsentence[i+1]=="True":
                return Noofij.right.data

            elif Eachsentence[i+1]=="False":

                if Eachsentence[i + 2] == "True":
                    return containsvan.right.data

                elif Eachsentence[i+2]=="False":

                     if Eachsentence[i+3] =="False":
                         return containsoo.left.data

                     elif Eachsentence[i+3] =="True":

                         if Eachsentence[i + 4] == "False":
                             return containsee.left.data

                         elif Eachsentence[i + 4] == "True":

                            if Eachsentence[i+5] == "True":
                                return containshet.right.data

                            elif Eachsentence[i+5] == "False":

                                 if Eachsentence[i+6] == "True":
                                     return Noofes.right.data
                                 elif Eachsentence[i + 6] == "False":
                                         return Noofes.left.data

def  thepredictfunction(attributelist):
    '''
    The function which performs prediction for all senetences
    :param attributelist: The feature values of each sentence
    :return: predictlist : The list with predictions for each sentence
    '''
    predictlist=[]
    for i in range(0,len(attributelist)):

        Eachsentence=attributelist[i]
        result=checkattributefunction(Eachsentence)
        predictlist.append(result)

    return predictlist

def main():
    '''
    The main program which runs the predict function and
    :return:
    '''
    testfilename=input("Please enter filename which conains the sentences:'test.txt' :")
    outputfilename=input("Please enter filename in which the predictions are to be stored :")

    # testfilename="test.txt"
    # outputfilename="output.txt"
    sentences=readfile(testfilename)
    attributelist=evaluationofattribute(sentences)

    predictlist=thepredictfunction(attributelist)
    for i in range(0,len(predictlist)):
        print(predictlist[i])


    with open(outputfilename, 'w') as file:
        for i in range(0, len(predictlist)):
           file.write(predictlist[i])
           file.write('\n')

    print("The output of predictions is stored in: ",outputfilename, "file")
if __name__=='__main__':
    main()