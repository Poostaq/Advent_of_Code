def check_if_ip_supports_tls(path_of_a_file):
    file = open(path_of_a_file, 'r')
    provided_data = file.read()
    provided_data = provided_data.split("\n", len(provided_data) - 1)
    number_of_SSL_IP = 0
    for line in provided_data:
        split_sequences = split_line_into_sequences(line)
        supernet_sequences = split_sequences[0]
        hypernet_sequences = split_sequences[1]

        aba_sequences = check_for_aba(supernet_sequences)
        bab_sequences = check_for_aba(hypernet_sequences)

        is_SSL = aba_has_bab(aba_sequences, bab_sequences)
        if is_SSL :
            number_of_SSL_IP += 1
    print(number_of_SSL_IP)

def split_line_into_sequences(line):
    temp_string = ""
    #print("Whole Line: " + line)
    supernet_sequences = []
    hypernet_sequences = []
    current_sequence = "supernet sequence"
    for character in line:
        if character != "[" and character != "]":
            temp_string += character
        else:
            if current_sequence == "supernet sequence":
                supernet_sequences.append(temp_string)
                current_sequence = "hypernet sequence"
            else:
                hypernet_sequences.append(temp_string)
                current_sequence = "supernet sequence"
            temp_string = ""
    supernet_sequences.append(temp_string)
    temp_string = ""
    return [supernet_sequences,hypernet_sequences]

def check_for_aba(sequence_list):
    aba_sequences = []
    aba_found = ""
    for sequence in sequence_list:
        for character_index in range(len(sequence)-2):
            if sequence[character_index] == sequence[character_index+2]:
                if sequence[character_index] != sequence[character_index+1]:
                    aba_found += sequence[character_index]+sequence[character_index+1]+sequence[character_index+2]
                    aba_sequences.append(aba_found)
                    #print(aba_found)
                    aba_found = ""
        aba_found = ""
    aba_found = ""
    return aba_sequences

def aba_has_bab(aba_sequences,bab_sequences):
    for aba in aba_sequences:
        for bab in bab_sequences:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                #print ("Dobre wyniki ma "+ aba + " " + bab)
                return True




check_if_ip_supports_tls("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day7 input")