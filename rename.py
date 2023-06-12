import os 

source = "C:/Users/pablo/Downloads" 
dest = "C:\Users\pablo\Documents\pasta_para_projeto115"

file_name = os.path.rename(dest)
print("O arquivo esta sendo renomeado" + file_name + "...")

