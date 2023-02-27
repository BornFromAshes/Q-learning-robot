# Q-learning-robot
In this project, we implemented iteration value and learning-Q. We first tested the agents in Gridworld, then applied them to a simulated robot controller (Crawler) and Pacman. Like previous projects, you can run the following command to debug and test the correctness of your algorithms:
```
python autograder.py
```
## Project Structure
- valueIterationAgents.py : An iteration value operator for solving known MDPs.
- qLearningAgents.py : Pacman and Gridworld, Crawler for Q-learnings
- analysis.py : A file to put your answers to the questions given in the project.
- mdp.py : Defines methods on common MDPs.
- learningAgent.py : Defines the ValueEstimationAgent and QLearningAgent base classes that your agents will extend.
- util.py : Utilities, including Counter.util, which is especially useful for learner-Qs.
- gridworld.py : Gridworld implementation.
- featureExtractors.py : Classes for extracting features in pairs (action, state) are used to approximate the learning-Q agent (in qlearningAgents.py).
- environment.py : Abstract class for general reinforcement learning environments used by gridworld.py.
- graphicsGridworldDisplay.py : Gridworld graphic display.
- graphicsUtils.py : graphic tools.
- textGridworldDisplay.py : Login for the Gridworld text interface.
- crawler.py : Crawler code and test. You run this but you don't edit it.
- graphicsCrawlerDisplay.py : GUI for crawler robot.
- autograder.py : Project auto grader.
- testParser.py : Parsing autocorrect tests and solution files.
- testClasses.py : General automatic test classes.
- test_cases/ : Folder containing different tests for each question.
- reinforcementTestClasses.py : Test classes.
## MDPs
Can run Gridworld in manual control mode, which uses directional keys:
```
python gridworld.py -m
```
