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
        txt_path2 = path.join(self.sol, "PASSED_RUNS.txt")
        with open(txt_path, "w") as error_file:
            error_file.write("The following files have errors and cannot be plotted: ")

        with open(txt_path2, "w") as pass_file:
            pass_file.write("The following files have successfully been plotted: ")

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
                        with open(txt_path2, "a") as pass_file:
                            pass_file.write("\n" + file)

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

    def set_grid_ticks(self):
        """
        sets maximum number of ticks and formats grid.
        :return:
        """
        # set ticks based on a maximum number:
        self.ax.get_xaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
        self.ax.get_yaxis().set_major_locator(plticker.MaxNLocator(10, prune=None))
        self.ax.get_xaxis().set_minor_locator(plticker.MaxNLocator(50))
        self.ax.get_yaxis().set_minor_locator(plticker.MaxNLocator(50))

        # format ticks and rotate the labels:
        self.ax.grid(b=True, which='major', linestyle='-', linewidth='1.0', color='gainsboro', zorder=0,
                     figure=self.fig)
        self.ax.grid(b=True, which='minor', linestyle=':', linewidth='0.5', color='silver', zorder=0, figure=self.fig)

        plt.xticks(rotation=70)

    def add_scatter_spreadsheet(self, path_to_sheet: str, x: str, y: str, legend="", colour='darkgrey',
                                filter_condition: dict = None, X_value: int = None,
                                y_error: str = None, error_colour='silver', best_fit_line: bool = False,
                                scatter: bool = True, best_fit_line_filter: dict = None, mean=False):
        """
        Based on spreadsheet input (csv or excel), plot scatter plot on a figure belonging to the Graph() instance.
        Can be used to plot multiple datasets on the same graph
        :param path_to_sheet: full path as string including extension .csv or .xls*
        :param x: exact name of column in spreadsheet for the x data
        :param y: exact name of column in spreadsheet for the y data
        :param legend: legend label
        :param colour: of line and if selected, line of best fit

        :type filter_condition: dict
        :param filter_condition: name of spreadsheet column (dictionary key value) which is filtered for values (dictionary values).

        :param X_value: assumes filter condition is X(cm) and filter value is the X_value. For specialist spreadsheets only.
        :param y_error: column name for y error bars - if present will add error bars to plot
        :param error_colour: error bar colour
        :param best_fit_line: if True will add a line of best fit
        :return:
        """
        # adding arguments globally to function so that they can be modified based on user input combination (e.g input type):
        print("plotting graphs...")
        my_filter_condition = filter_condition
        data = pd.DataFrame()
        y_data = pd.Series
        x_data = pd.Series

        if X_value is not None:
            my_filter_condition['X(cm)'] = str(X_value)

        # if data input is an excel or csv spreadsheet:
        if 'xls' in path_to_sheet:
            data = pd.read_excel(path_to_sheet, path_to_sheet='Sheet1')
        elif 'csv' in path_to_sheet:
            data = pd.read_csv(path_to_sheet)

        if 'xls' or 'csv' in path_to_sheet:
            if my_filter_condition is None:
                x_data = data[x]
                x_data = x_data.astype('float64')
                y_data = data[y]
                y_data = y_data.astype('float64')
            else:
                new_data = pd.DataFrame(
                    data.loc[(data[list(my_filter_condition)] == pd.Series(my_filter_condition)).all(axis=1)])
                x_data = new_data[x]
                x_data = x_data.astype('float64')

                y_data = new_data[y]
                y_data = y_data.astype('float64')

        if mean is True:
            # convert data into numpy arrays:
            array_x, array_y = np.array(x_data), np.array(y_data)
            array_x = array_x.round(2)
            # sort x and y by x value
            order = np.argsort(array_x)
            xsort, ysort = array_x[order], array_y[order]

            # create a dataframe and add 2 columns for your x and y data:
            df = pd.DataFrame()
            df['xsort'] = xsort
            df['ysort'] = ysort
            # create new dataframe with no duplicate x values and corresponding mean values in all other cols:
            mean = df.groupby('xsort').mean()
            x_data = mean.index
            y_data = mean['ysort']

        if scatter == True:
            plt.scatter(x_data, y_data, color=colour, zorder=10, s=10, label=legend, figure=self.fig)

        if legend != "":
            plt.legend()

        if y_error is not None and my_filter_condition is not None:
            new_data = pd.DataFrame(
                data.loc[(data[list(my_filter_condition)] == pd.Series(my_filter_condition)).all(axis=1)])
            error = new_data[y_error]
            error = error.astype('float64')
            self.add_error_bar(x_data, y_data, error, error_colour)

        elif y_error is not None and my_filter_condition is None:
            error = data[y_error]
            error = error.astype('float64')
            self.add_error_bar(x_data, y_data, error, error_colour)

        if best_fit_line is True:
            if best_fit_line_filter is None:
                x_data = data[x]
                x_data = x_data.astype('float64')
                y_data = data[y]
                y_data = y_data.astype('float64')
                self.add_best_fit_line(x_data, y_data, colour=colour)

            else:
                new_data = pd.DataFrame(
                    data.loc[(data[list(best_fit_line_filter)] == pd.Series(best_fit_line_filter)).all(axis=1)])
                x_data = new_data[x]
                x_data = x_data.astype('float64')
                y_data = new_data[y]
                y_data = y_data.astype('float64')
                self.add_best_fit_line(x_data, y_data, colour=colour)

    def add_scatter_sol(self, solution: Solution, x: str, y: str, name="", legend="", colour='darkgrey',
                        filter_condition: dict = None, X_value: int = None, number_of_points=1, multip: int = 1,
                        scatter: bool = True, best_fit_line: bool = False):
        """

        :param solution: name of instance when generating the data from the Solution() class (used for chemkin output folder data)
        :param x: exact name of column for the x data
        :param y: exact name of column for the y data
        :param name: if present, will search and plot data from a specific .out file. Must remove .out file extension - just write the file name
        :param legend: legend label
        :param colour: colour of line and if selected, line of best fit

        :type filter_condition: dict
        :param filter_condition: name of spreadsheet column (dictionary key value) which is filtered for values (dictionary values

        :param X_value: assumes filter condition is X(cm) and filter value is the X_value.
        :param number_of_points: repressents n for plotting every nth point in the data. Use for very large datasets
        :param best_fit_line: if True will add a line of best fit
        :return:
        """
        my_filter_condition = filter_condition
        print("plotting graphs...")
        if X_value is not None:
            my_filter_condition['X(cm)'] = str(X_value)

        # input type is the name of a file/df stored in a dictionary:
        if name != "":
            df = solution.df_dict.get(name, 'no such value')
            if 'no such value' in df:
                raise IndexError("No file was found. Check the name doesn't contain a file extension")

            if my_filter_condition is None:
                x_data = df[x][(df.index % number_of_points == 1)]
                x_data = x_data.astype('float64')
                y_data = df[y][(df.index % number_of_points == 1)]
                y_data = multip * (y_data.astype('float64'))
            else:
                new_data = pd.DataFrame(
                    df.loc[(df[list(my_filter_condition)] == pd.Series(my_filter_condition)).all(axis=1)])
                x_data = new_data[x]
                x_data = x_data.astype('float64')
                y_data = new_data[y]
                y_data = multip * (y_data.astype('float64'))

        elif name == "":
            df_dict = solution.df_dict
            # for key, df in df_dict.items():
            df = pd.concat(df_dict)
            new_data = pd.DataFrame(
                df.loc[(df[list(my_filter_condition)] == pd.Series(my_filter_condition)).all(axis=1)])
            x_data = new_data[x]
            x_data = x_data.astype('float64')
            y_data = new_data[y]
            y_data = multip * (y_data.astype('float64'))
        else:
            raise IndexError("Conditions not recognised. Please provide more specific conditions for plotting.")

        if scatter == True:
            plt.scatter(x_data, y_data, color=colour, zorder=10, s=10, label=legend, figure=self.fig)

        if best_fit_line is True:
            self.add_best_fit_line(x_data, y_data, colour=colour)

        if legend != "":
            plt.legend()

    def add_best_fit_line(self, x, y, colour=None):
        """
        converts x and y data to np.array, sorts in order of x, converts to dataframe, removes duplicate x values and plots a polyfit line.
        :param x: x data list/set/Series
        :param y: x data list/set/Series
        :param colour: colour of line
        :return:
        """
        # convert data into numpy arrays:
        array_x, array_y = np.array(x), np.array(y)
        array_x = array_x.round(2)
        # sort x and y by x value
        order = np.argsort(array_x)
        xsort, ysort = array_x[order], array_y[order]

        # create a dataframe and add 2 columns for your x and y data:
        df = pd.DataFrame()
        df['xsort'] = xsort
        df['ysort'] = ysort
        # create new dataframe with no duplicate x values and corresponding mean values in all other cols:
        mean = df.groupby('xsort').mean()
        df_x = mean.index
        df_y = mean['ysort']

        if df_x.empty is False:
            # poly1d to create a polynomial line from coefficient inputs:
            trend = np.polyfit(df_x, df_y, 16)
            trendpoly = np.poly1d(trend)
            # plot polyfit line:
            plt.plot(df_x, trendpoly(df_x), linestyle=':', dashes=(6, 5), linewidth='1.3',
                     color=colour, zorder=9, figure=self.fig)

    def add_error_bar(self, x: pd.Series, y: pd.Series, y_error: pd.Series, colour):
        """
        adds error bars
        :param self:
        :param x: x data as Series/list/array
        :param y: y data as Series/list/array
        :param y_error: y error data as Series/list/array
        :param colour: colour of error bars
        :return:
        """
        plt.errorbar(x=x, y=y, yerr=y_error, fmt='none', color=colour, zorder=8,
                     figure=self.fig, elinewidth=1)

    def show_and_save(self, path_of_save_folder: str, name: str):
        """
        shows and saves the figure - must be called to show the figure at the end of plotting
        :param self:
        :param path_of_save_folder: save figures to this folder
        :param name: save figures under this name
        :return:
        """
        full_path = path.join(path_of_save_folder, name)
        plt.savefig(full_path, dpi=300, bbox_inches="tight")
        plt.close(self.fig)


class GraphSetAxis(Graph):
    """
    Make a new graph object. Same as graph class but axis and background can be specified.
    Plot lines are formatted so that they follow paper format - experiment results are single plot points (or dotted lines) and numerical results are smooth shaded lines.
    :param x_axis_label:
    :param y_axis_label:
    :param title: the title that will be set for the graph
    :param x_graph_size: default to almost square size 6 (increase number to change size ratio or increase resolution)
    :param y_graph_size: and default to almost square size 6.5 (increase number to change size ratio or increase resolution)
    """

    def __init__(self, x_axis_label: str, y_axis_label: str, title: str, x_graph_size: int = 6,
                 y_graph_size: int = 6.5):
        super().__init__(x_axis_label, y_axis_label, title, x_graph_size,
                     y_graph_size)

    def set_grid_ticks(self):
        """
        override original formatting for plot
        :return:
        """
        print("Calling sub class")
        self.ax.set_xlim(0.65, 1.35)
        self.ax.set_ylim(0)

        # set font family for plots:

        font = {'family': 'normal',
                'weight': 'bold',
                'size': 22}

        plt.rc('font', **font)
