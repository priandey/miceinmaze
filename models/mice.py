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
        archived_path = []
        condition = False
        iter = 0
        while not condition:
            self.current_position = self.start_point
            archive_id = 0
            archive_check = False
            path = []
            archived_path.append(path)
            while len(path) != motion_limit:
                adding = False
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
                    '''if (len(archived_path)) > 1:
                        while not archive_check:
                            print("Archive")
                            decided_step = choice(potential_steps)
                            for old_path in archived_path:
                                if path[:archive_id] != old_path[:archive_id]:
                                    print("ARCHIVE CHECK")
                                    archive_check = True
                                else:
                                    print("NOT ARCHIVE CHECK")
                                    continue
                    else:'''
                decided_step = choice(potential_steps)

                if decided_step in self.maze.wall_coord or decided_step in self.maze.obstacle_coord:
                    print("going through wall")
                    continue
                else:
                    self.current_position = decided_step
                    path.append(decided_step)
                    archive_id += 1
                    print(path)

            if path[-1] == self.end_point:
                condition = True
            else:
                continue

        return path
                # move randomly 1 steps if step in Maze
                # record step in Path
            #check final step, if == end_point, self.path = path
