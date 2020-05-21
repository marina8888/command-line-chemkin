import pandas as pd
from os import listdir, path
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
# set a global style for all graphs:
plt.style.use('seaborn-notebook')


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
        self.sol_to_df()

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

    def add_name_cols(self, out_file_name, df: pd.DataFrame):
        """
        Add name1 and name2 columns to dataframe for filtering purposes. Use the actual name of the file to extract them.
        :param out_file_name: The name of solution .out file for processing
        :param df: The dataframe.
        :return:
        """
        name = out_file_name.strip(".out")
        name1 = name.split('__')[0]
        name2 = name.split('__')[1]
        df['name1'] = name1
        df['name2'] = name2
        return df

    def sol_to_df(self):
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
                    name = file.strip('.out')
                    new_df = self.add_name_cols(file, new_df)
                    self.df_dict[name] = new_df


class Graph():
    def __init__(self, x_axis_label: str, y_axis_label: str, title: str, x_graph_size: int = 6,
                 y_graph_size: int = 6.5):
        """
        Initialise a graph, based on object arguments. One figure is created per new graph object.
        Any data added will be plotted on same graph. Call the add_scatter() and add_line_of_best_fit() for every set of data you intend to plot.
        :param x_axis_label:
        :param y_axis_label:
        :param title: the title that will be set for the graph
        :param x_graph_size: default to almost square size 6 (increase number to change size ratio or increase resolution)
        :param y_graph_size: and default to almost square size 6.5 (increase number to change size ratio or increase resolution)
        """
        self.fig = plt.figure(figsize=(x_graph_size, y_graph_size))

        # get access to axies functions:
        self.ax = self.fig.gca()

        # set format variables and format the figure:
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.title = title

        self.add_format()
        self.set_grid_ticks()


    def add_format(self):
        """
        Format graph. Add title, axies, tight layout, padding and grid.
        :return:
        """
        # add title, names and layout:
        plt.title(self.title, pad=15, figure=self.fig)
        plt.xlabel(self.x_axis_label, figure=self.fig)
        plt.ylabel(self.y_axis_label, figure=self.fig)
        plt.tight_layout()

    def set_grid_ticks(self):
        # set ticks based on a maximum number:
        self.ax.get_xaxis().set_major_locator(plticker.MaxNLocator(10, prune = None))
        self.ax.get_yaxis().set_major_locator(plticker.MaxNLocator(10, prune = None))
        self.ax.get_xaxis().set_minor_locator(plticker.MaxNLocator(50))
        self.ax.get_yaxis().set_minor_locator(plticker.MaxNLocator(50))

        self.ax.grid(b=True, which='major', linestyle='-', linewidth='1.0', color='gainsboro', zorder=0, figure=self.fig)
        self.ax.grid(b=True, which='minor', linestyle=':', linewidth='0.5', color='silver', zorder=0, figure=self.fig)
        # plt.gca().yaxis.set_major_formatter(plticker.StrMethodFormatter('{x:.1f}'))
        plt.xticks(rotation=70)


    def add_scatter_spreadsheet(self, path_to_sheet: str, x: str, y: str, legend="", colour='darkgrey',
                                filter_condition=None,
                                filter_value=None, X_value=None, round_filter_to_dp: int = None):
        # adding arguments globally to function so that they can be modified based on user input combination (e.g input type):
        my_filter_condition = filter_condition
        my_filter_value = filter_value
        data = pd.DataFrame()

        if X_value is not None:
            my_filter_condition = 'X(cm)'
            my_filter_value = X_value

        # if data input is an excel or csv spreadsheet:
        if 'xls' in path_to_sheet:
            data = pd.read_excel(path_to_sheet, path_to_sheet='Sheet1')
        elif 'csv' in path_to_sheet:
            data = pd.read_csv(path_to_sheet)

        if 'xls' or 'csv' in path_to_sheet:
            if round_filter_to_dp is not None:
                series = data[my_filter_condition]
                data[my_filter_condition] = series.round(decimals=round_filter_to_dp)
            if filter_condition is None:
                x_data = data[x]
                x_data = x_data.astype('float64')
                y_data = data[y]
                y_data = y_data.astype('float64')
            else:
                x_data = (data[x][(data[filter_condition] == filter_value)])
                x_data = x_data.astype('float64')
                y_data = (data[y][(data[filter_condition] == filter_value)])
                y_data = y_data.astype('float64')

        # for if an input is a dictionary of dataframes:
        plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)
        if legend != "":
            plt.legend(loc="upper left")


    def add_scatter_sol(self, solution: Solution, x: str, y: str, name="", legend="", colour='darkgrey', filter_condition=None,
                        filter_value=None, X_value=None, round_filter_to_dp: int = None, number_of_points = 20):
        # input type is the name of a file/df stored in a dictionary:
        if name != "":
            df = solution.df_dict.get(name, 'no such value')
            if df is 'no such value':
                IndexError("No file was found. Check the name doesn't contain a file extension")

            if filter_condition is None:
                x_data = df[x][(df.index % number_of_points == 1)]
                x_data = x_data.astype('float64')
                y_data = df[y][(df.index % number_of_points == 1)]
                y_data = y_data.astype('float64')
            else:
                x_data = (df[x][(df[filter_condition] == filter_value)])
                x_data = x_data.astype('float64')
                y_data = (df[y][(df[filter_condition] == filter_value)])
                y_data = y_data.astype('float64')

        plt.scatter(x_data, y_data, color=colour, zorder=10, s=20, label=legend, figure=self.fig)
        if legend != "":
            plt.legend(loc="upper left")



    def add_best_fit_line(self, path_to_sheet, x, y, x_error=None, y_error=None, legend=None, colour=None,
                          filter_condition=None,
                          filter_value=None):
        # use self.fig as a parameter
        pass

    def show_and_save(self, path_of_save_folder: str, name: str):
        plt.show()
        plt.savefig(path_of_save_folder + name)
