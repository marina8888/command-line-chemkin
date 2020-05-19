import matplotlib.pyplot as plt
import pandas as pd
from os import listdir, path
import re
import ast


class Solution():
    """
    This takes a folder of .out files amnd converts them to a dictionary of pandas DataFrames.
    Create 2 new dataframe columns for name1 and name2 as additional filtering criteria.
    Write the names of failed runs to a file in the same folder called ERROR_RUNS.txt as these cannot be plotted.
    """

    def __init__(self, path_to_solution_folder):
        self.sol = path_to_solution_folder

        # dictionary to store dataframes:
        self.df_dict = {}
        self.failed_runs()
        self.import_sol()

    def filter_txt(self, lines, add_X_col: bool = False):
        """
        Use RegEx expression to find DataFrame col values and data and save them as two lists from .out file.
        :param lines: .out file formatted as '/n' seperated list of strings
        :param add_X_col: True adds an extra X(cm) column header.
        :return:
        """
        col_list = []
        key_list = []
        col_tuple = [()]
        previous: str = ""
        row = []
        for line in enumerate(lines):
            if line[1].startswith('    1   '):
                # get list of keys from row above the row starting with "    1   "
                new_key_list = re.findall(r"\b[A-Z]{1}[\S]*", previous)
                if add_X_col == True:
                    new_key_list.insert(0, 'X(cm)')
                new_key_list.insert(0, "Index")
                key_list = new_key_list

            # get list of columns from the row starting with "    1   " onwards until the next newline and format
            if not line[1].isspace():
                col_tuple = re.findall(r"([-+]?[\d]+[\.]?[\d]*[E]?[-+]?[\d]+\b)|\s([\d]+)\s", line[1])
                if col_tuple != []:
                    row = [tup[0] or tup[1] for tup in col_tuple]
                    col_list.append(row)

            previous = line[1]

        return key_list, col_list

    def failed_runs(self):
        """
        prints all failed files to a text file and transfers all other files to a DataFrame. Initialises an ERROR_RUNS.TXT file.
        Writes all file names with errors to these files instead of converting them to a DataFrame.
        :return:
        """
        new_df = pd.DataFrame()

        # initalise an error file:
        txt_path = path.join(self.sol, "ERROR_RUNS.txt")
        with open(txt_path, "w") as error_file:
            error_file.write("The following files have errors and cannot be plotted: ")

        # go through all .out files in solutions folder:
        for file in listdir(self.sol):
            if file.endswith(".out"):
                full_path = path.join(self.sol, file)

                # readlines and if ERROR present in the file, write the name of file to error_file, otherwise create dataframe with data:
                with open(full_path, "r") as f:
                    lines = f.readlines()
                    if any("ERROR" in s for s in lines):
                        with open(txt_path, "a") as error_file:
                            error_file.write("\n" + file)
                    else:
                        whole_doc = ' '.join(lines)
                        whole_doc = whole_doc.split(' TWOPNT: ', 1)[0]

                        # create new dataframe and a super new dataframe for every slice of data seperated by 'MOLE FRACTION'
                        i = 0
                        filtered_lines = whole_doc.split("MOLE FRACTION")
                        for i in range(len(filtered_lines)):
                            split_filtered = filtered_lines[i].split('\n')

                            if i == 0:
                                key_list, col_list = self.filter_txt(split_filtered, add_X_col=False)
                                new_df = pd.DataFrame(col_list, columns=key_list)
                            else:
                                # merge all successive dataframes to inital dataframe on X(cm) as merge column:
                                key_list, col_list = self.filter_txt(split_filtered, add_X_col=True)
                                super_new_df = pd.DataFrame(col_list, columns=key_list)
                                super_new_df.drop('Index', axis=1, inplace=True)
                                new_df = new_df.merge(super_new_df, on='X(cm)')
                    self.df_dict[file] = new_df
                    print(self.df_dict[file])

    def import_sol(self):
        """
        populate a dictionary of dataframes, where the filename is the key. Add name1 and name2 as a filtering parameter.
        :return:
        """
        for file in listdir(self.sol):
            name = file.strip(".out")
            txt_name = name + ".txt"
            txt_full_path = path.join(self.sol, txt_name)
            df = pd.DataFrame([ast.literal_eval(line) for line in open(txt_full_path)])
            file_name_as_list = file.split('__')
            name1 = file_name_as_list[0]
            name2 = file_name_as_list[1]
            df['name1'] = name1
            df['name2'] = name2

            self.df_dict[name] = df


class Graph():
    def __init__(self, x_graph_size, y_graph_size):
        self.fig = plt.figure(x_graph_size, y_graph_size)

    def add_format(self, x_name, y_name, title):
        pass

    def add_scatter_dict(self, path_to_sheet, x, y, legend=None, colour=None, filter_condition=None, filter_value=None):
        # use self.fig as a parameter
        pass

    def add_best_fit_line(self, path_to_sheet, x, y, xerr, yerr, legend=None, colour=None, filter_condition=None,
                          filter_value=None):
        # use self.fig as a parameter
        pass
