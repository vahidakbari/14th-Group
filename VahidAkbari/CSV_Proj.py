username=[]
identifire=[]
firstname=[]
lastname=[]
with open("username.csv", "r") as csv_file:
    for i in range(6):
        line = csv_file.readline().strip('\n').split(';')
        username.append(line[0])
        identifire.append(line[1])
        firstname.append(line[2])
        lastname.append(line[3])
print(username)
print(identifire)
print(firstname)
print(lastname)

