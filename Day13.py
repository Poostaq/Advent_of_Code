import Queue


class FindWayAgain:

    actual_x = 0
    actual_y = 0
    actual_number_of_steps = 0
    visited_locations = [[1, 1]]

    def __init__(self):
        self.actual_x = 1
        self.actual_y = 1
        self.actual_number_of_steps = 0

    def start_walking(self):
        queue = Queue.Queue()
        starting_position = self.Position(self.actual_x, self.actual_y, self.actual_number_of_steps)
        queue.put(starting_position)
        while queue.qsize() > 0:
            position = queue.get()
            if position.position_number_of_steps == 51:
                print("AAA " + str(len(self.visited_locations)))
                return
            # print(str(position.position_x) + " " + str(position.position_y) + " " + str(position.position_number_of_steps))
            neighbour_positions = position.possible_neighbours(position.position_x, position.position_y)
            if neighbour_positions is not None:
                for x in neighbour_positions:
                    if x not in self.visited_locations:
                        if self.is_desired_position(x[0], x[1]):
                            print("ILOSC KROKOW = " + str(position.position_number_of_steps+1))
                            return
                        else:
                            queue.put(self.make_step(x, position.position_number_of_steps))

    def make_step(self, position_coords, actual_step):
        self.visited_locations.append(position_coords)
        new_position = self.Position(position_coords[0], position_coords[1], actual_step+1)
        return new_position

    def is_desired_position(self, x, y):
        if x == 31 and y == 39:
            return True
        else:
            return False

    class Position:

        FAV_NUMBER = 1358
        position_x = 1
        position_y = 1
        position_number_of_steps = 0

        def __init__(self, x, y, number_of_steps):
            self.position_x = x
            self.position_y = y
            self.position_number_of_steps = number_of_steps

        def possible_neighbours(self, x, y):
            neighbours = []
            if self.space_or_wall(x + 1, y) == ".":
                neighbours.append([x + 1, y])
            if self.space_or_wall(x, y + 1) == ".":
                neighbours.append([x, y + 1])
            if x - 1 >= 0 and self.space_or_wall(x - 1, y) == ".":
                neighbours.append([x - 1, y])
            if y - 1 >= 0 and self.space_or_wall(x, y - 1) == ".":
                neighbours.append([x, y - 1])
            return neighbours

        def space_or_wall(self, x, y):
            number_to_binary = x * x + 3 * x + 2 * x * y + y + y * y + self.FAV_NUMBER
            binary_number = bin(number_to_binary)[2:]
            if self.sum_of_1_bits(binary_number) == "Even":
                return "."
            elif self.sum_of_1_bits(binary_number) == "Odd":
                return "#"

        def sum_of_1_bits(self, binary_str):
            sum = 0
            for x in binary_str:
                if x == "1":
                    sum += 1
            if sum % 2 == 0:
                return "Even"
            else:
                return "Odd"




Test = FindWayAgain()
Test.start_walking()


# Test.print_room()
