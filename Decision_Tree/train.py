__author__ = 'Rajkumar Pillai'
"""
file: train.py
CSCI-630:  Found of Intelligent Systems 
Author: Rajkumar Lenin Pillai

Description:This program generates performs training on the data set and using entropy and information gain method,
it generates a decision tree which can be used to predict the type of languages from given set of sentences.
"""




global encounter
global nlcounter
import math

#List of the attributenames
attribtenames=["containsde","No of ij","No of ees",'containshet',"containsvan","containsoo","containsee","language"]


def entropyofattribute(Pvalueone,Nvalueone,Pvaluetwo,Nvaluetwo,encounter,nlcounter):
    '''
     Calculates the entropy of the attribute
    :param Pvalueone: no of example with True value for en label
    :param Nvalueone: no of example with False value for en label
    :param Pvaluetwo: no of example with True value for nl label
    :param Nvaluetwo: no of example with False value for nl label
    :param encounter: Total no of example with True value for en label
    :param nlcounter: Total no of example with False value for nl label
    :return:
    '''
    result= ( (((Pvalueone+Nvalueone))/((encounter+nlcounter)))*(IPN(Pvalueone,Nvalueone)) ) + ( (((Pvaluetwo+Nvaluetwo))/((encounter+nlcounter)))*(IPN(Pvaluetwo,Nvaluetwo)) )

    return result


def IPN(Pvalue,Nvalue):
    '''
    Calculate the information gain for the attributes
    :param Pvalue: no of example with True value for the label
    :param Nvalue: no of example with False value for the label
    :return:
    '''
    if Pvalue == 0 and Nvalue!=0:

        answer =  - ((Nvalue / (Pvalue + Nvalue))) * math.log2((Nvalue / (Pvalue + Nvalue)))
    elif Nvalue == 0 and Pvalue!=0:
        answer = ((-Pvalue / (Pvalue + Nvalue))) * math.log2((Pvalue / (Pvalue + Nvalue)))

    elif Nvalue==0 and Pvalue == 0:
        answer=0


    else:
        answer= ((-Pvalue/(Pvalue+Nvalue)))* math.log2( (Pvalue/(Pvalue+Nvalue))) - ((Nvalue/(Pvalue+Nvalue)))* math.log2( (Nvalue/(Pvalue+Nvalue)))

    return answer

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

def endswithing(sentence):
    '''
    Checks if the word in senetences end with -ing i.e if the word has ing as prefix
    :param sentence: The sentence on which the checking is performed
    :return: result : True if the sentence  has word with suffix ing and False otherwise
    '''
    result = "False"

    for i in range(0, len(sentence)):
        if sentence[i].endswith('ing'):
            result = "True"
            break
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


def evaluationofattribute(sentence,attributelist,examplelist):
    '''
    Performs operation to find features of the 15 words in the senetence
    :param sentence: The sentence on which the operation is performed
    :param attributelist: The list with values of features for eachsentence
    :param examplelist: The list with target_attributes values
    :return:attributelist:
    '''

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
        rowofattributevalues=[resultofde]+[resultofij]+[resultofes]+[resultofhet]+[resultofvan]+[resultofoo]+[resultofee]+[examplelist[i]]
        attributelist.append(rowofattributevalues)


    attributelist.insert(0,["containsde","No of ij","No of ees","containshet","containsvan","containsoo","containsee","language"])

    return attributelist

def containssuffix(sentence):
    '''
    Checks if any word with suffix 'on' is present in senetence
    :param sentence: The sentence on which the operation is performed
    :return: result : True if the suffix is present and False otherwise
    '''
    result="False"
    for i in range(0, len(sentence)):
        if sentence[i].endswith('on'):
            # print(sentence)
            result = "True"
            break
        else:
            result = "False"
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


def containsprefix(sentence):
    '''
    Checks if the words have be-,er-,ge-,her-,ont-,ver- as prefix
    :param sentence: The sentence on which the operation is performed
    :return: result : True if sentence has words that prefix and False otherwise
    '''
    result = "False"
    for i in range(0, len(sentence)):
        if sentence[i].startswith("be") or sentence[i].startswith("er") or sentence[i].startswith(
                "ge") \
                or sentence[i].startswith("her") or sentence[i].startswith("ont") or sentence[
            i].startswith("ver") \
                or sentence[i].startswith("on"):
            #(print(sentence[i])
            result = "True"
            break
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




def gainofeachattribute(attributelist,attributeno):
    '''
    Calculates the Pvalue and Nvalue required to calcualte the gain of attribute
    :param attributelist: Contains the values of the features for the set of sentences
    :param attributeno: The attribute's position whose Pvalue and Nvalue is to be calculated
    :return:
    '''
    Truecounter = 0
    Falsecounter = 0
    Pvalueone = 0
    Nvalueone = 0
    Pvaluetwo = 0
    Nvaluetwo = 0
    for i in range(1, len(attributelist)-1):

        if attributelist[i][attributeno] == 'True':
            Truecounter = Truecounter + 1


            if attributelist[i][len(attributelist[1])-1] == '|en':
                Pvalueone = Pvalueone + 1
            else:
                Nvalueone = Nvalueone + 1

        elif attributelist[i][attributeno] == 'False':
            #print(attributelist[i][0])
            Falsecounter = Falsecounter + 1
            if attributelist[i][len(attributelist[1])-1] == '|nl':
                Pvaluetwo = Pvaluetwo + 1
            else:
                Nvaluetwo = Nvaluetwo + 1
    return Pvalueone, Nvalueone, Pvaluetwo, Nvaluetwo

def gaincalculation(attributelist,attributeno,gaindictionary,attributes):
    '''
    This function calculates the entropy for class and attributes and calculates the gain for the
    attribute and inserts the gain value and attribute name in the gain dictionary
    :param attributelist: The values of feautures for each sentence
    :param attributeno:  The attribute's position whose gain is to be calculated
    :param gaindictionary: The dictionary to store gain value of each attribute
    :param attributes: The list of attribute names
    :return: The attribute with maximum gain value
    '''


    Pvalueone, Nvalueone, Pvaluetwo, Nvaluetwo = gainofeachattribute(attributelist,attributeno)
    entropyforattribute = entropyofattribute(Pvalueone, Nvalueone, Pvaluetwo, Nvaluetwo,encounter,nlcounter)
    entropyforclass = IPN(encounter,nlcounter)
    gain=(entropyforclass- entropyforattribute)
    gaindictionary[attributes[attributeno]]=gain

    return max(gaindictionary, key=gaindictionary.get)

def pluralityvalue(examples):
    '''
    This function returns the label which the maximum no of examples refer to
    :param examples: The set of feature values of sentences
    :return: The label of the maximum examples
    '''
    encounter=0
    nlcounter=0
    for i in range(1,len(examples)):
        if examples[i][0] == '|en':
             encounter=encounter+1
        else:
            #global nlcounter
            nlcounter = nlcounter + 1

    result= max(encounter,nlcounter)
    if encounter > nlcounter:
        return '|en'
    else:
        return '|nl'


def decisiontree(examples,attributes,attributenooftarget):
    '''
    This function builds the decision tree in a recursive manner by spitting the attributes with maximum gain
    :param examples: The set of feature values of sentences
    :param attributes: The list of attribute names
    :param attributenooftarget: The position of the target attribute in examples
    :return: tree : The decision tree which is built
    '''

    examples=examples[:]
    targetvalues    = [sentencefeatures[len(sentencefeatures)-1] for sentencefeatures in examples]
    valuewithmaxoccurence=pluralityvalue(examples)
    if not examples or (len(attributes)-1)<=0:
        return valuewithmaxoccurence
    elif targetvalues.count(targetvalues[0]) == len(targetvalues):
        return targetvalues[0]
    else:
        gaindictionary={}
        attributewithmaxgain=""
        length=0
        for record in examples:
            length=len(record)
        for i in range(0, length-1):
             attributewithmaxgain = gaincalculation(examples, i, gaindictionary,attributes)
        no=attribtenames.index(attributewithmaxgain)
        attributenoofmaxgainattribute=attributes.index(attributewithmaxgain)
        tree={attributewithmaxgain:{}}

        for val in getuniquevalues(examples,attributenoofmaxgainattribute):

            subtree=decisiontree(splitexamples(examples, attributenoofmaxgainattribute, val),[values for values in attributes if values != attributewithmaxgain],len([attr for attr in attributes if attr != attributewithmaxgain])-1)

            tree[attributewithmaxgain][val] = subtree
    return tree





def getuniquevalues(examples,attributeno):
    '''
    Identifies all the values of that attribute uniqely
    :param examples: The set of feature values of sentences
    :param attributeno: The attribute's position whose gain is to be calculated
    :return: uniquevals: The set with the unique values for the attribute
    '''
    attributeValues = [rec[attributeno] for rec in examples]
    uniqueVals = set(attributeValues)
    return uniqueVals




def splitexamples(attributelist, attributeno, val):
    '''
    This function splits the attributelist based on the value of that attribute for the attributeno specified
    :param attributelist: The set of feature values of sentences
    :param attributeno: The attribute's position whose Pvalue and Nvalue is to be calculated
    :param val: True or False according to the attributes value
    :return: newattributelist: This is the new atributelist split on pararameters provoded
    '''
    newattributelist = []

    for i in range(1, len(attributelist)):
        if attributelist[i][attributeno] == str(val):
            temp = list(attributelist[i][:attributeno])
            temp.extend(attributelist[i][attributeno + 1:])
            newattributelist.append(temp)
    return newattributelist



def readdutchfile(dutchfilename):
    '''
    :param:dutchfilename:Name of the file with dutch sentences
    :return: dutchsamples : List of each sentence read from file
    '''
    with open(dutchfilename) as textFile:
        for line in textFile:
            # line=line.replace('.',"")
            lines = line.split()
            #print(lines[0:15])
    begin = 0
    end = 16
    dutchsamples=[]
    language='|nl'
    while True:

        if lines[begin:end] == []:
             break
        lines[begin:end] = [language] + lines[begin:end]
        dutchsamples.append(lines[begin:end])
        begin = begin + 16
        end = end + 16
    #for  i in range(0,len(dutchsamples)):
     ##print(dutchsamples[i])

    ##print(len(dutchsamples))
    return dutchsamples



def readenglishfile(englishfilename):
    '''
    :param:  englishfilename: Name of the file with english sentences
    :return: List of each sentence read from file
    '''
    with open(englishfilename) as textFile:
        for line in textFile:
            lines = line.split()
    begin = 0
    end = 16
    englishsamples=[]
    language='|en'
    while True:

        if lines[begin:end] == []:
             break
        lines[begin:end] = [language] + lines[begin:end]
        englishsamples.append(lines[begin:end])
        begin = begin + 16
        end = end + 16

    return englishsamples

def main():

    '''
    The main program which accepts the filenames for training set and finally builds a decision tree
    and the decision tree is present on the file hypothesisout.txt
    :return:
    '''
    dutchfilename=input("Please enter filename with dutch samples:'dutch.txt' :")
    englishfilename=input("Please enter filename with english samples:'english.txt' :")
    modelfilename=input("Please enter filename to store the decision tree:'hypothesisout.txt' :")
    # modelfilename='hypothesisout.txt'
    # dutchfilename='dutch.txt'
    # englishfilename='english.txt'
    englishsamples=readenglishfile(englishfilename)
    dutchsamples=readdutchfile(dutchfilename)

    ## Contains both the dutch and english samples
    Allsamples=englishsamples+dutchsamples


    global encounter
    global nlcounter
    encounter=0
    nlcounter=0
    attributelist = []
    examplelist=[]
    for i in range(0,len(Allsamples)):
        if Allsamples[i][0] == '|en':
             encounter=encounter+1
        else:
            nlcounter = nlcounter + 1

    for i in range(0, len(Allsamples)):
        if Allsamples[i][0] == '|en':
            examplelist.append('|en')
        else:
            examplelist.append('|nl')
    attributelist=evaluationofattribute(Allsamples, attributelist,examplelist)
    attributes = ['containsde', 'No of ij', 'No of ees','containshet','containsvan','containsoo','containsee','language']

    trees=decisiontree(attributelist,attributes,10)


    with open('hypothesisout.txt', 'w') as the_file:
        for k in trees:
            the_file.write(str(trees))
            the_file.write('\n')

    print("The decision tree built is stored in: ",modelfilename,"file")

if __name__ =='__main__':
    main()

