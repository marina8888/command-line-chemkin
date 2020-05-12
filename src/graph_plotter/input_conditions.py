"""
This file generates the input conditions that are parsed into the .inp file. This .inp file is the input file for the solver.
The input conditions change for every run/new set of experimental conditions that are numerically simulated.
These definitions are covered in the stagnation_model_notes.
This file takes in a csv spreadsheet of conditions, given two potential csv input formats:

1. A spreadsheet using template.csv format as included in the /notes directory.

2. Workbook or BigWorkbook dataframe object in csv format created by the following repo:
https://github.com/marina8888/gas-analysis-dilution-method
...by running:
     [object_name] = Workbook('/file-to-path/filename.xlsm', [row-number-that-data-starts-on],
                     ['string-list-of-ppmv-measured-gases'], ['string-list-of-%-measured-gases'])
    [object_name].df.to_csv('../file-to-path/file-name.csv')" in the main.py file.
Most suitable if user has experimental data was collected in the excel template format provided by marina8888/gas-analysis-dilution-method

"""

