
def main():
    costumes = ["ghost", "witch", "elf", "ogre"]
    name = "elf"
    if name in costumes:
        costumes.remove(name)
    for item in costumes:
        print(item)
   
if __name__ == "__main__":
    main()