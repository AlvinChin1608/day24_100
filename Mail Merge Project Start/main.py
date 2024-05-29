#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("./Input/Letters/starting_letter.txt", "[name]") as letters:
#     content = letters.readlines()
#     print(content)

PLACEHOLDER = "[name]"


# Name list
with open("./Input/Names/invited_names.txt", "r") as names_file:
    name_list = names_file.readlines()
name_list = [name.strip() for name in name_list] #strip() any new line aka \n
print(name_list)


# with open("./Input/Names/invited_names.txt") as names_file:
#     name_list = names_file.readlines()
#     print(name_list)


with open("./Input/Letters/starting_letter.txt") as letters:
    letter_content = letters.read()
    for name in name_list:
        new_letter = letter_content.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/{name}", mode= "w") as ready_letter:
            ready_letter.write(f"{new_letter}")

