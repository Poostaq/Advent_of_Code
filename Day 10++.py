class BotFactory():
    botList = {}
    outputList = {}

    def __init__(self):
        opened_file = open("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day10 input", 'r')
        data = opened_file.read()
        data = data.split("\n", len(data) - 1)
        self.botList = {}
        for x in range(1, 50):
            for line in data:
                self.processCommand(line)
        self.computeResultForPartTwo()

    def processCommand(self, command):
        command = command.split(" ")
        #print(command)
        if command[0] == "value":
            value = int(command[1])
            #print(value)
            botNumber = command[5]
            self.tryCreatingBot(botNumber)
            if not value in self.botList[botNumber]:
                self.addValue(value, botNumber)
            #print(self.botList[botNumber])
        elif command[0] == "bot":
            givingBotNumber = command[1]
            targetDeviceLower = command[6]
            targetDeviceHigher = command[11]
            self.tryCreatingBot(givingBotNumber)
            if command[5] == "bot":
                self.tryCreatingBot(targetDeviceLower)
            else:
                self.tryCreatingOutput(targetDeviceLower)
            if command[10] == "bot":
                    self.tryCreatingBot(targetDeviceHigher)
            else:
                self.tryCreatingOutput(targetDeviceHigher)
            #print(self.botList[givingBotNumber])
            if len(self.botList[givingBotNumber]) == 2:
                print("bot " + givingBotNumber + " zaczyna przekazywanie wartosci")
                self.passValue(givingBotNumber,command[5],command[6],command[10],command[11])


    def tryCreatingBot(self, botNumber):
        if not botNumber in self.botList:
            self.botList[botNumber] = []

    def tryCreatingOutput(self, outputNumber):
        if not outputNumber in self.outputList:
            self.outputList[outputNumber] = 0

    def addValue(self, value, botNumber):
        listOfBotValues = self.botList[botNumber]
        listOfBotValues.append(value)
        self.botList[botNumber] = listOfBotValues

    def passValue(self, passingBot, targetLowerType, targetLowerNumber, targetHigherType, targetHigherNumber):
        self.sortValues(passingBot)
        if targetLowerType == "bot" and len(self.botList[targetLowerNumber]) < 2 :
            self.botList[targetLowerNumber].append(self.botList[passingBot][0])
        if targetHigherType == "bot" and len(self.botList[targetHigherNumber]) < 2 :
            self.botList[targetHigherNumber].append(self.botList[passingBot][1])
        if targetLowerType == "output":
            self.outputList[targetLowerNumber] = (self.botList[passingBot][0])
        if targetHigherType == "output":
            self.outputList[targetHigherNumber] = (self.botList[passingBot][1])
        self.botList[passingBot] = []

    def sortValues(self, botNumber):
        self.checkIfWantedBot(botNumber)
        self.botList[botNumber].sort()
        print("bot " + str(botNumber) + " = " + str(self.botList[botNumber]))

    def checkIfWantedBot(self, botNumber):
        if 17 in self.botList[botNumber] and 61 in self.botList[botNumber]:
            print("Znaleziony bot to " + str(botNumber))

    def computeResultForPartTwo(self):
        print(int(self.outputList["0"])*int(self.outputList["1"])*int(self.outputList["2"]))
test = BotFactory()
"""test.tryCreatingBot("1")
test.tryCreatingBot("2")
test.tryCreatingBot("3")
test.addValue(61, "1")
test.addValue(17, "1")
print(test.botList["1"])
test.passValue("1", "bot", "2", "bot", "3")"""

