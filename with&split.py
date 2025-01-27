with open("Codingal.txt",'w') as file:
    file.write("\n Hi my name is Maham.")
file.close()

with open("Codingal.txt",'r') as file:
    data=file.readlines()
    for i in data:
        word=i.split()
        print(word)
file.close()