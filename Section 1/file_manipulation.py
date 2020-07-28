f = open('../Ex_Files_Python_Automation/Exercise Files/inputFile.txt','r')

count = 0

for line in f:
    print(str(count) +": " + line)
    count += 1

f.close()