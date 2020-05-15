"""
This file generates the input conditions that are parsed into the .inp file. This .inp file is the input file for the solver used in job.sh.
The input conditions change for every run/new set of experimental conditions that are numerically simulated.
These definitions are covered in the stagnation_model_notes.
This file takes in a spreadsheet of conditions, given a spreadsheet using template.xls format as included in the /notes directory.
"""
import pandas as pd
import numpy as np

class ChemkinModel():

    def __init__(self, path_to_spreadsheet: str, path_to_inp_file: str):
        """
        :param path_to_spreadsheet: input data spreadsheet file path
        :param path_to_inp_file: input file path
        """
        self.sheet = path_to_spreadsheet
        self.inp = path_to_inp_file
        self.df = self.sheet_to_df()
        self.check_df_col()

    def sheet_to_df(self):
        """
        Create dataframe from spreadsheet file, with a column for each parameter/input. Rejects excel files with duplicate columns.
        spreadsheet column headers and data types must be as documented/shown in notes excel template, and should be first filled with user's input conditions
        :param: None
        :return df: DataFrame
        """
        df = pd.read_excel(self.sheet, sheet_name = 'Sheet1')

        dup_cols: pd.Series = (df.columns[df.columns.duplicated(keep=False)])
        if dup_cols.empty == False:
            raise AssertionError('these duplicate columns need renaming: ' + str(dup_cols))

        return df


    def generate_new_inp(df: pd.DataFrame, row_number: int, path_to_inp_file: str):
        """
        :param df:
        :param row_number: take data from this row
        :param path_to_inp_file: Use the stagnation_template.inp file for the stagnation flame model, included in /chemkin_launch_files directory.
        :return: None
        """
        with open(path_to_inp_file, 'r') as file:
            filedata = file.read()

        # replace input file data with a new value:

        filedata = filedata.replace('ram', 'abcd')

        # Write the file out again
        with open(path_to_inp_file, 'w') as file:

            file.write(filedata)


    def check_df_col(self):
        """
        Function to check that DataFrame has all the information (and in the right format). Will raise errors if there are any issues with the data.
        This includes any #REF #ERR type cells in the spreadsheet and wrongly typed cells. Also checks all
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

            if len(other_bad_values[0])!=0:
                raise NameError('Colummn ' + str(i) + ' has negative values in your spreadsheet')

