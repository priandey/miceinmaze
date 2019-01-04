# -*- coding: utf-8 -*

import models as m

def main():
    maze = m.Maze()
    maze.std_structure()
<<<<<<< HEAD
    maze.print_structure(True) # Passer "True" en parametre pour afficher les coordonnees de chaque passage au lieu de '#'
=======
    maze.print_structure(True) # Passer "True" en parametre pour afficher les coordonnées de chaque passage au lieu de '#'
>>>>>>> 787b5cbdcb66ca1ec7da031b9d58d2a063d8b93b
    maze.get_end_point()
    maze.print_structure()
    # Initialize maze
    # Get input from user : number of steps & number of obstacles & endpoint
    # Magic tric
    # Output = list of obstacle's coordinates

main()
