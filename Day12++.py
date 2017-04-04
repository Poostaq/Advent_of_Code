class FindCodeDay12:
    registers = {"a":0,"b":0,"c":1,"d":0}

    def __init__(self):

        opened_file = open("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\test input", 'r')
        data = opened_file.read()
        data = data.split("\n", len(data) - 1)
        executedCommand = 0
        while executedCommand < len(data):
            line = data[executedCommand].split(" ")
            if line[0] == "cpy":
                self.cpy(line[1], line[2])
            if line[0] == "inc":
                self.inc(line[1])
            if line[0] == "dec":
                self.dec(line[1])
            if line[0] == "jnz":
                jump = self.jnz(line[1],line[2])
                executedCommand += jump
            executedCommand += 1
        print(self.registers["a"])



    def cpy(self,value,register):
        if value in self.registers:
            self.registers[register] = self.registers[value]
            # print("Kopiuje wartosc z " + str(value) + " do " + str(register))
        else:
            self.registers[register] = int(value)
            # print("Kopiuje wartosc " + str(value) + " do " + str(register))

    def inc(self, register):
        self.registers[register] += 1
        # print("Zwiekszylem " + str(register))

    def dec(self,register):
        self.registers[register] -= 1
        # print("Zmniejszylem " + str(register))

    def jnz(self, register, jump):
        if register in self.registers:
            if self.registers[register] != 0:
                return int(jump)-1
        elif register != 0:
            return int(jump) - 1
        return 0

Test = FindCodeDay12()

#komentarz