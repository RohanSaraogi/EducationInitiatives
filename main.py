# Name: Rohan Saraogi
# Roll No: 20BCP057
# Date:6th October 2023

# Mars Programming Exercise for Eductaion Initiatives Coding Test

''' Class grid represents obstacles coordinates and the total area of the grid '''


class Grid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.obstacles = set()

    def add_obstacle(self, x, y):
        # adds obstactle coordinates to list
        self.obstacles.add((x, y))

    def has_obstacle(self, x, y):
        # checks if coordinates has obstacle or not
        return (x, y) in self.obstacles


''' Class rover attributes:- current position(x,y), direction(N,S,E,W)(String), grid object '''


class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.f = 1

    ''' if command is 'M' then move the rover forward in facing the direction, if current dirrection is 
        'N' then (y+1) elseif 'S' (y-1) also if current dirrection is 'E' then (x+1) else (x-1)'''
    
    def move(self):
        if self.direction == 'N':
            new_x, new_y = self.x, self.y + 1
        elif self.direction == 'S':
            new_x, new_y = self.x, self.y - 1
        elif self.direction == 'E':
            new_x, new_y = self.x + 1, self.y
        elif self.direction == 'W':
            new_x, new_y = self.x - 1, self.y

        if 0 <= new_x < self.grid.size_x and 0 <= new_y < self.grid.size_y:
            if not self.grid.has_obstacle(new_x, new_y):
                self.x, self.y = new_x, new_y
            else:
                self.f=0

    ''' if command is 'R' then Turn the rover right, if current dirrection is 'N' then turn right ie 
        'W' elseif 'S' then 'E' also if current dirrection is 'E' then 'N'' else 'S'. '''

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    ''' if command is 'L' then Turn the rover Left, if current dirrection is 'N' then turn left ie 
        'E' elseif 'S' then 'W' also if current dirrection is 'E' then 'S'' else 'N'. '''

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    ''' generate status report of the rover current coordinates and which direction it is facing and no obstcles detected'''
    def generate_status_report(self):
        if self.f==1:
            return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected."
        else:
            return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. Obstacle detected and Rover Stooped  ."
            


def main():
    grid = Grid(10, 10)
    grid.add_obstacle(2, 2)
    grid.add_obstacle(3, 5)

    rover = Rover(0, 0, 'N', grid)
    commands = ['M', 'M', 'R', 'M', 'M', 'L']

    for command in commands:
        if command == 'M':
            rover.move()
        elif command == 'L':
            rover.turn_left()
        elif command == 'R':
            rover.turn_right()

    print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
    print(rover.generate_status_report())


if __name__ == "__main__":
    main()
