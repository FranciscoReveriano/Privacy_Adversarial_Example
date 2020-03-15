''' Main File to Run The Simulation
Duke University Pratt School of Engineering
By: Francisco Reveriano and Tim Scargill
March 2020
'''
import numpy as np
import pandas as pd
import sklearn
from Reader.Reader import *


# Call the Reader To Read All Privacy Documents
Eye_Data_Path = "/home/franciscoAML/Documents/Privacy_Adversarial_Example/Eye_Data"
Dataframe = Reader(Eye_Data_Path).load_file()
print(Dataframe)