# -*- coding: utf-8 -*

import models as m

def main():
    maze = m.Maze()
    maze.std_structure()
    maze.print_structure(True) # Passer "True" en parametre pour afficher les coordonnees de chaque passage au lieu de '#'

    maze.print_structure(True) # Passer "True" en parametre pour afficher les coordonnées de chaque passage au lieu de '#'

    #maze.get_end_point()
    maze.print_structure()
    mice = m.Mice(maze)
    result = mice.get_path()
    print(result)
    # Initialize maze
    # Get input from user : number of steps & number of obstacles & endpoint
    # Magic tric
    # Output = list of obstacle's coordinates

main()
