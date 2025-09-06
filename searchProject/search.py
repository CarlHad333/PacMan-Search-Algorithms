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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()   (5,5)
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())  false
    print "Start's successors:", problem.getSuccessors(problem.getStartState())   [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    """

    stack = util.Stack()
    start = problem.getStartState()
    marked = []
    stack.push((start, []))

    while not stack.isEmpty():
        sp = stack.pop()
        state = sp[0]
        actions = sp[1]
        if state not in marked:
            marked.append(state)
            if problem.isGoalState(state):
                return actions
            else:
                successors = problem.getSuccessors(state)
                for s in successors:
                    newactions = actions + [s[1]]
                    stack.push((s[0], newactions))
    return actions


# RightActionTinyMaze ['South','South','West','South','West','West','South','West']

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    start = problem.getStartState()
    queue.push((start, []))
    marked = []

    while not queue.isEmpty():
        qp = queue.pop()
        state = qp[0]
        actions = qp[1]
        if state not in marked:
            marked.append(state)
            if problem.isGoalState(state):
                return actions
            else:
                successors = problem.getSuccessors(state)
                for s in successors:
                    newactions = actions + [s[1]]
                    queue.push((s[0], newactions))
    return actions


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    priorityqueue = util.PriorityQueue()
    start = problem.getStartState()
    priorityqueue.push((start, [], 0), 0)
    marked = {}

    while not priorityqueue.isEmpty():
        pqp = priorityqueue.pop()
        state = pqp[0]
        actions = pqp[1]
        cost = pqp[2]
        if state not in marked:
            marked[state] = cost
            if problem.isGoalState(state):
                return actions
            else:
                successors = problem.getSuccessors(state)
                for s in successors:
                    newactions = actions + [s[1]]
                    newcost = cost + s[2]
                    priorityqueue.push((s[0], newactions, newcost), newcost)
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priorityqueue = util.PriorityQueue()
    start = problem.getStartState()
    priorityqueue.push((start, [], 0), 0)
    marked = []

    while not priorityqueue.isEmpty():
        pqp = priorityqueue.pop()
        state = pqp[0]
        actions = pqp[1]
        cost = pqp[2]
        if state not in marked:
            marked.append((state, cost))
            if problem.isGoalState(state):
                return actions
            else:
                successors = problem.getSuccessors(state)
                for s in successors:
                    newactions = actions + [s[1]]
                    newcost = cost + s[2]

                    explored = False
                    for m in marked:
                        markedstate = m[0]
                        markedcost = m[1]
                        if (s[0] == markedstate) and (newcost >= markedcost):
                            explored = True

                    if not explored:
                        priorityqueue.push((s[0], newactions, newcost), newcost + heuristic(s[0], problem))
                        marked.append((s[0], newcost))

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
