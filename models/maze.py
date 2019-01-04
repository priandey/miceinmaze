class Maze():
    def __init__(self):
        self.structure = list()
        self.y_range = 4
        self.x_range = 4
        self.start_point = tuple()
        self.end_point = tuple()

    def get_end_point(self):
        noerror = False
        while not noerror :
            try:
                raw_coord = input("Coordonnées de sorties (format : x,y) :")
                inter=raw_coord.split(",")
                self.end_point = (int(inter[0]), int(inter[1]))
                if type(self.end_point[0]) == int and type(self.end_point[1]) == int and len(self.end_point) == 2:
                    noerror = True
                else:
                    continue
            except:
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
                    else:
                        inter += '#'
                print(inter)
        else:
            for line in self.structure:
                print(line)
