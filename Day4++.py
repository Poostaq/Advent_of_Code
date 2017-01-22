def check_sum_of_ID(path_of_a_file):
    file = open(path_of_a_file, 'r')
    data = file.read()
    data = data.split("\n", len(data)-1)
    northpole_line = ""
    id_counter = 0

    northpole_room_id = ""
    for record in data:
        id_adding_flag = True
        record = record.replace("-","").replace("[","").replace("]","")
        print(record)
        checksum = record[-5:]
        record = record.replace(record[-5:],"")
        id_number = int(record[-3:])
        record = record.replace(record[-3:],"")
        character_counter = {}
        translated_record = ""
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
            #print(ord(character))
            #print(ord(character)+id_number)
            #print((ord(character)+id_number)%26)
            if (id_number%26)+ord(character) <= 122:
                translated_record += chr((id_number % 26) + ord(character))
            else:
                translated_record += chr((id_number % 26) + ord(character)-26)
            #print(((ord(character)+id_number)%26)+97)
            #print(translated_record)
        if "northpole" in  translated_record:
            northpole_line = translated_record
            northpole_room_id = id_number
    print(northpole_room_id)
    print(northpole_line)



check_sum_of_ID("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day4 input")