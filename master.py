import os 

cwd = os.getcwd()


os.chdir(cwd+'/pictures')

cwd = os.getcwd()

file_list = os.listdir(cwd)

for i in range(len(file_list)):
    print(file_list[i])