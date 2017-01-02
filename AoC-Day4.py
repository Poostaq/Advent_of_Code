def check_sum_of_ID(path_of_a_file):
    file = open(path_of_a_file, 'r')
    data = file.read()
    data = data.split("\n", len(data)-1)

    id_counter = 0

    for record in data:
        id_adding_flag = True
        record = record.replace("-","").replace("[","").replace("]","")
        print(record)
        checksum = record[-5:]
        record = record.replace(record[-5:],"")
        id_number = int(record[-3:])
        record = record.replace(record[-3:],"")
        character_counter = {}
        for letter in range(97, 123):
            character_counter[str(chr(letter))] = 0
        for character in record:
            if character in character_counter:
                character_counter[character] += 1
        for character in checksum:
            #print(character)
            #print(character_counter[character])
            value_a = max(character_counter, key=lambda key: character_counter[key])
            print(value_a)
            if character_counter[character] != character_counter[value_a]:
                id_adding_flag = False
                break
            del character_counter[character]
        if id_adding_flag:
            id_counter += id_number
        print(id_counter)
        for character in record:

{}




check_sum_of_ID("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day4 input")