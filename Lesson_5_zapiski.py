f = open("secret.txt", "w") # r - это режим чтения, w - запись, перезапись
# date = f.read()
# data = f.readlines()
# print(data)
f.write("New information")

f.close()
