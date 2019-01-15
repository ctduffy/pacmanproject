# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    stackdfs = util.Stack() #defines queue(stack in this case) that will be used as base for search

    current = (problem.getStartState(), []) #variable that holds current node

    visited = [current[0]] #defines list that keeps track of places that have already been visited

    while not problem.isGoalState(current[0]): #while current node isn't goal
        successors = problem.getSuccessors(current[0]) #defines variable successors as the successors of the current node
        visited.append(current[0]) #adds the current node to visited

        for y in successors: #for each of the successors of the current node
            if not y[0] in visited: #if that node has not been visited
                copy = current[1][:] #copies the current current variable
                copy.append(y[1]) #appends the action it took to get there onto the list that contains all of the actions to get to the current place
                end =(y[0], copy) # makes variable end into the tuple that contains the location and the actions to get there
                stackdfs.push(end) #push the successor onto the stack
        current = stackdfs.pop() # makes new current the next node that must be visited
    return current[1] #returns the list of actions that need to be taken to reach the goal


    """
    

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
  


def breadthFirstSearch(problem):
    bfs = util.Queue()#defines queue(queue in this case) that will be used as base for search

    current = (problem.getStartState(), [])#variable that holds current node

    visited = [current[0]]#defines list that keeps track of places that have already been visited

    while not problem.isGoalState(current[0]):#while current node isn't goal
        successors = problem.getSuccessors(current[0])#defines variable successors as the successors of the current node
        visited.append(current[0])#adds the current node to visited

        for y in successors:#for each of the successors of the current node
            if not y[0] in visited: #if that node has not been visited
                copy = current[1][:]#copies the current current variable
                copy.append(y[1])#appends the action it took to get there onto the list that contains all of the actions to get to the current place
                end =(y[0], copy)# makes variable end into the tuple that contains the location and the actions to get there
                bfs.push(end)#push the successor onto the queue
        current = bfs.pop()# makes new current the next node that must be visited
    return current[1]#returns the list of actions that need to be taken to reach the goal

    """Search the shallowest nodes in the search tree first."""


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    ucs = util.PriorityQueue()#defines queue(priority queue in this case) that will be used as base for search

    current = (problem.getStartState(), [])#variable that holds current node

    visited = [current[0]]#defines list that keeps track of places that have already been visited

    while not problem.isGoalState(current[0]):#while current node isn't goal
        successors = problem.getSuccessors(current[0])#defines variable successors as the successors of the current node
        visited.append(current[0])#adds the current node to visited

        for y in successors:#for each of the successors of the current node
            if not y[0] in visited: #if that node has not been visited
                copy = current[1][:]#copies the current current variable
                copy.append(y[1])#appends the action it took to get there onto the list that contains all of the actions to get to the current place
                end =(y[0], copy)# makes variable end into the tuple that contains the location and the actions to get there
                ucs.push(end, problem.getCostOfActions(copy))#push the successor onto the queue with the cost of the action so that it can be prioritized in the queue
        current = ucs.pop()# makes new current the next node that must be visited
    return current[1]#returns the list of actions that need to be taken to reach the goal


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    astar = util.PriorityQueue()#defines queue(priority queue in this case) that will be used as base for search

    current = (problem.getStartState(), [])#variable that holds current node

    visited = [current[0]]#defines list that keeps track of places that have already been visited

    while not problem.isGoalState(current[0]):#while current node isn't goal
        successors = problem.getSuccessors(current[0])#defines variable successors as the successors of the current node
        visited.append(current[0])#adds the current node to visited

        for y in successors:#for each of the successors of the current node
            if not y[0] in visited: #if that node has not been visited
                copy = current[1][:]#copies the current current variable
                copy.append(y[1])#appends the action it took to get there onto the list that contains all of the actions to get to the current place
                end =(y[0], copy)# makes variable end into the tuple that contains the location and the actions to get there
                astar.push(end, (problem.getCostOfActions(copy) + heuristic(y[0], problem)))#push the successor onto the queue with the cost of the action so that it can be prioritized in the queue
        current = astar.pop()# makes new current the next node that must be visited
    return current[1]#returns the list of actions that need to be taken to reach the goal



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
