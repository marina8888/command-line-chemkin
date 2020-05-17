import matplotlib.pyplot as plt
from classes import InpGenerator
import pandas as pd
from os import listdir, path

class SolutionwithX():
    """
    Solution class takes all files from solution folder and transfers all values after if it exists. If not, assume the run failed.
    Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
    Write the names of failed runs to a text file.
    """
    def __init__(self, path_to_solution_folder):
        self.sol=path_to_solution_folder
        self.df_dict={}

    def failed_runs(self):
        """
        prints all failed files to a text file and cleans the other files ready to be transferred to a dataframe.
        :return:
        """
        for file in listdir(self.sol, "r"):
            if
        pass

    def import_sol(self):
        """
        populate a dictionary of dataframes, where the filename is the key.
        :return:
        """
        for file in listdir(self.sol, "r"):
            name=file.strip(".out")
            self.df_dict[name]=pd.DataFrame(file)

    def create_name1_name2(self):
        pass

    def sol_to_df(self):
        pass

    def all_sol_to_df(self):
        pass

class SolutionAtX():
 pass

class Graphs():
pass
