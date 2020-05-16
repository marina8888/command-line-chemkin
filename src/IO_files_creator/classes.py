"""
This file generates the input conditions that are parsed into the .inp file. This .inp file is the input file for the solver used in job.sh.
The input conditions change for every run/new set of experimental conditions that are numerically simulated.
This file takes in a values from 'Sheet1' of conditions, given a spreadsheet using template.xls format as included in the /notes directory.
"""
import pandas as pd
import numpy as np
import os.path
import re


class InpGenerator():

    def __init__(self, path_to_spreadsheet: str, path_to_inp_file: str):
        """
        :param path_to_spreadsheet: input data spreadsheet file path
        :param path_to_inp_file: input file path
        """
        self.sheet = path_to_spreadsheet
        self.inp = path_to_inp_file
        self.inp_name = os.path.basename(path_to_inp_file)
        self.content = []

        self.df = self.sheet_to_df()
        self.check_df_col()
        self.get_name()
        self.create_new_inp(4)

    def sheet_to_df(self):
        """
        Create dataframe from spreadsheet file, with a column for each parameter/input. Rejects excel files with duplicate columns.
        spreadsheet column headers and data types must be as documented/shown in notes excel template, and should be first filled with user's input conditions
        :param: None
        :return df: DataFrame
        """
        df = pd.read_excel(self.sheet, sheet_name='Sheet1')
        print("Reading input values from 'Sheet1' of your excel spreadsheet...")
        dup_cols: pd.Series = (df.columns[df.columns.duplicated(keep=False)])
        if dup_cols.empty == False:
            raise AssertionError('these duplicate columns need renaming: ' + str(dup_cols))

        return df

    def check_df_col(self):
        """
        Function to check that DataFrame has all the information (and in the right format). Will raise errors if there are any issues with the data.
        This includes any #REF #ERR type cells in the spreadsheet and wrongly typed cells. Also checks all columns contain positive integers.
        :return: None
        """
        bad_type = self.df.loc[:, self.df.dtypes != np.float64]
        bad_type = bad_type.loc[:, bad_type.dtypes != np.int64]

        if bad_type.empty is False:
            raise NameError('Columns: ' + str(bad_type.dtypes) + ' contain non-integer values')
        if self.df.isnull().values.any():
            raise NameError('There are columns with null values in your spreadsheet')

        for i in self.df.columns:
            if self.df[i].empty:
                raise NameError('Column ' + str(i) + ' is empty in your spreadsheet')

            other_bad_values = np.where(self.df[i] < 0)

            if len(other_bad_values[0]) != 0:
                raise NameError('Column ' + str(i) + ' has negative values in your spreadsheet')

    def get_name(self):
        """
        If name1 and name2 columns (which are used for naming solution.out files and filtering data) do not exist,
        create arbitary name1 and name2 columns.
        :return: None
        """
        default_names = []
        if not 'name1' in self.df.columns or not 'name2' in self.df.columns:
            for x in range(0, len(self.df), 1):
                default_names.append(x)
        if not 'name1' in self.df.columns:
            self.df['name1'] = default_names
        if not 'name2' in self.df.columns:
            self.df['name2'] = default_names

    def get_inp_name(self, row: int, round1: int = 2, round2: int = 2):
        """
        Creates a name for an input file.
        :param row: spreadsheet row number
        :param round1: rounding value for name1 column (WARNING: too low of a number might overwrite an input file due to duplicate names!)
        :param round2: rounding value for name2 column (WARNING: too low of a number might overwrite an input file due to duplicate names!)
        :return new_inp_name: a new name for the input file.
        """
        new_inp_file_name = str(round(self.df['name1'][row], round1)) + '__' + str(
            round(self.df['name2'][row], round2)) + '__' + self.inp_name
        return new_inp_file_name

    def create_new_inp(self, round_val: int = -1):
        """
        A function that generates a new input file based on a dataframe input, where column headers are the variables replaced.
        :param round_val:
        :return:
        """

        # open old input file and write each line to content:
        with open(self.inp, 'rt') as f:
            self.content = [line.strip() for line in f]
        row_num = 5
        # look up the spreadsheet column headers in the old inp file, extract the number in the corresponding row following it.
        # Replace this with a new number from a spreadsheet row_num
        with open('haha.inp', 'w') as new_f:
            for l in self.content:
                for col in enumerate(self.df):
                    if col[1] in l:
                        number_in_text = re.findall(r"\b(\d+(?:\.\d*)?|\.\d+)\b", l)
                        if len(number_in_text) == 0:
                            raise TypeError(
                                'please ensure that you have placeholder numerical values in your input file for all variables that you are modifying')
                        if len(number_in_text) != 1:
                            raise TypeError(
                                'ensure that inp file only contains one space seperated number per line (which is the variable value).')
                        if round_val is -1:
                            l = l.replace(" " + number_in_text[0] + " ", " " + str(self.df[col[1]][row_num]) + " ", 1)
                        else:
                            l = l.replace(" " + number_in_text[0] + " ",
                                          " " + str(round(float(self.df[col[1]][row_num]), round_val)) + " ", 1)
                new_f.write("\n" + l)
