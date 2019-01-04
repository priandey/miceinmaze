import models as m

def main():
    maze = m.Maze()
    maze.std_structure()
    maze.print_structure()
    maze.get_end_point()
    maze.print_structure()
    # Initialize maze
    # Get input from user : number of steps & number of obstacles & endpoint
    # Magic tric
    # Output = list of obstacle's coordinates

main()
