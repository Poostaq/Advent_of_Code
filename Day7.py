def check_if_ip_supports_tls(path_of_a_file):
    file = open(path_of_a_file, 'r')
    provided_data = file.read()
    provided_data = provided_data.split("\n", len(data) - 1)
    supernet_sequences = []
    hypernet_sequences = []


def split_line_into_sequences(line):
    temp_string = ""
    print("Whole Line: " + line)
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
    temp_string = ""
    return [supernet_sequences,hypernet_sequences]


        """for ip_part_index in range(len(split_IP)):
            for character_index in range(len(split_IP[ip_part_index])):
                if len(split_IP[ip_part_index]) >= character_index+4:
                    if split_IP[ip_part_index][character_index] == split_IP[ip_part_index][character_index+3]:
                        if split_IP[ip_part_index][character_index+1] == split_IP[ip_part_index][character_index+2]:
                            if split_IP[ip_part_index][character_index] != split_IP[ip_part_index][character_index+1]:
                                if (ip_part_index + 2) % 2 == 0:
                                    split_IP_part_check["bracketed"] += 1
                                    print("Part " + split_IP[ip_part_index] + "contains abba string - IP MAY BE VIABLE")
                                else:
                                    split_IP_part_check["non-bracketed"] += 1
                                    print("Part " + split_IP[ip_part_index] + "contains abba string - IP NON-VIABLE")
        print("Checking IP: " + line)
        if split_IP_part_check["bracketed"] > 0 and split_IP_part_check["non-bracketed"] == 0:
            ip_with_tsl_support += 1
            print("IP with TSL support so far: " + str(ip_with_tsl_support))

        split_IP_part_check["non-bracketed"] = 0
        split_IP_part_check["bracketed"] = 0
        split_IP = []"""


def check_for_aba(sequence):
    aba_sequences = []
    aba_found = ""
    for supernet_character_index in range(len(sequence)-2):
        if sequence[supernet_character_index] == sequence[supernet_character_index+2]:
            if sequence[supernet_character_index] != sequence[supernet_character_index+1]:
                aba_found += sequence[supernet_character_index]+sequence[supernet_character_index+1]+sequence[supernet_character_index+2]
                aba_sequences.append(aba_found)
    return aba_sequences

def aba_has_bab(aba_sequences,bab_sequences):



check_if_ip_supports_tls("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day7 input")