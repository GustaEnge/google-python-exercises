import os
import os.path
import re

#dict-win= {} #global dictionary which will be assigned all the names

def handlePath(filename):
    backslash = "\\"
    regex_dir_pattern = r'(^.*\\)\w+\.\w+$'
    filename_list = filename.split()
    file_path = filename_list[0]
    cond = True if re.search(regex_dir_pattern, file_path) == None else False
    if "--summary" in filename_list and len(filename_list) == 2 and not(cond):
        openFile(file_path,filename_list[1])
    elif "--all" and "--summary" in filename_list and cond:
        runFolder(file_path+backslash) if backslash not in file_path[-1] else runFolder(file_path)
    elif cond:
        openFile(file_path, "")


def openFile(filename,action):

    s = ""
    list_ranking = []
    try:
        with open(filename,"rt",newline=None) as f:
            list_ranking = extract_names(f.read())
            print(list_ranking)
            f.close()
            if action == '--summary':
                write_file(list_ranking,filename)
    except:
        print("Couldn't find any file in this path.")

def extract_names(file):
    dict_win = {}
    full_list = []
    list_win = []
    year = int(re.findall(r"([0-9]*)</h3>",file)[0])
    beginning_anchor_term = file.find("h3")
    ending_anchor_term = file[beginning_anchor_term:].find("</table>")
    str_var = file[beginning_anchor_term:ending_anchor_term]
    name_rank = re.findall(r'(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)',str_var)
    for name in name_rank:
        dict_win[name[1]] = name[0]
        dict_win[name[2]] = name[0]
    list_win = list(dict_win.keys())
    list_win.sort()
    full_list.append(year)
    for i in range(len(list_win)):
        full_list.append(str(list_win[i]+" "+dict_win[list_win[i]]))
    return full_list

def write_file(list_var,filename):
    regex_dir_pattern = r'(^.*\\)\w+\.\w+$'
    m = re.search(regex_dir_pattern, filename)
    directory = m.group(1)
    current_path = directory+f'{list_var[0]}'+'.txt'

    if os.path.isfile(current_path):
        os.remove(current_path)
    w = open(directory + f'{list_var[0]}' + '.txt',"w")
    for each in list_var:
        print(each, end="\n", file=w)
        # print("".join(map(str, stretch) for stretch in list_var), end="\n") tentar imprimir usando generator

    w.close()

#here a function that runs every single file  and release an overall of the most used names based on search
def runFolder(path_f):
   # m = re.search(r'(^.*\\)\w+\.\w+$',path_f) this snippet is searching to match all the path(directory) but name of file and extension

    list_dir = os.listdir(path_f) #list all the files that belong to the right-most directory
    for each_file in list_dir:
        if ".html" in each_file:
            openFile(path_f+each_file, "--summary")

def main():

    #input_var = r"C:\Users\gustavo.cunha\Desktop\Pessoal\texto_mimic.txt"

    path_f = input("Enter the path of the file you would like to see the most used names and --summary (blank space in between) for retrieving the alphabetic-order ranking into a new file: ")
    handlePath(path_f)

if __name__ == "__main__":
    main()
