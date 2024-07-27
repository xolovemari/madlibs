from opcoes import daenerys, mari, mia_goth
import random

if __name__ == "__main__":
    m = random.choice([daenerys, mari, mia_goth])
    m.madlib()