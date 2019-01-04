from .maze import Maze
from random import choice

class Mice():
    def __init__(self, maze):
        self.maze = maze
        self.current_position = tuple()
        self.start_point = maze.start_point
        self.end_point = maze.end_point
        self.path = []

    def get_path(self, motion_limit=6):
        path = []
        condition = False
        while not condition:
            self.current_position = self.start_point
            for steps in range(motion_limit):

                potential_steps = list()

                for line in self.maze.structure
                    if (self.current_position[0]+1,self.current_position[1]) in line:
                        potential_steps.append((self.current_position[0]+1,self.current_position[1]))
                    if (self.current_position[0],self.current_position[1]+1) in line:
                        potential_steps.append((self.current_position[0],self.current_position[1]+1))
                    if (self.current_position[0]-1,self.current_position[1]) in line:
                        potential_steps.append((self.current_position[0]-1,self.current_position[1]))
                    if (self.current_position[0],self.current_position[1]-1) in line:
                        potential_steps.append((self.current_position[0],self.current_position[1]-1))
                    else:
                        break

                decided_step = choice(potential_steps)

                if decided_step in self.maze.wall_coord or decided_step in self.maze.obstacle_coord:
                    break


                # move randomly 1 steps if step in Maze
                # record step in Path
            #check final step, if == end_point, self.path = path
