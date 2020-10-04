# Generata - Generate Data

A Python package to generate data of your choice!


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
            'number_of_categorical_features': 0,
            'mean': 0,
            'stdev': 5,
            'decimals': 2,
            'samples': 10,
        }
```


Create your dataframe:

```
df = g.get_dataframe(params)
```


