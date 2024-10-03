# README

fico is a small module to calculate Fitness and Complexity according to the algorithm defined in 
Tacchella et al, A New Metrics for Countries' Fitness and Products' Complexity
Scientific Reports volume 2, Article number: 723 (2012).

## Setup
It should probably install automatically.

## Installation

fico can be installed via pip:
'''
pip install git+https://github.com/fabiosaracco/lou_reed.git
'''
## Contents (so far)

* setup.py: the setup, easy as this.
* lou_reed/lou_reed.py: calculate fitness and complexity and reorder matrices

## Licence

MIT

# How it works
fico module is pretty simple. First load all fucntions in the module:
'''
from fico import
'''
If m is the biadjacency matrix of a bipartite network (in the present version, it is a numpy array), then 
'''
fico(m)
'''
returns the fitnesses of the rows and the complexity of the columns. 


If you want to reorder the biadjacency matrix m in term of fitness and complecity, then 
'''
bam_fico_or(m)
'''
returns the matrix m opportunely reordered. If you want to get the argsort used to reorder the matrix, just turn on the return_argsorts option:
'''
bam_fico_or(m, return_argsorts=True)
'''


