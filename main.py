#Ria Saldajeno

def decode(password):
    decoded = [int(num) - 3 for num in password]
    decoded_password = ''.join(map(str, decoded))
    return decoded_password


if __name__ == "__main__":
    while True:
        # prints menu and prompts user input
        useroption = int(input(("Menu\n------------- \n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")))

        #encoder
        if useroption == 1:
            pass_to_encode = input("Please enter your password to encode: ")
            pass_to_encode_list = []

            # convert the password from string to a list
            pass_to_encode_list[:0] = pass_to_encode

            # set up empty list and string for the encoded password later
            encoded_pass_list = []
            encoded_pass = ""

            # for every item in the password, add 3
            for item in pass_to_encode_list:
                item = int(item)
                item += 3

                # add new value of the item to a list
                encoded_pass_list.append(str(item))

                # store the whole list as a string in encoded_pass variable
                encoded_pass = ''.join(encoded_pass_list)

            print("Your password has been encoded and stored!\n")

        #decoder
        if useroption == 2:

            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.\n')

        #quit
        if useroption == 3:
            break