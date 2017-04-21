import Queue
import copy
class Day24:

    position_x = 0
    position_y = 0
    number_of_steps = 0
    ventilation_map = []
    points_to_visit = []
    points_coordinates = {}

    def __init__(self):
        opened_file = open("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\MyInput.txt", 'r')
        data = opened_file.read()
        self.number_of_steps = 0
        self.ventilation_map = data.split("\n", len(data) - 1)
        self.position_y = self.find_starting_y()
        self.position_x = self.find_starting_x()
        position_0 = {"x":self.position_x, "y":self.position_y}
        self.points_to_visit = self.find_important_points()
        self.points_coordinates = self.coords_for_important_points()

    def print_map(self):
        for line in self.ventilation_map:
            print(line)

    # ###INIT FUNCTIONS###
    def find_starting_y(self):
        for index in range(0, len(self.ventilation_map)):
            if '0' in self.ventilation_map[index]:
                return index
        return None

    def find_starting_x(self):
        for index in range(0, len(self.ventilation_map)):
            if '0' in self.ventilation_map[index]:
                return self.ventilation_map[index].index('0')
        return None

    def find_important_points(self):
        return_list = []
        for line in self.ventilation_map:
            for char in line:
                if char not in ['#', '.', '0']:
                    return_list.append(char)
        return return_list
    # ###/INIT FUNCTIONS###

    def coords_for_important_points(self):
        temp_coords = {}
        for X in self.points_to_visit:
            temp_coords[X] = self.find_coordinates_X(X)
        return temp_coords


    def find_shortest_path(self):
        queue = Queue.Queue()
        initial_snapshot = self.Snapshot(self.position_x, self.position_y, self.points_to_visit, self.number_of_steps)
        queue.put(initial_snapshot)
        while queue.qsize() > 0:
            snapshot = queue.get()
            possible_moves = self.check_possible_moves(snapshot.position_x, snapshot.position_y)
            for coordinates in possible_moves:
                new_snapshot = self.move_cleaner(coordinates, snapshot)
                if self.all_points_visited(new_snapshot.remaining_places):
                    print(new_snapshot.last_place)
                    print("Skonczylem w " + str(new_snapshot.steps_made) + "ruchach!")
                    return
                else:
                    queue.put(new_snapshot)

    def all_points_visited(self, points_to_visit):
        if len(points_to_visit) == 0:
            return True
        else:
            return False

    def move_cleaner(self, coordinates, previous_snapshot):
        x = coordinates["x"]
        y = coordinates["y"]
        last_place = previous_snapshot.last_place
        remaining_locations = copy.deepcopy(previous_snapshot.remaining_places)
        if coordinates != last_place:
            if self.ventilation_map[y][x] in remaining_locations:
                remaining_locations.remove(self.ventilation_map[y][x])
                visited_locations = []
        last_place = {"x": x, "y": y}
        # print("Ruszam do " + str(coordinates))
        return self.Snapshot(x, y, remaining_locations, previous_snapshot.steps_made+1, last_place)

    def find_coordinates_X(self, X):
        for iterator_y in range(0,len(self.ventilation_map)):
            for iterator_x in range(0, len(self.ventilation_map[iterator_y])):
                if str(self.ventilation_map[iterator_y][iterator_x]) is str(X):
                    return {"x": iterator_x, "y": iterator_y}
        return None

    def calculate_distance_AB(self, a, b):
        queue = Queue.Queue()
        initial_snapshot = self.Snapshot_augmented(a["x"], a["y"], 0)
        queue.put(initial_snapshot)
        while queue.qsize() > 0:
            snapshot = queue.get()
            possible_moves = self.check_possible_moves(snapshot.position_x, snapshot.position_y)
            for coordinates in possible_moves:
                x = coordinates["x"]
                y = coordinates["y"]
        # DOKONCZYC!!!

    def check_possible_moves(self, x, y):
        possible_moves = []
        if self.ventilation_map[y][x+1] is not "#":
            possible_moves.append({"x": x+1, "y": y})
        if self.ventilation_map[y][x-1] is not "#":
            possible_moves.append({"x": x-1, "y": y})
        if self.ventilation_map[y+1][x] is not "#":
            possible_moves.append({"x": x, "y": y+1})
        if self.ventilation_map[y-1][x] is not "#":
            possible_moves.append({"x": x, "y": y-1})
        # print(possible_moves)
        return possible_moves

    class Snapshot:
        position_x = 0
        position_y = 0
        remaining_places = []
        last_place = {}
        steps_made = 0

        def __init__(self, x, y, remaining_places, steps_made, last_place={}):
            self.position_x = x
            self.position_y = y
            self.remaining_places = remaining_places
            self.last_place = last_place
            self.steps_made = steps_made

    class Snapshot_augmented:
        position_x = 0
        position_y = 0
        last_place = {}
        steps_made = 0

        def __init__(self, x, y, steps_made, last_place={}):
            self.position_x = x
            self.position_y = y
            self.last_place = last_place
            self.steps_made = steps_made

Test = Day24()

print(Test.find_important_points())
print(Test.find_starting_x())
print(Test.find_starting_y())
# Test.print_map()
Test.find_shortest_path()