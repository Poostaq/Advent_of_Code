def check_if_ip_supports_tls(path_of_a_file):
    file = open(path_of_a_file, 'r')
    data = file.read()
    data = data.split("\n", len(data) - 1)
    split_IP = []
    index_for_split_IP = 0
    ip_with_tsl_support = 0
    split_IP_part_check = {"non-bracketed" : 0, "bracketed" : 0}


def splitting_ip(line):
        temp_string = ""
        print("Whole Line: " + line)
        for character in line:
            if character != "[" and character != "]":
                temp_string += character
            else:
                split_IP.append(temp_string)
                temp_string = ""
                index_for_split_IP += 1
        split_IP.append(temp_string)
        temp_string = ""

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
        for supernet_ip_part_index in range(0, len(split_IP), 2):
            for supernet_character_index in range(len(split_IP[supernet_ip_part_index])):
                if len(split_IP[supernet_ip_part_index]) >= supernet_character_index+3:
                    if split_IP[supernet_ip_part_index][supernet_character_index] == split_IP[supernet_ip_part_index][supernet_character_index+2]:
                        if split_IP[supernet_ip_part_index][supernet_character_index] != split_IP[supernet_ip_part_index][supernet_character_index+1]:
                            for hypernet_ip_part_index in range(1,len(split_IP), 2):
                                for hypernet_character_index in range(len(split_IP[hypernet_ip_part_index])):
                                    if len(split_IP[hypernet_ip_part_index]) >= hypernet_ip_part_index+3:
                                        if split_IP[hypernet_ip_part_index][hypernet_character_index] == split_IP[hypernet_ip_part_index][hypernet_character_index+1]:
                                            if split_IP[hypernet_ip_part_index][hypernet_character_index] == split_IP[supernet_ip_part_index][supernet_character_index+1]:
                                                if split_IP[hypernet_ip_part_index][hypernet_character_index] == split_IP[supernet_ip_part_index][supernet_character_index+2]:



    print("IP with TSL support:" + str(ip_with_tsl_support))

def check_for_aba(sequence):
    for supernet_character_index in range(len(sequence)-2):
        if sequence[supernet_character_index]



check_if_ip_supports_tls("C:\\Users\\Poostaq\\Dysk Google\\Projekty\\Advent of Code\\day7 input")