 
import pandas as pd #reading csv fiel
import numpy as np #array manupulation
import matplotlib.pyplot as plt #plotting figures
from keras.models import Sequential
from keras.layers import BatchNormalization, Conv2D, Activation, MaxPooling2D, Dense, GlobalAveragePooling2D, Dropout, Flatten
from keras import optimizers
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm

print("asdasd")