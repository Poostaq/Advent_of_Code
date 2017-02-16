# -*- coding: UTF-8 -*-
import Queue
import itertools

class FloorObject:
    def __init__(self, object_type, radioisotope="none"):
        self.object_type = object_type
        self.radioisotope = radioisotope

    def to_string(self):
        return self.object_type + self.radioisotope


class Snapshot:
    def __init__(self, actual_locations, elevator_positon):
        self.actual_locations = actual_locations
        self.elevator_position = elevator_positon

    def generate_snapshot_stamp(self):
        snapshot = ""
        for floor in print_names_of_objects(self.actual_locations):
            floor = sorted(floor)
            for element in floor:
                snapshot += element
        snapshot += str(self.elevator_position)
        print(snapshot)
        return snapshot


def create_initial_locations(path_of_a_file):
    file = open(path_of_a_file, 'r')
    data = file.read()
    data = data.split("\n", len(data) - 1)
    clear_data = []
    for line in data:
        line = line.replace("The first ", "").replace("The second ", "").replace("floor contains ", "").\
            replace("The third ", "").replace("The fourth ", "").replace("a ", "").\
            replace("nothing relevant", "").replace(".", "").replace("-compatible", "").replace("and ", "")
        line = line.split(", ",)
        floor_components = []
        for element in line:
            if "generator" in element:
                radioisotope = element.replace(" generator", "")
                component = FloorObject("generator", radioisotope)
                floor_components.append(component)
            elif "microchip" in element:
                radioisotope = element.replace(" microchip", "")
                component = FloorObject("microchip", radioisotope)
                floor_components.append(component)
            else:
                pass
        clear_data.append(floor_components)
    return clear_data


def print_names_of_objects(location_of_objects):
    names_of_objects = []
    for floor in location_of_objects:
        floor_object_names = []
        floor_object_names.append(" ")
        for element in floor:
            floor_object_names.append(element.radioisotope + element.object_type)
        names_of_objects.append(floor_object_names)
    return names_of_objects


def is_searched_stamp(Snapshot):
    if len(Snapshot.actual_locations[3]) == 10:
        return True
    else:
        return False

# DO MOŻLIWEJ OPTYMALIZACJI
def create_possible_combinations(Snapshot):
    table_to_return = []
    for combination in itertools.combinations(Snapshot.actual_locations[Snapshot.elevator_position-1],1):
        table_to_return.append(combination)
    for combination in itertools.combinations(Snapshot.actual_locations[Snapshot.elevator_position-1],2):
        table_to_return.append(combination)
    return table_to_return

def try_moving_element(snapshot, combination, destination_floor):
    element_locations = snapshot.actual_locations
    for element in combination:
        element_locations[snapshot.elevator_position-1].remove(element)
        element_locations[destination_floor-1].append(element)


def check_if_does_not_blow(elements_of_floor):
    evaluated_floor = elements_of_floor
    for element in evaluated_floor:
        for i in range(len(evaluated_floor)):
            if element.radioisotope == evaluated_floor[i].radioisotope and element.object_type != evaluated_floor[i].object_type:
                evaluated_floor.remove(element)
                evaluated_floor.remove(evaluated_floor[i])
    #DO DOKONCZENIA

def main():
    list_of_snapshots = []
    list_of_snapshot_stamps = []
    queue_for_snapshots = Queue()
    input_locations = create_initial_locations("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day11 input")
    starting_snapshot = Snapshot(input_locations,1,0)
    queue_for_snapshots.put(starting_snapshot)
    while queue_for_snapshots.qsize() > 0:
        evaluated_snapshot = queue_for_snapshots.get()
        if is_searched_stamp(evaluated_snapshot):
            print(evaluated_snapshot.number_of_steps)
            break
        else:
            possible_combinations = create_possible_combinations(evaluated_snapshot)
if __name__ == "__main__":
    main()
