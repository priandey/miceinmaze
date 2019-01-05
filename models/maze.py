# -*- coding: utf-8 -*

import random

class Maze():
    def __init__(self):
        self.structure = list()
        self.y_range = 7
        self.x_range = 7
        self.start_point = tuple()
        self.end_point = [0,0]
        self.wall_coord = [(1, 1), (1, 3), (1, 5), (3, 1), (3, 3), (3, 5), (5, 1), (5, 3), (5, 5)]
        self.obstacle_coord = list()
        self.couloirs=[(0,1),(0,3),(0,5),(1,0),(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(3,0),(3,2),(3,4),(3,6),(4,1),(4,3),(4,5),(5,0),(5,2),(5,4),(5,6),(6,1),(6,3),(6,5)]

    def get_end_point(self):
        noerror = False
        while not noerror :
            try:
                raw_coord = input("Coordonnées de sorties (format : x,y) :")
                inter=raw_coord.split(",")
                self.end_point = (int(inter[0]), int(inter[1]))
                if len(self.end_point) == 2:
                    if self.end_point not in self.wall_coord:
                        noerror = True
                else:
                    print("Trop de données (format : x,y)")
                    continue
            except:
                print("Données ou format non valide, respectez le format suivant : x,y")
                continue

    def std_structure(self):
        for y in range(self.y_range):
            line = list()
            for x in range(self.x_range):
                line.append((x,y))
            self.structure.append(line)
        self.start_point = self.structure[-1][0]

    def print_structure(self, printuple=False):
        if not printuple:
            for line in self.structure:
                inter = str()
                for entry in line:
                    if entry == self.start_point:
                        inter += 'S'
                    elif entry == self.end_point:
                        inter += 'R'
                    elif entry in self.wall_coord:
                        inter += 'O'
                    else:
                        inter += '#'
                print(inter)
        else:
            for line in self.structure:
                print(line)

#Generate every possible compbination of obstacles
    def put_obstacle_at(self):
        #number_obstacles= input("nombres d'obstacles : ")
        number_obstacles =2
        general_coord_obstacle=list()
        coord_obstacle=list()
        while number_obstacles > 0: #Create as many obstacle as needed
            gate_obstacle=0
            for posit in self.couloirs:
                if posit in coord_obstacle: #an obstacleis is already here
                    continue
                elif gate_obstacle==0 : #there is nothing here, put an obstacle
                    coord_obstacle.append(posit)
                    print ("put an obstacle")
                    number_obstacles-=1 #decrase amount of obstacles to put
                    gate_obstacle=1 #get out of the loop to start again.

        print ("coord : ",coord_obstacle)
