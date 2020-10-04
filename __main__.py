# __main__.py

import sys
import generator
from importlib import resources  # Python 3.7+
from configparser import ConfigParser

#from reader import feed
#from reader import viewer

def main():
    """Begin here"""
    # Read package details from config file

    print("generata")

    cfg = ConfigParser()
    cfg.read_string(resources.read_text("generata", "config.txt"))
    version = cfg.get("package", "version")

    version = "0.0.1"
    print(version)

    # instantiate the class
    g = generator.Generator()

    # data definition
    datag = {
        'number_of_numerical_features': 2,
        'number_of_categorical_features': 0,
        'mean': 0,
        'stdev': 5,
        'decimals': 2,
        'samples': 10,
    }

    df = g.get_dataframe(datag)

    print(df)

if __name__ == "__main__":
    main()