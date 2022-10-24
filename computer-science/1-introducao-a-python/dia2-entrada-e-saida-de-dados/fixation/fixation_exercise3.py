file = open("fixation_exercise3.txt", mode="r")
failed = []

for line in file:
    name, grade = line.split(" ")

    if int(grade) < 6:
        failed.append(f"{name}\n")
        
file.close()

new_file = open("fixation_exercise3_new.txt", mode="w")
new_file.writelines(failed)
new_file.close()
