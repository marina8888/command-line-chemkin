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
        Initalise a parent class for all flame models to inherit from.
        Use inp_vals and corresponding_df_col_headers to define a string list of input variables and their respective col headers in the spreadsheet.
        :param path_to_spreadsheet: input data spreadsheet file path
        :param path_to_inp_file: input file path
        """
        self.sheet = path_to_spreadsheet
        self.inp = path_to_inp_file
        self.df = self.sheet_to_df()
        self.inp_vals: str = []

    def sheet_to_df(self):
        """
        Create dataframe from spreadsheet file, with a column for each parameter/input. Rejects excel files with duplicate columns.
        spreadsheet column headers and data types must be as documented/shown in notes excel template, and should be first filled with user's input conditions
        :param: None
        :return df: DataFrame
        """
        df = pd.read_excel(self.sheet, sheet_name = 'Sheet1', header = 0)

        dup_cols: pd.Series = (df.columns[df.columns.duplicated(keep=False)])
        if dup_cols.empty == False:
            raise AssertionError('these duplicate columns need renaming: ' + str(dup_cols))

        return df



class BurnerStabilizedStagnationFlame(ChemkinModel):
    def __init__(self, path_to_spreadsheet: str, path_to_inp_file: str):
        super().__init__(path_to_spreadsheet, path_to_inp_file)

        self.inp_vals = ['PRES', 'TINL StagPlane', 'TMAX', 'TINL C1_Inlet1', 'UINL C1_Inlet1',
                         'REAC C1_Inlet1 NH3', 'REAC C1_Inlet1 CH4', 'REAC C1_Inlet1 O2', 'REAC C1_Inlet1 N2']
        self.check_df_col()



    def generate_new_inp(df: pd.DataFrame, row_number: int, path_to_inp_file: str):
        """
        Replace stagnation flame reactor model input (.inp) file to use conditions from a specific row of the dataframe.
        Modify this function if writing modifying input file for a different flame reactor model or using a different format.
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
        for i in self.inp_vals:
            if self.df[i].empty:
                raise NameError('Column ' + str(i) + ' is empty in your spreadsheet')
            if self.df.columns.to_series().groupby(self.df.dtypes).groupsnp.float64 or np.int64 is False:
                raise NameError('Column ' + str(i) + ' contains non-integer values')
            if self.df.isnull().values.any():
                print(self.df[i])
                raise NameError('Column ' + str(i) + ' has null values in your spreadsheet')
            if (self.df[self.df[i]>=0]).empty:
                print(self.df[i]>0)
                raise NameError('Colummn ' + str(i) + ' has negative values in your spreadsheet')
            # for row in range(0,len(self.df),1):
            #      if self.df.iloc[row][i] <= 0 or self.df.dtypes(self.df.iloc[i]) is not int:
            #         raise TypeError('Your column' + str(i) + 'contains invalid data')
