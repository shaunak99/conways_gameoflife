import json
import numpy as np
import gol_v2 as gol

if __name__ == "__main__":

    """
    There are 5 popular starting patterns to choose from. You can find more at
    https://playgameoflife.com/lexicon/tableself.
    An option for random starting pattern has also been provided.
    The patters are stored as .txt files and is loaded with the help of the
    config.json file.
    Number of generations to run is also configurable in config.json.
    """

    grid = []
    modef = None

    while modef == None:
        f=open('config.json')
        config_dict = json.load(f)

        print("Choose pattern:\n")
        for key in config_dict["options"]:
            print(key+". "+config_dict["options"][key]["name"])

        op = input()
        modef = config_dict["options"].get(op)

        if modef == None:
            print("Invalid Option. Please Re-enter.")
            continue
        else:
            modef=modef["file"]

        if modef != 1:
          with open(modef) as file:
              grid=[[int(digit) for digit in line.strip()] for line in file]
        else:
          grid = np.random.randint(0,2,(20,50))

    generations = config_dict["generations"]
    grid = np.array(grid)
    gol.run(grid,generations)
