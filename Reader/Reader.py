''' File Reads the .txt Files with the eyedata'''
import os
import numpy as np
import pandas as pd



class Reader:
    Num_Files = 0
    panda_columns_names = ""
    Eye_Data_Path = ""
    File_List = []
    def __init__(self, Source_Path):
        self.Eye_Data_Path = Source_Path
        self.set_column_names()
        # We First Count How Many Files There Are In our List Data
        self.count_num_files()
        print("Number of Files:", self.Num_Files)
        # Load the Files into Panda
        ### Needs to Be called
    def count_num_files(self):
        count = 0                                                                                                       # Starting Count Index
        for file in os.listdir(self.Eye_Data_Path):                                                                     # Count and Get the Filenames of All Files in the Directory
            self.File_List.append(file)                                                                                 # Save the Filenames in the Eye Data Directory
            count += 1                                                                                                  # Update Index
        self.Num_Files = count                                                                                          # Update Global Count Variable
    def set_column_names(self):
        self.panda_columns_names = ['Engagement','Average Blink Rate','Focus Ratio', 'Average Focus Deviation Rate', 'Number of Focused Fixations', 'Mean Focused Fixation Duration',
                                    'Median Focused Fixation Duration', 'Time to First Fixation', 'RFDSD', 'Standard Deviation (X)', 'Standard Deviation (Y)',
                                    'Standard Distance (XY)', 'Number of Saccades', 'Mean Focused Saccade Amplitude', 'Median Focused Saccade Amplitude']
    def load_file(self):
        dataframe = pd.DataFrame()                                                                            # Create Empty Dataframe
        for file in self.File_List:                                                                                     # Loop Through All Files
            new_file_name = self.Eye_Data_Path + "/" + file                                                             ## Update File Name for Correct Path
            new_data = np.loadtxt(new_file_name, usecols=0)                                                             ## Load Column Using Numpy Array
            new_panda = pd.DataFrame(new_data).T                                                                        ## Transpose to Correct Format
            dataframe = dataframe.append(new_panda)                                                                     ## Create dataFrame
        dataframe.columns = self.panda_columns_names                                                                    ## Return Datafram
        return dataframe
    def load_file_noise(self):
        dataframe = pd.DataFrame()                                                                            # Create Empty Dataframe
        for file in self.File_List:                                                                                     # Loop Through All Files
            new_file_name = self.Eye_Data_Path + "/" + file                                                             ## Update File Name for Correct Path
            new_data = np.loadtxt(new_file_name, usecols=0)                                                             ## Load Column Using Numpy Array
            ## We need to Call Noise
            ## Add Noise to the loaded data
            for i in range(1,len(new_data)):
                noise = np.random.uniform(0, 0.1)
                new_data[i] += noise
            new_panda = pd.DataFrame(new_data).T                                                                        ## Transpose to Correct Format
            dataframe = dataframe.append(new_panda)                                                                     ## Create dataFrame
        dataframe.columns = self.panda_columns_names                                                                    ## Return Datafram
        return dataframe