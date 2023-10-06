# EducationInitiatives
Problem Statement
Create a simulation for a Mars Rover that can navigate a grid-based terrain. Your Rover should be able to move forward, turn left, and turn
right. You'll need to make sure that it avoids obstacles and stays within the boundaries of the grid. Remember to use pure Object-Oriented
Programming, design patterns, and avoid using if-else conditional constructs.
Functional Requirements
1. Initialize the Rover with a starting position (x, y) and direction (N, S, E, W).
2. Implement the following commands:
'M' for moving one step forward in the direction the rover is facing
'L' for turning left
'R' for turning right
3. Implement obstacle detection. If an obstacle is detected in the path, the Rover should not move.
4. Optional: Add functionality for the Rover to send a status report containing its current position and facing direction.
Key Focus
1. Behavioral Pattern: Use the Command Pattern to encapsulate 'M', 'L', 'R' as objects for flexibility.
2. Structural Pattern: Use the Composite Pattern to represent the grid and obstacles.
3. OOP: Leverage encapsulation, inheritance, and polymorphism.

## Usage
1.clone the repositorites.
https://github.com/RohanSaraogi/EducationInitiatives
```sh
cd E-Commerce--Educational-Initiatives-main
```
2.Run the Application.
```sh
python main.py
```



Possible Inputs
Grid Size: (10 x 10)
Starting Position: (0, 0, N)
Commands: ['M', 'M', 'R', 'M', 'L', 'M']
Obstacles: [(2, 2), (3, 5)]
Possible Outputs
Final Position: (1, 3, E)
Status Report: "Rover is at (1, 3) facing East. No Obstacles detected."
Evaluation
1. Code Quality: Are the best practices, SOLID principles, and design patterns effectively implemented?
2. Functionality: Does the code perform all the required tasks?
3. Global Convention: Is the code written in a way that is globally understandable?
4. Gold Standards: Does the code handle logging, exceptions, and validations effectively?
5. Code Walkthrough: Ability of the candidate to explain the architecture, design patterns used, and the decisions taken.
Intent of this exercise is to gauge the candidate's practical knowledge of design patterns, OOP, and coding best practices... This will serve
as an insightful lens through which to assess the depth and breadth of their skills...

