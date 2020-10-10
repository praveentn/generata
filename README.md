# Generata - Generate Data

A Python package to generate data of your choice!

## <i> work-in-progress

### Dependencies:

+ Python (3.8+)


Install `generata` on your system using:

```
pip install generata
```


### Usage:

Importing the library: 

```
import generata
from generata import generator as gr
```


Instantiate the class:

```
g = gr.Generator()
```


Initialize the parameters:

```
params = {
        'number_of_numerical_features': 2,
        'number_of_categorical_features': 3,
        'mean': 0,
        'stdev': 5,
        'decimals': 2,
        'samples': 10,
        'number_of_categories': 3,
       }
```


Create your dataframe:

```
df = g.get_dataframe(params)
```


