# __main__.py

import sys
import generator
from importlib import resources  # Python 3.7+

def main():
    """Begin here"""

    # instantiate the class
    g = generator.Generator()

    # data definition
    datag = {
        'number_of_numerical_features': 2,
        'number_of_categorical_features': 3,
        'mean': 0,
        'stdev': 5,
        'decimals': 2,
        'samples': 10,
        'number_of_categories': 3,
    }

    df = g.get_dataframe(datag)

    print(df)

if __name__ == "__main__":
    main()