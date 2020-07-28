f = open('../Ex_Files_Python_Automation/Exercise Files/inputFile.txt','r')

pass_file = open('passfile.txt','w')

count = 0

for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        pass_file.write(line)

f.close()
pass_file.close()