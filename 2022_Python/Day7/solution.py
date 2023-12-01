

def build_tree(filename):
    print("hola")
    file_tree={}
    with open(filename, 'r', encoding='utf-8') as file:
        current_directory = ""
        for i,line in enumerate(file):
            line = line.strip().split(" ")
            if line[1] == "cd":
                cd = line[2]
                if cd == "/":
                    current_directory = "/"
                elif cd == "..":
                    current_directory = file_tree[current_directory]["parent"]
                    continue
                else:
                    current_directory = f"{current_directory}/{cd}"
               
                if current_directory not in file_tree:
                    file_tree[current_directory] = {
                        "parent" : "",
                        "size":0
                    } 
                # current_directory=cd
            elif line[1] == "ls":
                pass
            elif line[0] == "dir":
                dir_name = f"{current_directory}/{line[1]}"
                if dir_name not in file_tree:
                    file_tree[dir_name] = {
                        "parent" : current_directory,
                        "size":0
                    }
                else:
                    file_tree[dir_name]["parent"]=current_directory
            else:
                file_size = int(line[0])
                file_tree[current_directory]["size"] += file_size
                parent_dir = file_tree[current_directory]["parent"]
                while parent_dir != "":
                    file_tree[parent_dir]["size"] += file_size
                    parent_dir = file_tree[parent_dir]["parent"]
    return file_tree

def part1():
    file_tree = build_tree("inputD7.txt")
    total = sum([int(dir["size"]) for i, dir in file_tree.items() if int(dir["size"])<=100000])
    print(file_tree)
    return total
    
print(part1())

if __name__ == "__main__":
    print("_____Part1_____")

# 1390824