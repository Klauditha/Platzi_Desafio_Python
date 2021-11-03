def read():
    numbers = []
    with open("./archivos/number.txt","r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers) 


def write():
    names = ["Maria","Alej","Luis","Rocío"]
    #with open("./archivos/name.txt","w",encoding="utf-8") as f:
    with open("./archivos/name.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()


if __name__ == '__main__':
    run()