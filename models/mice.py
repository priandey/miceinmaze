# -*- coding: utf-8 -*

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
        condition = False
        while not condition:
            print('\n')
            self.current_position = self.start_point
            path = []
            while len(path) != motion_limit:
                potential_steps = list()

                for line in self.maze.structure:
                    if (self.current_position[0]+1,self.current_position[1]) in line:
                        potential_steps.append((self.current_position[0]+1,self.current_position[1]))
                    if (self.current_position[0],self.current_position[1]+1) in line:
                        potential_steps.append((self.current_position[0],self.current_position[1]+1))
                    if (self.current_position[0]-1,self.current_position[1]) in line:
                        potential_steps.append((self.current_position[0]-1,self.current_position[1]))
                    if (self.current_position[0],self.current_position[1]-1) in line:
                        potential_steps.append((self.current_position[0],self.current_position[1]-1))
                    else:
                        continue
                # Here we could chek on archive_path if the path hasn't already been made in that order
                # by running a for loop, where iter goes [:iter]

                decided_step = choice(potential_steps)
                if decided_step in path:
                    print("BEEN THERE")
                    continue
                if decided_step in self.maze.wall_coord or decided_step in self.maze.obstacle_coord:
                    print("BOUMWALL")
                    continue
                else:
                    self.current_position = decided_step
                    path.append(decided_step)

                    print(path)

            if self.end_point in path:
                condition = True
            else:
                continue

        return path
                # move randomly 1 steps if step in Maze
                # record step in Path
            #check final step, if == end_point, self.path = path
