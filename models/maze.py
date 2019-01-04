class Maze():
    def __init__(self):
        self.structure = list()
        self.y_range = 7
        self.x_range = 7
        self.start_point = tuple()
        self.end_point = tuple()
        self.wall_coord = [(1, 1), (1, 3), (1, 5), (3, 1), (3, 3), (3, 5), (5, 1), (5, 3), (5, 5)]
        self.obstacle_coord = list()

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
