__author__ = 'Rajkumar Pillai'
"""
file: Countdown.py

Description:This program generates an expression which when evaluated is equal to the target value using random restart algorithm
"""
import random
from collections import defaultdict


# list of 100 1 digit number
randomNumbers = [5, 1, 7, 8, 5, 5, 6, 7, 0, 1, 9, 4, 6, 4, 2, 5, 9, 3, 3, 0, 5, 0, 3, 7, 9,
                 3, 2, 8, 8, 5, 8, 2, 0, 1, 2, 0, 4, 4, 7, 2, 5, 9, 8, 8, 1, 3, 1, 6, 9, 6,
                 0, 8, 3, 9, 8, 7, 3, 6, 2, 3, 7, 0, 7, 3, 1, 0, 2, 5, 7, 8, 6, 7, 2, 1, 6,
                 9, 7, 9, 6, 5, 7, 4, 6, 2, 3, 1, 2, 4, 1, 3, 6, 1, 6, 1, 3, 4, 0, 8, 6, 0]

# Dictionary to keep track of actual calculated value of each expression
dictionary={}

# The target value which is to be reached
target=0

# To keep track of no of random restart
iterationCounter=0

# To keep store the current state and it's child state along with it's value
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

def evaluate(expression):
    '''
    This function calculates the actual value of the expresssion as per arithmetic operation defined in given problem
    :param expression: The expression whose value is to be calculated
    :return: expression
    '''
    result =float(expression[0])
    for i in range(1,len(expression),2):
        op=expression[i]
        newNumber=float(expression[i+1])
        if op == '+':
            result= result + newNumber
        if op == '*':
            result = result * newNumber
        if op == '/':
            if newNumber != 0:
                result = result / newNumber
        if op == '-':
            result = result - newNumber
    #print("Expression is", expression,"Result is",result)
    return result

def swap(expression):
    '''
    This performs swapping of the numbers in the expression and connects an edge between expression and all swapped expressions along with
    the distance from target.
    :param expression: The expression on which swapping of numbers has to be done

    '''
    #print('<--------Performing swap------------------>')
    expr=list(expression)
    for i in range (0,len(expr)-2,2):
        expr=list(expression)
        for j in range (i+2,len(expr),2):
            expr = list(expression)
            temp=expr[i]
            expr[i]=expr[j]
            expr[j]=temp
            newExpression=''.join(expr)
            result=evaluate(newExpression)
            value = valueEvaluation(result)
            dictionary[newExpression]=value
            addEdge(tree,expression, newExpression)


def changeOp(expression):
    '''
    This function performs changing of operators at different position in the expression connects an edge between expression and all new expressions along with
    the distance from target.
    :param expression: The expression on which change of operators has to be done
    :return:
    '''

    #print('<--------Changing operator------------------>')
    nextExpression=expression
    setOfOperators='+-*/'
    for j in range(1, len(expression), 2):
      op=nextExpression[j]
      for i in range (0,len(setOfOperators)):
        if op != setOfOperators[i]:
            nextExpression = expression
            nextExpression=nextExpression.replace(op,setOfOperators[i],1)
            #print(newExpression,"new one")
            result=evaluate(nextExpression)
            value=valueEvaluation(result)
            dictionary[nextExpression]=value
            addEdge(tree, expression, nextExpression)
            #print("Next expression is", nextExpression)

def valueEvaluation(result):
        '''
        This function calculates the distance of calculated value of expression from target value
        :param result: The actual arithmetic value of expression
        :return:value: The value of expression from target value
        '''
        if result >= 0:
            if target > result:
                value = target - result
                return value
                # print("1st if",value)
            else:
                value = result - target
                return value
                # print("1st else", value)
        else:
            if target > result:
                value = target - result
                return value
                # print("2nd if", value)
            else:
                value = result - target
                return value
                # print("2nd else", value)


def generate():
    '''
    This function generates random expression
    :return: expression :   Random expression generated
    '''

    setOfOperations=['+','-','*','/']
    randomExpression=''
    randomNumbers = [5, 1, 7, 8, 5, 5, 6, 7, 0, 1, 9, 4, 6, 4, 2, 5, 9, 3, 3, 0, 5, 0, 3, 7, 9,
                     3, 2, 8, 8, 5, 8, 2, 0, 1, 2, 0, 4, 4, 7, 2, 5, 9, 8, 8, 1, 3, 1, 6, 9, 6,
                     0, 8, 3, 9, 8, 7, 3, 6, 2, 3, 7, 0, 7, 3, 1, 0, 2, 5, 7, 8, 6, 7, 2, 1, 6,
                     9, 7, 9, 6, 5, 7, 4, 6, 2, 3, 1, 2, 4, 1, 3, 6, 1, 6, 1, 3, 4, 0, 8, 6, 0]

    # Perform shuffling oflist of numbers
    random.shuffle(randomNumbers)
    #print(randomNumbers)
    j=0
    for i in range(0, 200):
        if (i % 2 == 0):
            #print(len(randomNumbers))
            randomExpression += str(randomNumbers[j])
            j=j+1

        elif i != 199:
            r = random.randint(0, 3)
            randomExpression += str(setOfOperations[r])
    #print(len(randomExpression))
    return randomExpression



def exploreNewstate(newState):
           '''
           This function is used to find all possible next state possible for the new state and if it does not have a best state than itself
           then it performs a random restart
           :param newState: The state which is to be explored
           :return:
           '''
           currentState=newState
           result = evaluate(newState)

           currentStateValue = valueEvaluation(result)

           changeOp(newState)
           swap(newState)

           newState = min(dictionary, key=dictionary.get)
           newStateValue = dictionary[newState]
           if (currentStateValue > newStateValue):
               print("Best state is : ", newState)
               print("The distance from target is:", newStateValue)
               exploreNewstate(newState)

           elif newStateValue==0:
                 print("The solution is ",newState)
                 return
           else:
               print("Over all Best is ",currentStateValue)
               global iterationCounter
               iterationCounter += 1
               print("<--------------RR iteration :", iterationCounter, " ------------------->")
               randomRestart()


def randomRestart():
    '''
    This function performs random restart operation by taking a random expression as a start state and then exploring it
    :return:
    '''
    expression = generate()
    result = evaluate(expression)
    # print(result)
    currentStateValue = valueEvaluation(result)
    print("S0  : ", expression)
    print("The distance from target is: ",currentStateValue)
    dictionary.clear()
    changeOp(expression)
    swap(expression)


    newState = min(dictionary, key=dictionary.get)
    newStateValue = dictionary[newState]
    # print("reached here",currentStateValue,newStateValue)
    if (currentStateValue > newStateValue):
        print("Best state is : ", newState)
        print("Distance form target is: ", newStateValue)
        exploreNewstate(newState)
    elif newStateValue == 0:
        print("The solution is ", newState)

    else:
        print("Over all Best is ", currentStateValue)
        global iterationCounter
        iterationCounter += 1
        print("<--------------RR iteration :", iterationCounter, " ------------------->")
        randomRestart()


def main():
    '''
    The main program which begins with a initial expression and finds a expression equal to target value
    :return:
    '''
    global target
    target=float(input("Enter the target value"))
    #expression='1+2*3-4'
    #expression='2+6/1+0-7+0*0*0+3/2-0+1-9/9+5*4*4-0+9-4*9*1+8/8-4*4-5-7+9+0-2-8-9-7/6*0*0-5+2*4*4/6-3-6+9+7+4/1*9*9/3*3+0-1+9-9*6*2-9-6/1+5*0+8*7-7+1*0*6-9/7-7+0-0/7-9-9+2+7+5/2+4-4*4/7-3-3-8/2+5+7*0-8+9+1*4/1*4-0+0'

    # Generating a initial expression
    expression=generate()
    print("Number set :",randomNumbers)
    print("Target is : ", target)
    print("S0 is : ", expression)

    result=evaluate(expression)
    #print(result)
    currentStateValue= valueEvaluation(result)
    print("Distance from target is: ", currentStateValue)

    changeOp(expression)
    swap(expression)


    newState=min(dictionary,key=dictionary.get)
    newStateValue=dictionary[newState]
    #print("reached here",currentStateValue,newStateValue)
    if (currentStateValue > newStateValue):
       print("Best state is:  ",newState)
       print("Distance from target is: ",newStateValue)
       exploreNewstate(newState)
    elif newStateValue == 0:
        print("The solution is:  ", newState)

    else:
        print("Over all Best is ", currentStateValue)
        global iterationCounter
        iterationCounter += 1
        print("<--------------RR iteration :", iterationCounter, " ------------------->")
        randomRestart()


if __name__== '__main__':
    main()
