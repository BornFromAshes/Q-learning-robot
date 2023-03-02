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
Note that when you press the top key, the agent moves north in only 80 % of the time.
This is the life of a Gridworld agent! <br>
You can control many aspects of simulation. A complete list of available options is displayed with the following command:
```
python gridworld.py -h
```
The default agent moves randomly:
```
python gridworld.py -g MazeGrid
```
Important: MDP GridWorld is such that you first need to enter a Terminal-Rere mode( dual boxes shown in the graphical user interface )and then special action "exit" before the end of the episode( in the actual terminal mode Called State_terminal, which is not shown in the graphical user interface ). If you run an episode manually, due to Rate Discount, your total recursive value may be less than expected( -d to change, 0.9 by default ). Similar to Pacman, positions are shown in Cartesian coordinates (y, x) and each arrangement is indexed with [x][y] so that "north" is to increase y. By default, most transnationals receive zero rewards. However, you can change this with the live reward option -r.
## Value Iteration
Using the equation below:
![image](https://user-images.githubusercontent.com/117355603/221672777-23c0280e-be22-4f39-a6e4-5d9c98ec1ab7.png)
We wrote a value iteration agent in ValueIterationAgent. The repetition factor is the value of an offline scheduler and not a reinforcement learning factor. The training option is related to the number of value iterations that must be executed in the initial programming phase (-i option.) ValueIterationAgent takes an MDP in the constructor and executes the value iteration for a specified number of iterations before the constructor finishes executing. Value iteration calculates k-step estimates of optimal values, Vk. In addition to implementing value iteration, the following methods are implemented for ValueIterationAgent using Vk:
- function computeActionFromValues which calculates the best action given the value function given by values.self.
- computeQValueFromValues function that takes the input (action, state) and calculates the value-Q for action in state according to the value function stored in self.values.
<br>
These numbers are all displayed in the GUI: the values are the numbers inside the square. The Q-values are the numbers in the quadrants of the square and the arrows rule outside each square.
To test the implementation, run autograder:

```
python autograder.py -q q1
```
The following command loads the ValueIterationAgent, which calculates a policy and executes it 10 times. Press a key on the keyboard to view the values, value-Qs, and simulation. You should notice that the value of the start state ( (start(V) which you can read from the GUI) and the resulting average empirical reward (printed after 10 runs) are quite close.
```
python gridworld.py -a value -i 100 -k 10
```
In the default BookGrid, running iterate over the value for 5 iterations should give you this output:
```
python gridworld.py -a value -i 5
```
![image](https://user-images.githubusercontent.com/117355603/222379429-2ae37880-71f5-4da7-91e1-e4ee7426e5c3.png)
## Bridge crossing analysis
BridgeGrid is a map on the world grid with a low-reward terminal state and a high-reward terminal state, separated by a narrow "bridge", on either side of which is a gap of high negative reward. The agent starts close to the low reward mode. With a default discount of 9.0 and a default noise of 2.0, the optimal policy does not cross the bridge.
```
python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
```
![image](https://user-images.githubusercontent.com/117355603/222379954-74b4095a-8bba-468d-a3d1-40196efc2e74.png)
## Policies
Consider the DiscountGrid map shown below. This grid has two end states with positive rewards. A near output with +1 reward and a far output with +10 reward. The bottom row of the grid contains end states with negative reward (shown in red) and we call this cliff part. Each state in the cliff has a reward. 10. The starting state is a yellow square. We distinguish between two types of routes: 1) routes that "risk the cliff" and move near the bottom row of the grid. These routes are shorter, but risk receiving They have a large negative reward and are indicated by the red arrow in the figure below. 2) Paths that "avoid the cliff" and move along the upper edge of the grid. These routes are longer, but less likely to incur large negative returns. These paths are shown with green arrows in the figure below:
![image](https://user-images.githubusercontent.com/117355603/222380455-db69a2be-15a9-4153-bf47-30ae031ff805.png)
We chose the settings of discount, noise and life reward parameters for this MDP in order to obtain several different types of optimal policies. Setting the parameter values for each section has the characteristic that if the agent follows its optimal policy without creating noise, the given behavior shows the If a certain behavior is not achieved with any setting of the parameters, the policy is claimed to be impossible by returning the string "POSSIBLE NOT".
Here are the types of optimal policies:
- Prefer the nearest exit (+1) risk the danger of the cliff (-10)
- Prefer the nearby exit (+1) but avoid the cliff (-10)
- Prefer the far exit (+10) take the risk of the cliff (-10)
- Prefer the far exit (+10) avoid the danger of the rock (-10) 
- Avoid both exits and cliffs (so the execution of an episode should never end).
<br>
Run autograder to check the answer:

```
python autograder.py -q q3
```
## Asynchronous Value Iteration






















