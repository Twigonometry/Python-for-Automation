f = open('../Ex_Files_Python_Automation/Exercise Files/inputFile.txt','r')

count = 0

print("Successful candidates:\n")

for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

f.close()