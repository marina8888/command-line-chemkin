"""
This file generates the input conditions that are parsed into the .inp file. This .inp file is the input file for the solver used in job.sh.
The input conditions change for every run/new set of experimental conditions that are numerically simulated.
These definitions are covered in the stagnation_model_notes.
This file takes in a csv spreadsheet of conditions, given two potential csv input formats:

1. A spreadsheet using template.csv format as included in the /notes directory.

2. An object of class Workbook or BigWorkbook (created by the following repo), saved in csv format:
https://github.com/marina8888/gas-analysis-dilution-method

...by running in the main.py file:
     object_name = Workbook('/file-to-path/filename.xlsm', row-number-that-data-starts-on,
                     ['string-list-of-ppmv-measured-gases'], ['string-list-of-%-measured-gases'])
    create_workbook.create_workbook(object_name)
    object_name.df.to_csv('../file-to-path/file-name.csv')" in the main.py file.

 Rename column A to Tmax and add adiabatic temperatures.
Most suitable if user already has experimental data was collected in the excel template format provided by marina8888/gas-analysis-dilution-method

"""
import pandas as pd


class ChemkinModel():

    def __init__(self, path_to_csv_file: str, path_to_inp_file: str):
        """
        Initalise a parent class for all flame models to inherit from.
        Use inp_vals and corresponding_df_col_headers to define a string list of input variables and their respective col headers in the spreadsheet.
        :param path_to_csv_file: input data spreadsheet file path
        :param path_to_inp_file: input file path
        """
        self.csv = path_to_csv_file
        self.inp = path_to_inp_file
        self.df = self.csv_to_df()
        self.inp_vals: str = []
        self.corresponding_df_col_headers: str = []

    def csv_to_df(self):
        """
        Create dataframe from csv file, with a column for each parameter/input. Rejects csv files with duplicate columns.
        csv column headers and data types must be as documented/shown in notes csv template, and should be first filled with user's input conditions
        :param: None
        :return df: DataFrame
        """
        df = pd.read_csv(self.csv, header=0)

        dup_cols: pd.Series = (df.columns[df.columns.duplicated(keep=False)])
        if dup_cols.empty == False:
            raise AssertionError('these duplicate columns need renaming: ' + str(dup_cols))

        return df

    def check_df_col(self):
        """
        Function to check that DataFrame has all the information (and in the right format). Will raise errors if there are any issues with the data.
        :return: None
        """


class BurnerStabilizedStagnationFlame(ChemkinModel):
    def __init__(self, path_to_csv_file: str, path_to_inp_file: str):
        super().__init__(path_to_csv_file, path_to_inp_file)

        self.inp_vals = ['PRES', 'TINL StagPlane', 'TMAX', 'TINL C1_Inlet1', 'UINL C1_Inlet1',
                         'REAC C1_Inlet1 NH3', 'REAC C1_Inlet1 CH4', 'REAC C1_Inlet1 O2', 'REAC C1_Inlet1 N2', ]
        self.corresponding_df_col_headers = ['pressure_atm', 'Tw[K]', 'Tmax', 'T1', 'Uout[m/s]', 'NH3upper actual',
                                             'CH4upper actual',
                                             'Air upper actual', 'Air upper actual']
        self.add_inp_col_to_df()

    def add_inp_col_to_df(self):
        """
        Add columns to dataframe to include (the new) columns needed for generating an input file for this model.
        If importing from BigWorkbook/Workbook class, the column headers and data will be changed into the template format.
        :param: None
        :return: None
        """
        if self.df['PRES'] is None and self.df['Actual Room Pressure in Mpa'] is not None:
            self.df.rename(columns={'Actual Room Pressure in Mpa': 'PRES'})
            self.df['PRES'] = self.df['PRES'] * 9.86923

        if (self.df['TMAX'] and self.df['TINL C1_Inlet1'] and self.df['UNIL C1_Inlet1'] and self.df['TINL StagPlane']) is None and (
                self.df['Tmax'] and self.df['T1[‚ÑÉ]'] and self.df['Uout[m/s]'] and self.df['Tw[K]']) is not None:
            self.df.rename(columns={'Tmax': 'TMAX', 'T1[‚ÑÉ]':'TINL C1_Inlet1', 'Uout[m/s]': 'UNIL C1_Inlet1', 'Tw[K]': 'TINL StagPlane'})

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
