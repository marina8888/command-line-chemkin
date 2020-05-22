# Command Line CHEMKIN

## Overview
When conducting combustion analysis with CHEMKIN software, often a range of input conditions need to be tested. 

This code accelerates this process. The user can input a spreadsheet with all required chemkin conditions (or values aquired from an experiment). These values can be used to automatically generate input files and launch all the files to chemkin through the command line.  

This code also helps avoid the process of sorting, joining and filtering many excel spreadsheets, by coverting a folder of CHEMKIN solution.out files so that they can easily be plotted or saved to one processed excel spreadsheet. Filtering data for a certain X value (reaction chamber depth) across many files or by other parameters (including custom added parameters) is possible. Plotting options allow for the selection of a legend, colour settings and for the numerical results to be plotted against experimental results. 

Please note that only the generation of the input.inp file is considered in the script. The mechanism, thermal, transport and .dtd files for the considered flame should be acquired from the author of the mechanism or a reputable database (e.g GRI-Mech 3.0). 

Also, please note that this code is a personal open-source project and is intended to act as a helper tool for users that already have licenses and an installation of CHEMKIN software. This project is not created by ANSYS and is no way affiliated with this company. It is a personal project and not intended to perform to commerical standards. 

## Main Libraries Used
- pandas and numpy for converting data and filtering data (from .out format)
- matplotlib for plotting data
- pdocs for generating documentation (in progress...)

## To Install and Use
1. Install Python3 (if you havn't installed it before) : <https://www.python.org/downloads/>

2. Install pip (if you havn't installed it before) by typing `pip install pip` in MacOS. For further information: <https://pypi.org/project/pip/> ; or in Windows use `python get-pip.py`. For further information: <https://www.liquidweb.com/kb/install-pip-windows/>

3. If using a Windows computer, set up git for your operating system by following the video tutorials: <https://confluence.atlassian.com/bitbucket/clone-a-repository-223217891.html>. If MacOS, git should already be installed. 

4. Go to the directory where you want to save the project folder by typing : `cd path/to/directory/`

5. In your terminal/command line type : `git clone https://github.com/marina8888/command-line-chemkin.git`

6. If you do not have an environment module that you already use, it is recommended to install one by typing: `pip3 install virtualenv`

7. Once installed, set up an environment so that all the libraries you install for this project do not potentially interfere with other code. In the terminal/cmd go to the folder where the project is stored: `cd path/to/directory/command-line-chemkin` and create the environemnt by typing `virtualenv --python=python3.7 .` (Don't forget the end dot!)

8. Finally, in the same directory, activate the environment by typing `source bin/activate`

9. To install all libraries and modules used in the project, type: `pip install -r requirements.txt`

10. You should now be set up to run the code. Choose an text editor of your choice (PyCharm, Atom, Sublime Text...) and open the project. The source directory is src and the project is run from the src/main.py file. Ensure that the text editor is configured to recognise the environment, source directory etc.

11. By typing different options in the main function in main.py, it is now possible to run this code.  

## Functions
### For Generating Input Files From Spreadsheet
Generating chemkin input files from spreadsheets: 
1. Create/load a spreadsheet with all the conditions you want to test. Every row of the file will be an input for a chemkin file. Ensure that the format (usually requires 'number' to be set in excel) matches the format of the chemiin input file. Column headers should correspond to the exact variable name in the chemkin file (try to avoid additional whitespaces after the column name). Name1 and name2 columns should be populated with two names that can later be used to filter and/or identify each file generated. If name1 and name2 are both identical to those in another row, only one version of a file will be generated. For example, I use equivalence ratios and heat ratios as name1 and name2.  

2. Go to chemkin and run your desired model/reactor network once with 'save intermediate file options' activated. In the folder where the files are saved, you should find a chemkin.inp file that is in a similar format to the template files provided in the notes directory. Check that this file contains all the parameters you wish to modify. 

3. In the src/main.py file type:
`random_instance_name = classes.InpGenerator(path/to/excel/file/name_of_spreadsheet.xlsx, path/to/chemkin/input/file/template/templatename.inp)`

4. A folder of input files will be generated in src/chemkin_launch_files/input_files directory and these can be launched with chemkin from the command line.

5. Go the source directory from which you will be running the job (for example through logging into the supercomputer and finding your user directory). Add a folder named solutions to this folder. Go back to the source directory add another folder named input_files. Drop all the recently created input files into the input_files folder. Also add a job_files folder.

6. Return to your source directory and add the following relevant files:
- run_jobs.sh file (copy from the src/chemkin_launch_files directory)
- build_jobs.sh file (copy from the src/chemkin_launch_files directory)
- thermo.dat (from mechanism author - may not be required depending on model)
- transport.dat (from mechanism author)
- mechanism.inp (from mechanism author)
- chemkin-data.dtd (list of chemkin setup settings from previous runs)
- filter.py (postprocesses solution.out files, copy from src/chemkin_launch_files )
- filter.sh (launches filter.py, copy from src/chemkin_launch_files)

7.The job files MUST be modified to contain the correct project names, paths, and to load the correct model. This is the most likely source of error and should be checked carefully. Current .sh files are built as an example of one set of supercomputer settings. 

8.In the source directory, submit the run_jobs.sh file. Once this is complete, submit the filter.sh file. 
 
9.All files will be saved in name1_name2_inputname.out format in the solutions folder. 

### For Plotting Data From Solution.Out Files
The following guide gives a list of commands to type into the src/main.py file. 
1. Add the solutions folder to the src/chemkin_launch_files directory. For multiple runs, feel free to add multiple folders. 

2. To postprocess the solutions files so that they can be plotted:
`solutions1 = graphs.Solution(path/to/solutions/folder)`

3. To create a graph, see below. Note that this can be used to create multiple graphs as long as the names (e.g graph1, graph2..) are different:
`graph1 = graphs.Graph('X Axis Name Here', 'Y Axis Name Here', 'My Title')`

4. To add solution.out data to the graph1 plot, see below. Note that multiple data with legends and colours can be added to the same plot:
`graph1.add_scatter_sol(solutions1, x='name2', y='H2O', colour='steelblue', X_value = 1.4995, best_fit_line= True)`

The full list of options and format is shown here: 
```
def add_scatter_sol(self, solution: Solution, x: str, y: str, name="", legend="", colour='darkgrey',
                    filter_condition=None,
                    filter_value=None, X_value: int = None, number_of_points=1, best_fit_line: bool= False):
    """

    :param solution: name of instance when generating the data from the Solution() class (used for chemkin output folder data)
    :param x: exact name of column for the x data
    :param y: exact name of column for the y data
    :param name: if present, will search and plot data from a specific .out file. Must remove .out file extension - just write the file name
    :param legend: legend label
    :param colour: colour of line and if selected, line of best fit
    :param filter_condition: name of column used as a filter for values
    :param filter_value: the value the filter_column should have for plotting data
    :param X_value: assumes filter condition is X(cm) and filter value is the X_value.
    :param number_of_points: repressents n for plotting every nth point in the data. Use for very large datasets
    :param best_fit_line: if True will add a line of best fit
    :return:
    """
```
5. To add data from a spreadsheet to the graph1 plot (for example experimental data), see below. Note that multiple data with legends and colours can be added to the same plot:
```
graph1.add_scatter_spreadsheet('/file/path/to/spreadsheet/name_of_spreadsheet.xlsx',
                                   x='column_name_of_x_axis_values', y='column_name_of_x_axis_values', colour='red', filter_condition='column_name_to_filter_data',
                                   filter_value=0.3, y_error='column_name_of_error_values', legend='legend_label', best_fit_line= True)
```
The full list of options and format is shown here:
```
def add_scatter_spreadsheet(self, path_to_sheet: str, x: str, y: str, legend="", colour='darkgrey',
                            filter_condition=None,
                            filter_value=None, X_value: int = None, round_filter_to_dp: int = None,
                            y_error: str = None, error_colour='darkgray', best_fit_line: bool = False):
    """
    Based on spreadsheet input (csv or excel), plot scatter plot on a figure belonging to the Graph() instance.
    Can be used to plot multiple datasets on the same graph
    :param path_to_sheet: full path as string including extension .csv or .xls*
    :param x: exact name of column in spreadsheet for the x data
    :param y: exact name of column in spreadsheet for the y data
    :param legend: legend label
    :param colour: of line and if selected, line of best fit
    :param filter_condition: name of spreadsheet column used as a filter for values
    :param filter_value: the value the filter_column should have for plotting data
    :param X_value: assumes filter condition is X(cm) and filter value is the X_value. For specialist spreadsheets only.
    :param round_filter_to_dp: rounds the filter column values to number of decimal places. Use negative values for 0s (nearest 10, 100 etc)
    :param y_error: column name for y error bars - if present will add error bars to plot
    :param error_colour: error bar colour
    :param best_fit_line: if True will add a line of best fit
    :return:
    """
```

6.Show the graphs and save them:
`graph1.show_and_save('path/to/save/folder', 'name_to_save_as')`

7.For graph colour options, use the matplotlib colour names : <https://matplotlib.org/3.1.1/gallery/color/named_colors.html>

### Project Format 
To complete...

### Example src/main.py script
To generate input files from a spreadsheet, which will be saved to src/chemkin_launch_files. This code uses a stagnation flame template from the notes directory but can be replaced with any other chemkin_model.inp input file: 
```
from IO_files_creator import classes, graphs

def main():
    instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
                                      '/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp')
if __name__ == "__main__":
    main()
```
To plot experimental results and (first sort) plot chemkin_solution.out files on the same graph. 

```
from IO_files_creator import classes, graphs
def main():
    my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    graphy = graphs.Graph('X(cm)', 'Speed, U(cm/s)', 'My Title')
    graphy.add_scatter_sol(my_instance, x='name2', y='H2O', colour='steelblue', X_value = 1.4995, best_fit_line= True)
    graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx',
                                   x='mean_eqy', y='X_CO', colour='steelblue', filter_condition='mean_heaty',
                                   filter_value=0.6, y_error='delta_X_CO', legend='0.6', best_fit_line= True)
    graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx',
                                   x='mean_eqy', y='X_CO', colour='red', filter_condition='mean_heaty',
                                   filter_value=0.3, y_error='delta_X_CO', legend='0.3', best_fit_line= True)
    graphy.show_and_save('chemkin_launch_files/graphs', 'test')
if __name__ == "__main__":
    main()
```

### Example Graph: 
![](/Users/marina/Developer/GitHub/chemkin-plot-premix/notes/graphstest.png)



### To Do List [Project in Progress]:
- [x] Generate input file that launches the correct solver with the suitable temperature conditions and allows a custom name for the output file. 
- [x] Generate an csv file that includes all the conditions required for input. 
- [x] Use python to create new input (.inp) files from the BigWorkbook csv file.
- [x] Generate a bash file that launches all files in input folder
- [x] Generate a class for sorting the solution to dataframe
- [x] Generate a class for plotting solution (with optional legend, title, axies titles, conditions used)
- [x] Add capability for plotting experimental results on same graph 
- [ ] Rearrange folders and filepaths for ease of use
- [x] Add website, tutorial and launch documentation 
- [ ] Add job files for pipe and parallel processing
- [ ] Add sensitivity printing options to file 
- [ ] Add interface
- [ ] Test max temp, stag temp, and inlet velocity effect  on output.  

### Contributions
To contribute please raise an issue then open a pull request for review. Specifically, notes folder contributions of chemkin example input files would be very welcome. Please raise any errors as GitHub issues. 
