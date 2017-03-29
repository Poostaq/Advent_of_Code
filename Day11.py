import copy
import itertools
from multiprocessing import Queue

class ShortestWay():
    actualIsotopesPositions = []
    actualElevatorPosition = 1
    listOfSnapshots = []
    numberOfSteps = 0

    def __init__(self):
        opened_file = open("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\test input", 'r')
        data = opened_file.read()
        data = data.split("\n", len(data) - 1)
        for line in data:
            line = line.replace("The first ", "").replace("The second ", "").replace("floor contains ", ""). \
                replace("The third ", "").replace("The fourth ", "").replace("a ", ""). \
                replace("nothing relevant", "").replace(".", "").replace("-compatible", "").replace("and ", "").replace(",", "")
            line = line.split(" ", )
            print(line)
            floor_components = []
            for element_index in range(0,len(line),2):
                if len(line[element_index]) > 0:
                    component = [line[element_index],line[element_index+1]]
                    floor_components.append(component)
                    print("appending " + str(component))
            self.actualIsotopesPositions.append(floor_components)
        print(self.actualIsotopesPositions)
        self.numberOfSteps = 0
        self.actualElevatorPosition = 1

    def generateSnapshot(self,
                         snapshotPositions = actualIsotopesPositions,
                         snapshotElevator = actualElevatorPosition,
                         snapshotSteps = numberOfSteps):
        snapshot = ""
        radioisotope = 0
        elementType = 1
        for floor in snapshotPositions:
            for element in floor:
                snapshot+=element[radioisotope]+"."+element[elementType]+","
            snapshot = snapshot[:-1]
            snapshot += ";"
        snapshot = snapshot[:-1]
        return [snapshot, snapshotElevator, snapshotSteps]

    def unpackSnapshot(self, snapshot):
        self.actualIsotopesPositions = [[],[],[],[]]
        snapshotString = snapshot[0]
        snapshotString = snapshotString.split(';')
        for floorIndex in range(0,len(snapshotString)):
            if len(snapshotString[floorIndex]) == 0:
                continue
            else:
                tempList = []
                floor = snapshotString[floorIndex].split(",")
                for element in floor:
                    element = element.split(".")
                    tempList.append(element)
                self.actualIsotopesPositions[floorIndex] = tempList
        self.actualElevatorPosition = snapshot[1]
        self.numberOfSteps = snapshot[2]

    def tryMovingElevator(self, direction, carriedElements):
        #direction to +1 albo -1
        element_locations = copy.deepcopy(self.actualIsotopesPositions)
        elevator_position = self.actualElevatorPosition
        for element in carriedElements:
            #print(carriedElements)
            #print(element)
            #print(element_locations[elevator_position-1])
            #print(self.actualIsotopesPositions[elevator_position-1])
            element_locations[elevator_position-1].remove(element)
            element_locations[elevator_position-1+direction].append(element)
        if self.doesNothingBlow(element_locations, carriedElements):
            return [element_locations, elevator_position+direction]
        #print("Przenioslem" + str(carriedElements))

    def doesNothingBlow(self, elementsPositions, movedElements):
        if self.doesNotElevatorBlow(movedElements):
            return False
        if self.doesNotFloorBlow(elementsPositions):
            return False
        #print("Nie wybuchlo przeniesienie " + str(movedElements))
        return True

    def doesNotElevatorBlow(self, combination):
        if len(combination) == 2:
            if combination[0][0] != combination[1][0] and combination[0][1] != combination[1][1]:
                return False
        return True

    def doesNotFloorBlow(self, elementsPositions):
        for floor in elementsPositions:
            tempList = copy.deepcopy(floor)
            for elementIndex in range(0,len(floor)):
                #print("Porównuję: " + str(floor[elementIndex]))
                for iterator in range(0,len(floor)):
                    #print("porównany do: " + str(floor[iterator]))
                    if elementIndex == iterator:
                        continue
                    if floor[elementIndex][0] == floor[iterator][0]:
                        if floor[elementIndex] in tempList:
                            #print("Usuwamy z listy " + str(tempList) + " element " + str(floor[elementIndex]) + " i " + str(floor[iterator]))
                            tempList.remove(floor[elementIndex])
                            tempList.remove(floor[iterator])
            #print(tempList)
            microchips = list(filter(lambda x: x[1] == "microchip", tempList))
            generators = list(filter(lambda x: x[1] == "generator", floor))
            #print(microchips)
            #print(generators)
            if len(microchips) > 0\
                and len(generators) > 0:
                return False
        return True


    def createPossibleCombinations(self):
        tableToReturn = []
        for element in self.actualIsotopesPositions[self.actualElevatorPosition-1]:
            tableContainingElement =[]
            tableContainingElement.append(element)
            tableToReturn.append(tableContainingElement)
        for combination in itertools.combinations(self.actualIsotopesPositions[self.actualElevatorPosition-1], 2):
            tableToReturn.append(combination)
        return tableToReturn

    def isSearchedSnapshot(self):
        if len(self.actualIsotopesPositions[3]) == 4:
            return True
        else:
            return False

    def findShortestPath(self):
        queue_for_snapshots = Queue()
        initialSnapshot = self.generateSnapshot()
        queue_for_snapshots.put(initialSnapshot)
        self.listOfSnapshots.append(initialSnapshot[0])
        iterator = 0
        while queue_for_snapshots.qsize() > 0:
            iterator += 1
            if iterator%10==0:
                print(iterator)
            evaluatedSnapshot = queue_for_snapshots.get()
            self.unpackSnapshot(evaluatedSnapshot)
            if self.isSearchedSnapshot():
                print(self.numberOfSteps)
                break
            else:
                possible_combinations = self.createPossibleCombinations()
                for combination in possible_combinations:
                    if self.actualElevatorPosition > 1:
                        listOfLocationsAndElevatorPosition = self.tryMovingElevator(-1, combination)
                        if listOfLocationsAndElevatorPosition != None and \
                                self.doesNothingBlow(listOfLocationsAndElevatorPosition[0], combination):
                            if listOfLocationsAndElevatorPosition[0] not in self.listOfSnapshots:
                                snapshot = self.generateSnapshot(listOfLocationsAndElevatorPosition[0],
                                                      listOfLocationsAndElevatorPosition[1],
                                                      self.numberOfSteps+1)
                                queue_for_snapshots.put(snapshot)
                                self.listOfSnapshots.append(snapshot)
                    if self.actualElevatorPosition < 4:
                        listOfLocationsAndElevatorPosition = self.tryMovingElevator(1, combination)
                        if listOfLocationsAndElevatorPosition != None:
                            if self.doesNothingBlow(listOfLocationsAndElevatorPosition[0], combination) \
                                    and listOfLocationsAndElevatorPosition[0] not in self.listOfSnapshots:
                                snapshot = self.generateSnapshot(listOfLocationsAndElevatorPosition[0],
                                                      listOfLocationsAndElevatorPosition[1],
                                                      self.numberOfSteps + 1)
                                queue_for_snapshots.put(snapshot)
                                self.listOfSnapshots.append(snapshot)



Test = ShortestWay()
#print(Test.createPossibleCombinations())

Test.findShortestPath()

#print(Test.generateSnapshot())
#print(Test.unpackSnapshot('thulium.generator,thulium.microchip,plutonium.generator,strontium.generator,;plutonium.microchip,strontium.microchip,;promethium.generator,promethium.microchip,ruthenium.generator,ruthenium.microchip,;'))