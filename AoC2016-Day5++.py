import hashlib

def get_password():
    input = "uqwqemis"
    password = [0,0,0,0,0,0,0,0]
    loop_index = 0
    characters_found = 0

    print(input+str(loop_index))

    while characters_found < 8:
        string_to_hash = input+str(loop_index)
        string_to_hash = string_to_hash.encode('utf-8')

        hashing_machine = hashlib.md5()
        hashing_machine.update(string_to_hash)

        digested_hash = hashing_machine.hexdigest()

        if digested_hash[:5] == "00000":
            if digested_hash[5].isdigit():
                if int(digested_hash[5]) in range(0, 8):
                    if password[int(digested_hash[5])] == 0:
                        print(string_to_hash)
                        print("loop index: " + str(loop_index))
                        print("digest with 00000: " + digested_hash)
                        password[int(digested_hash[5])] = digested_hash[6]
                        characters_found += 1
        loop_index += 1
    print(password)
get_password()