import os

#this stuff is kinda cryptic to me so it's basically just copied and pasted in
#i'll try to explain what its doing though, for my sake

PRINTED_FILE = "printed_assignments.txt"

def load_printed():

    #if the file doesn't exist, we haven't printed anything yet so return empty set
    if not os.path.exists(PRINTED_FILE):
        return set()
    
    #open the file and return a set of each line
    with open(PRINTED_FILE, "r") as f:
        return set(int(line.strip()) for line in f)
    

def save_printed_ids(printed_ids):
    #open the file in write mode, give a set of ids we printed and add it to the file
    with open(PRINTED_FILE, "w") as f:
        for id in printed_ids:
            f.write(f"{id}\n")
