import sys
import re
import os
import shutil
from zipfile import ZipFile

def methodHandler(current,method,commands):
    '''
    Returns a method according to the user's selected option

            Parameters:
                    current (string): the path of .py, actual path
                    method (string): which method the user will input
                    commands (list): all the rest of the statements/commands after the method

            Returns:
                    caller method (object)
    '''
    list_paths = []
    methods = {"--todir": (3,copy_to),
               "--tozip": (2,zip_to),
               "--move": (3,move_to),
               "--delete": (1,delete),
               "--list": (2,print_all),
               "--find": (2,find_path),
               "--help": (0,help),
               #"--dedupli": lambda x:"dffd",
              }

    
    list_methods = methods.keys()             

    method_cond =  method in list_methods
    qtd_commands_cond = len(commands)>= methods[method][0]

    error_message = "Missing commands to proceed"

    if method_cond:
        if qtd_commands_cond and method != "--help":
            methods[method][1](current,commands)               
        elif method == "--help":
            methods[method][1]()                               
        else:
            return (False,error_message)            
        
    else:
        text_error = ','.join(each_command for each_command in list_methods)
        return (False,(f"this command: {method} is not valid. Use one of these: <({text_error}) command2 path1 path2>"))

def help():
    file = open(os.getcwd()+'\docs.txt','r',newline='\n')
    print(f'\n{file.read()}')
def check_dir(path,current):
    '''
    Returns the directory path depending on the argumnent. Whether . (dot) or a valid path

            Parameters:
                    path (string): the path where the method will perform the action
                    current (string): the path of .py, actual path
                    

            Returns:
                   dir_path (string): a valid path for bring used in further methods
    '''
    dir_path = path
    if path == ".":
        dir_path = os.path.dirname(os.path.abspath(current))+"\\"
    return dir_path

def all_files(path,current=""):
    '''
    Returns all the archives/directories from a predefined path

            Parameters:
                    current (string): the path of .py, actual path
                    path (string): the path where the method will perform the action
                    
            Returns:
                   A list of all archives logged
    '''
    directory = path
    if current != "":
        directory = check_dir(path,current)
    list_paths = list(enumerate(os.listdir(directory),1))
    return list_paths

def find_path(current,param):
    '''
    Find files/folders based on matching text pattern

            Parameters:
                current (string): the path of .py, actual path
                param (string): the path where the method will perform the action or the params to be filtered
    '''
    #pattern = r"\\((?!.*\\)[\d\sa-zA-Z_-]*)"
    pattern = r"(.*)(\.)"
    source = check_dir(param[0],current)
    files = os.listdir(source)
    paths = list((n,v) for n,v in enumerate(files,1))
    pattern_check = lambda x: (re.search(pattern,x)).group(1)
    for i in files:
        if (os.path.isdir(i)): #and param[1] in (pattern_check(i)):
            print(i)
    #print(*(f"{value} : {os.path.abspath(path)}" for value,path in paths if param[1] in (pattern_check(pattern,path))), sep="\n")
    
def print_all(current,param):
    '''
    Outputs all the archives/directories from a predefined path

            Parameters:
                    current (string): the path of .py, actual path
                    path (string): the path where the method will perform the action
                    
            Returns:
                   A list of all archives logged
    '''
    list_var = handleFiles("list",params=param[1],current=current,source=param[0])
    paths = list((n,v) for n,v in enumerate(list_var,1))
    print(*(f"{value} : {os.path.abspath(path)}" for value,path in paths if re.match(pattern,params)), sep="\n")  

def get_special(path,current, pattern):
    directory = (check_dir(path,current))    
    os.chdir(directory)
    list_paths = os.listdir(directory)
    
    if (len(list_paths) != 0):
        flag_pattern = False
        for path in list_paths:
            if os.path.isfile(path) and re.search(pattern,path):
                flag_pattern = True
                print (os.path.abspath(path))  
        if not(flag_pattern):
            raise Exception(f"Error: There's no file following the pattern:{pattern}")
    else:
        raise Exception("Error: There is no file in this directory") 
          
def validation_target(target):
    '''
    Validate target path otherwise it will be created if it doesn't exist

            Parameters:
                    target (string): the path where the method will perform the action
                    
            Returns:
                   boolean, empty/ error if False
    '''
    if os.path.isdir(target):
        return True,""
    elif os.path.isfile(target):
        return False,"This is not a valid target path."
    else:
        try:
            os.mkdir(target) 
        except:
            return False,f"Creation of the directory {target} failed"            
        return True,""      
    
def handleFiles(method,target="",source="",params = "",current = "",obj=""):
    '''
    Handles which method will be performed from all those that are in the dictionary

            Parameters:
                method (string): which method the user will input
                current (string): the path of .py, actual path
                path (string): the path where the method will perform the action
                    
            Returns:
                   A list of all archives logged
    '''

    list_paths = []
    methods = {"copy": lambda each_source,target: shutil.copy2(each_source,target),
               "zip": lambda each_source,target: obj.write(each_source),
               "move": lambda each_source,target: shutil.move(each_source,target),
               "del": lambda each_source,target: os.remove(each_source),
               "list": lambda each_source,target: list_paths.append(each_source)
              }
              

    # Find a way of dealing with a general file object as well as ZipFile does by using WITH structure (hint: using oop)
    # with Object("example.txt","w") as myfile:
    #   myfile.write('sadd')

    error_list = []

    source = source if source == "" else check_dir(source,current)
    target = target if target == "" else check_dir(target,current)

    validation_source,message = (True,"") if (os.path.isdir(source) or os.path.isfile(source)) and source != target else (False,"This is not a valid source path.")
    error_list.append(message)

    validation_target_cond,message = validation_target(target)
    error_list.append(message)
    obj_file = ""

    cond_validation = validation_source if method in ["zip","del","list"] else validation_source and validation_target_cond
    
    
    if cond_validation and any(map(lambda x:x==method,methods.keys())):
           
        os.chdir(source)
        files = os.listdir(source)
        pattern_2 = r".+(\..*)$"
        pattern = r"\..*"
        pattern_check = lambda x,y: y == (re.search(pattern_2,x)).group(1) #maracutaia
  
                             
        if "".join(params) == "--all":
            for each_source in files:
                #os.path.getatime(each_source)
                methods[method](each_source,target)
        elif re.match(pattern,params) and not "," in params:
            for each_source in files:
                if not(os.path.isdir(each_source)) and pattern_check(each_source,params):
                    methods[method](each_source,target) 
        elif "-" in params[0]:
            match_pattern = params[1:]
            for each_source in files:
                if not (pattern_check(each_source,match_pattern)):
                    methods[method](each_source,target)
        elif "," in params and all(map(lambda x:not(x.isdigit()),params.split(","))):
            for each_extension in params.split(","):
                for each_source in files:
                    if not(os.path.isdir(each_source)) and pattern_check(each_source,each_extension):
                        methods[method](each_source,target) 
        else:
            pos = params.split(",")
            if all(map(lambda x:x.isdigit(),pos)):
                pos = list(map(int,pos))
                if max(pos) <= len(files):
                    list_files = all_files(source)
                    for i in pos:
                        methods[method](list_files[i-1][1],target)
                else:
                    raise Exception("Error: Params greater than expected")
            else:
                raise Exception("Error: Invalid parameters")
        
        if method == "list":
            return list_paths

                    
    else:
        if len(error_list) > 1:
            raise Exception("\nError: ".join(filter(lambda x: x != "",error_list)))
        else:
            raise Exception("Error: The method is invalid")
            
def copy_to(current,param):
    '''
    Copy file(s)/folder from a source to a target path

            Parameters:
                current (string): the path of .py, actual path
                param (string): the path where the method will perform the action or the params to be filtered
    '''
    handleFiles("copy",target=param[1],source=param[0],params=param[2],current=current)
    
def zip_to(current,params):
    '''
    Zip/Compact selected files or the whole folder, depending on the source and target paths

            Parameters:
                current (string): the path of .py, actual path
                param (string): the path where the method will perform the action or the params to be filtered          
    '''
    target=""
    source=""
    name=""
    param = ""
    path=""
    cond_target = "\\" in params[1] 
    if cond_target:
        source,target,name = params[0],params[1],params[2]
        param = "" if len(params) == 3 else params[3]
        path = target
    else:
        source,name = params[0],params[1]
        param = "" if len(params) == 2 else params[2]
        path = source
    with ZipFile(path+fr"\{name}.zip",'w') as zipObj:
        handleFiles("zip",target,source,param,current,zipObj)
    if cond_target:
        move_to(current,[source,target,""])

def move_to(current,param):
    '''
    Move file(s)/folder from a source to a target path

            Parameters:
                current (string): the path of .py, actual path
                param (string): the path where the method will perform the action or the params to be filtered          
    '''
    handleFiles("move",target=param[1],source=param[0],params=param[2],current=current) 

def delete(current,params):
    '''
    Delete file(s)/folder from a source path

            Parameters:
                current (string): the path of .py, actual path
                param (string): the path where the method will perform the action or the params to be filtered          
    '''

    target = params[0] if re.match(r"\\$",params[0]) or os.path.isfile(params[0]) else params[0]+"\\"
    cond_param = len(params) < 2
    if os.path.isfile(target):
        os.remove(target) 
    elif os.path.isdir(target) and len(os.listdir(target)) == 0 and cond_param :
        os.removedirs(target)               
    elif os.path.isdir(target) and len(os.listdir(target)) > 0 and cond_param :
        shutil.rmtree(target)
    else:
       handleFiles("del",params=params[1],source=target)
""" def countFiles(current,param):
    list_var = handleFiles("list",params=param[1],current=current,source=param[0])
    paths = filter(lambda )
    list((n,v) for n,v in enumerate(list_var,1))
    print(*(f"{value} : {os.path.abspath(path)}" for value,path in paths), sep="\n")    """     
    
def main():
    get_special(r"F:\Arquivos\NewM\videos_reunioes",r"F:\Arquivos\NewM\videos_reunioes",r"__\w*__")
    
if __name__ == "__main__":
  main()  


'''
Ideas:

-put a recursive method to run through the directories
- find better names for dir_var, dir_path, path, current
*- deduplicate files
- sort by modification and creation date
- create a database in sqlite where will store all instructions performed by cmd during this app runtime in order to easier next time (pressing down key to get old instructions)
-- use as well as to save the files/dir history to make upcoming comparisons
*- a method to compare files with the same name but distinct extension, for example if you wanna delete a pdf from a djvu that already exists
Examples that don't work:
Design a way of allowing list files without --all
copyspecial_solut.py --list .
copyspecial_solut.py --list F:\a

'''
