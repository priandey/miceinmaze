from .maze import Maze

class Mice():
    def __init__(self, maze):
        self.maze = maze
        self.start_point = maze.start_point
        self.end_point = maze.end_point
        self.path = []

    def get_path(self, motion_limit=6):
        path = []
        condition = False
        while not condition:
            for e in range(motion_limit):
                # move randomly 1 steps if step in Maze
                # record step in Path
            #check final step, if == end_point, self.path = path
