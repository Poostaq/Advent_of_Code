class Bot:
    list_of_bots = []
    bot_number = 0
    lower_value = 0
    higher_value = 0
    found_bot = -1
    def __init__(self, bot_number):
        self.bot_number = bot_number
        self.lower_value = 0
        self.higher_value = 0
        Bot.list_of_bots.append(self)

    def add_value(self, value):
        if value > self.lower_value:
            if value > self.higher_value:
                self.lower_value = self.higher_value
                self.higher_value = value
            else:
                self.lower_value = value


    def pass_value(self, which_value, bot_number):
        bot = Bot.return_bot_with_number(bot_number)
        if bot is None :
            bot = Bot.try_to_create_bot(bot_number)
        if which_value == "high" and self.higher_value != 0:
            bot.add_value(self.higher_value)
            print "Bot " + str(self.bot_number) + " passed " + str(self.higher_value) + " to bot " + str(bot_number)
            self.higher_value = 0
        elif which_value == "low" and self.lower_value != 0:
            bot.add_value(self.lower_value)
            print "Passed " + str(self.lower_value) + " to " + str(bot_number)
            self.lower_value = 0
        print "Bot " + str(bot_number) + " has values " + str(bot.lower_value) + " " + str(bot.higher_value)

    @staticmethod
    def try_to_create_bot(bot_number):
        if Bot.return_bot_with_number(bot_number) is not None:
            #print "There is already bot " + str(bot_number)
            return
        return Bot(bot_number)

    @staticmethod
    def return_bot_with_number(bot_number):
        for bot in Bot.list_of_bots:
            if bot.bot_number == bot_number:
                return bot
        #print "No bot with " + str(bot_number) + " number found"
        return None

def get_input_from_file(path_of_a_file):
    opened_file = open(path_of_a_file, 'r')
    data = opened_file.read()
    data = data.split("\n", len(data)-1)
    return data

def process_data():
    data = get_input_from_file("C:\PRYWATNE\PROJEKTY\Advent_of_Code\\day10 input")
    for line in data:
        line = line.split(" ")
        if line[0] == "value":
            value = line[1]
            bot_number = int(line[5])
            bot = Bot.try_to_create_bot(bot_number)
            if bot is not None:
                bot.add_value(value)
            else:
                bot = Bot.return_bot_with_number(bot_number)
                bot.add_value(value)
            #print "bot " + str(bot_number) + " has values " + str(bot.lower_value) + " " + str(bot.higher_value)
    #for x in range(1,1000):
    for line in data:
        line = line.split(" ")
        if line[0] == "bot":
            #print line
            bot_one_number = int(line[1])
            bot_one = Bot.try_to_create_bot(bot_one_number)
            if bot_one is None:
                bot_one = Bot.return_bot_with_number(bot_one_number)
            device_lower = line[5]
            device_higher = line[10]
            device_lower_number = int(line[6])
            device_higher_number = int(line[11])
            if bot_one.lower_value != 0 and bot_one.higher_value != 0:
                if (int(bot_one.lower_value) == 2 and int(bot_one.higher_value) == 3):
                    Bot.found_bot = bot_one.bot_number
                    print "ZNALAZL CHUJA NR " + str(bot_one.bot_number)
                if device_lower == "output":
                    bot_one.lower_value = 0
                elif device_lower == "bot":
                    bot_one.pass_value("low", device_lower_number)
                    bot_one.lower_value = 0
                if device_higher == "output":
                    bot_one.higher_value = 0
                elif device_higher == "bot":
                    bot_one.pass_value("high", device_higher_number)
                    bot_one.higher_value = 0
            print Bot.found_bot
    for bot in Bot.list_of_bots:
        print "bot " + str(bot.bot_number) + " has values " + str(bot.lower_value) + " " + str(bot.higher_value)
process_data()


