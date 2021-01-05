#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/home/eden/PycharmProjects/mail-merge-project-start/Input/Names/invited_names.txt") as names:
    all_names = names.readlines()
    with open("/home/eden/PycharmProjects/mail-merge-project-start/Input/Letters/starting_letter.docx") as letter_template:
        content = letter_template.read()
    for name in all_names:

        with open(f"/home/eden/PycharmProjects/mail-merge-project-start/Input/Letters/to_{name}.docx", mode = 'w') as send:
            stripped_name = name.strip()
            completed_letter = content.replace('[name]', f"{name}")
            send.write(completed_letter)





