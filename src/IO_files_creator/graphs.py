import matplotlib.pyplot as plt
import pandas as pd
from os import listdir, path

class Solution():
    """
    Solution class takes all files from solution folder and transfers all values after if it exists. If not, assume the run failed.
    Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
    Write the names of failed runs to a text file.
    """
    def __init__(self, path_to_solution_folder):
        self.sol=path_to_solution_folder
        self.df_dict={}
        self.failed_runs()
        # self.import_sol()

    def failed_runs(self):
        """
        prints all failed files to a text file and cleans the other files ready to be transferred to a dataframe.
        :return:
        """
        for file in listdir(self.sol):
            full_path = path.join(self.sol, file)
            with open(full_path, "r") as f:
                lines = f.readlines()
                if not any("ERROR" in s for s in lines):
                    whole_doc = '\n'.join(lines)
                    whole_doc.split(' TWOPNT: ', 1)[0]
                    with open(full_path, "w") as f:
                         f.write(whole_doc)

    def import_sol(self):
        """
        populate a dictionary of dataframes, where the filename is the key. Add name1 and name2 as a filtering parameter.
        :return:
        """
        for file in listdir(self.sol, "r"):
            print(file)
            name=file.strip(".out")
            df=pd.DataFrame(file)

            file_name_as_list = file.split('__')
            name1 = file_name_as_list[0]
            name2 = file_name_as_list[1]
            df['name1'] = name1
            df['name2'] = name2

            self.df_dict[name]=df

class SolutionAtX():
    def __init__(self, path_to_solution_folder):
        self.sol=path_to_solution_folder
        self.df=pd.DataFrame()

    def failed_runs(self):
        for file in listdir(self.sol, "r"):
            pass

    def import_sol(self):
        pass

# class Graph():
#     def __init__(self):
#         fig=fig #create figure
#
#
# class ExpGraph(Graph):
#     def __init__(self):
#         super.__init__():


