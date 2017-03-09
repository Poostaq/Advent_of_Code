class Authentication_Screen:
    screen = []
    def __init__(self, width, heigth):
        for i in range(0, heigth):
            screen_row = []
            for j in range(0,width):
                screen_row.append(Authentication_Screen.create_pixel())
            self.screen.append(screen_row)
        print("Authentication device created")

    def process_input(self, path_of_a_file):
        opened_file = open(path_of_a_file, 'r')
        provided_data = opened_file.read()
        provided_data = provided_data.split("\n", len(provided_data) - 1)
        for line in provided_data:
            print(line)
            if "rect" in line:
                line = line.split(" ")
                print(line)
                parameters = line[1].split("x")
                print(parameters)
                self.rect(int(parameters[0]), int(parameters[1]))
            else:
                line = line.split(" ")
                print(line)
                row_column = line[2].split("=")
                print(row_column)
                row_column = int(row_column[1])
                shift = int(line[4])
                if "row" in line:
                    self.rotate_row(row_column, shift)
                elif "column" in line:
                    self.rotate_column(row_column, shift)
            self.print_screen()


    def print_screen(self):
        for screen_row in self.screen:
            temp_row = []
            for pixel in screen_row:
                if pixel:
                    temp_row.append("X")
                else:
                    temp_row.append(" ")
            print(temp_row)

    def rect(self, width, heigth):
        for rows in range(0, heigth):
            for pixel in range(0, width):
                self.screen[rows][pixel] = True

    def rotate_row(self, row_number, shift):
        number_of_columns = len(self.screen[row_number])
        temp_row = []
        for pixel in range(0,number_of_columns):
            temp_row.append(False)
        for pixel_index in range(0, number_of_columns):
            new_index = pixel_index + shift
            if new_index > number_of_columns-1:
                new_index -= number_of_columns
            temp_row[new_index] = self.screen[row_number][pixel_index]
        self.screen[row_number] = temp_row

    def rotate_column(self, column_number, shift):
        number_of_rows = len(self.screen)
        old_values = []
        for value in range(0, number_of_rows):
            old_values.append(self.screen[value][column_number])
        for index in range(0, number_of_rows):
            new_index = index+shift
            if new_index >=number_of_rows:
                new_index -= number_of_rows
            self.screen[new_index][column_number] = old_values[index]

    def print_amount_of_lit_pixels(self):
        pixel_counter = 0
        for row_index in self.screen:
            for pixel_index in row_index:
                if pixel_index:
                    pixel_counter += 1
        print(pixel_counter)


    @staticmethod
    def create_pixel():
        return False

Test = Authentication_Screen(50, 6)
Test.process_input("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day8 input")
Test.print_screen()
Test.print_amount_of_lit_pixels()