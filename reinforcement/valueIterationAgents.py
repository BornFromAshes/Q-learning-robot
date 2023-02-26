# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        """*** YOUR CODE HERE ***"""
        for i in range(self.iterations):
            temp_values = self.values.copy()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    continue
                temp_values[state] = self.computeQValueFromValues(state, self.computeActionFromValues(state))
            self.values = temp_values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        value = 0
        transition = self.mdp.getTransitionStatesAndProbs(state, action)
        for next_state, next_prob in transition:
            value += (self.mdp.getReward(state, action, next_state) + self.discount * self.getValue(
                next_state)) * next_prob
        return value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        actions = self.mdp.getPossibleActions(state)
        best_action = 0
        max_value = 0
        if len(actions) == 0:
            return None
        for action in actions:
            value = 0
            transition = self.mdp.getTransitionStatesAndProbs(state, action)
            for next_state, next_prob in transition:
                value += (self.mdp.getReward(state, action, next_state) + self.discount * self.getValue(
                    next_state)) * next_prob
            if value > max_value or max_value == 0:
                max_value = value
                best_action = action

        return best_action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        """*** YOUR CODE HERE ***"""
        states = self.mdp.getStates()

        for i in range(self.iterations):
            ix = i % len(states)

            if self.mdp.isTerminal(states[ix]):
                continue

            actions = self.mdp.getPossibleActions(states[ix])
            self.values[states[ix]]= max([self.getQValue(states[ix],action) for action in actions])





class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        """*** YOUR CODE HERE ***"""
        que = util.PriorityQueue()
        states = self.mdp.getStates()
        pred = {}

        for state in states:

            if self.mdp.isTerminal(state):
                continue

            for action in self.mdp.getPossibleActions(state):
                for next_state, next_prop in self.mdp.getTransitionStatesAndProbs(state, action):
                    if next_state in pred:
                        pred[next_state].add(state)
                    else:
                        pred[next_state] = {state}

        for state in states:

            if self.mdp.isTerminal(state):
                continue

            diff = abs(self.values[state] - max(
                [self.computeQValueFromValues(state, action) for action in self.mdp.getPossibleActions(state)]))

            que.update(state, -diff)

        for i in range(self.iterations):

            if que.isEmpty():
                break

            this_state = que.pop()
            if not self.mdp.isTerminal(this_state):
                self.values[this_state] = max(
                    [self.computeQValueFromValues(this_state, action) for action in self.mdp.getPossibleActions(this_state)])

            for pre in pred[this_state]:

                if self.mdp.isTerminal(pre):
                    continue

                diff = abs(self.values[pre] - max(
                    [self.computeQValueFromValues(pre, action) for action in self.mdp.getPossibleActions(pre)]))

                if diff > self.theta:
                    que.update(pre, -diff)

