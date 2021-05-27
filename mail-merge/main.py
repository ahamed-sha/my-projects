# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
name_list = []
with open("./Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    for name in list_of_names:
        new_name = name.strip()
        name_list.append(new_name)
    print(name_list)


for guest in name_list:
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        lines = starting_letter.readlines()
        words = lines[0].rstrip()
        replaced_word = words.replace("[name]", guest)
        f = open(f"./Output/ReadyToSend/{guest}.txt", "w")
        f.write(replaced_word)
        f.write("\n")
        for i in range(1, 7):
            f.write(lines[i])
