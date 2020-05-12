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

Then open the resulting .csv file and remove [‚ÑÉ] from the T1-T9 columns as .csv conversion corrupted this symbol. Rename column A to 'i'.
Most suitable if user already has experimental data was collected in the excel template format provided by marina8888/gas-analysis-dilution-method

"""
import pandas as pd


def csv_to_df(path_to_csv_file: str):
    """
    Create dataframe from csv file, with a column for each parameter/input. Rejects csv files with duplicate columns or in the wrong format
    :param path_to_csv_file: csv column headers and data types must be as documented/shown in notes csv template, and should be first filled with user's input conditions
    :return df: DataFrame
    """
    df = pd.read_csv(path_to_csv_file, header=0)

    dup_cols: pd.Series = (df.columns[df.columns.duplicated(keep=False)])
    if dup_cols.empty == False:
        raise AssertionError('these duplicate columns need renaming: ' + str(dup_cols))

    return df


def generate_new_inp(df: pd.DataFrame, row_number: int, path_to_inp_file: str):
    """
    Replace stagnation flame reactor model input (.inp) file to use conditions from a specific row of the dataframe.
    Modify this function if writing modifying input file for a different flame reactor model or using a different format.
    :param df:
    :param row_number: take data from this row
    :param path_to_inp_file: Use the stagnation_template.inp file for the stagnation flame model, included in /chemkin_launch_files directory.
    :return: None
    """
    inp_vals = ['PRES', 'TINF', 'TINL', 'TMAX', 'TINL C1_Inlet1', 'UINL C1_Inlet1', 'REAC C1_Inlet1 N2',
                'REAC C1_Inlet1 NH3', 'REAC C1_Inlet1 CH4', 'REAC C1_Inlet1 O2']
    corresponding_df_col_headers = ['pressure_atm', ]
    with open(path_to_inp_file, 'r') as file:
        filedata = file.read()

    # replace input file data with a new value:

    filedata = filedata.replace('ram', 'abcd')

    # Write the file out again
    with open(path_to_inp_file, 'w') as file:
        file.write(filedata)
