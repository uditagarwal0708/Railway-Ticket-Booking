import os

def read_file():
    if os.path.exists("tickets.txt") == False:
        return [] 
    
    lst = []
    
    f = open("tickets.txt", "r")
    data = f.readlines()
    f.close()
    
    for x in data:
        l = x.strip() 
        if l == "": 
            continue 
            
        spl = l.split(",") 
        
        # Temp dictionry to hold row data
        temp = {
            "pnr": int(spl[0]),
            "name": spl[1],
            "age": int(spl[2]),
            "src": spl[3],
            "dest": spl[4],
            "dt": spl[5]
        }
        lst.append(temp)
        
    return lst

def write_file(lst):
    f = open("tickets.txt", "w")
    
    for i in lst:
        line = str(i['pnr']) + "," + i['name'] + "," + str(i['age']) + "," + i['src'] + "," + i['dest'] + "," + str(i['dt']) + "\n"
        f.write(line)
        
    f.close()