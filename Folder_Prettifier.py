# oh soldier prettify my folder
import os

# folder = input("Enter the path of your folder")
# file = input("Enter the path of the file which should not be changed")
# format = input("Enter the file format ")

def soldier(folder,file,format):
    os.chdir(folder)
    files = os.listdir(folder)
    i = 1
    
    with open(file) as f:
        filelist = f.read().split("\n")
        
    for item in files:
        if item in filelist:
            pass
        elif os.path.splitext(item)[1] == format:
            os.rename(item,f"{i}{format}")
            i += 1
        else:
            # os.rename(item,item[0].upper()+item[1:])
            os.rename(item,item.capitalize())
    
soldier(r"")
    