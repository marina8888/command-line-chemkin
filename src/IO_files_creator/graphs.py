import matplotlib.pyplot as plt
from classes import InpGenerator

class Solution():
    """
    Solution class takes all files from solution folder and transfers all values after " SEARCH:  SUCCESS.  THE SOLUTION:" if it exists. If not, assume the run failed.
    Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
    Write the names of failed runs to a text file.
    """
    def __init__(self, path_to_solution_folder):
        self.sol=path_to_solution_folder

    def create_name1_name2(self):
        pass

    def sol_to_df(self):
        pass

    def all_sol_to_df(self):
        pass

    def failed_runs(self):
        pass

class Graphs():

