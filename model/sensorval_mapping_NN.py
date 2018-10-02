import tensorflow as tf
import numpy as np
import pandas as pd
from pandas import DataFrame

raw = pd.read_csv('../data/sensorval_rand0_0913.csv', header=0, index_col=0).fillna(0).values




print (raw[0:3])
