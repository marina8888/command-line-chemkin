# Command Line CHEMKIN

### Overview
When conducting combustion analysis with CHEMKIN software, often a range of input conditions need to be tested. 

This code accelerates this process. The user a inputs a spreadsheet with all required conditions (or values aquired from an experiment). These values can be used to automatically generate input files and launch all the files to chemkin through the command line. Furthermore, post-processing CHEMKIN files to extract the critical information can be time consuming. 

This code also includes capability for post-processing and plotting the data. Filtering data for a certain X value (reaction chamber depth) or by other parameters (including custom added parameters) is possible. Plotting options allow for the selection of a legend, colour settings and for the numerical results to be plotted against experimental results. 

Note only the generation of the input.inp file is considered in the script. The mechanism, thermal, transport and .dtd files for the considered flame should be acquired from the author of the mechanism or a reputable database (e.g GRI-Mech 3.0). 

Please note that this code is a personal open-source project and is intended to act as a helper tool for users that already have licenses and an installation of CHEMKIN software. This project is not created by ANSYS and is no way affiliated with this company. It is a personal project and not intended to perform to commerical standards. 

### To Do List:
- [x] Generate input file that launches the correct solver with the suitable temperature conditions and allows a custom name for the output file. 
- [x] Generate an csv file that includes all the conditions required for input. 
- [x] Use python to create new input (.inp) files from the BigWorkbook csv file.
- [x] Generate a bash file that launches all files in input folder
- [x] Generate a class for sorting the solution to dataframe
- [x] Generate a class for plotting solution (with optional legend, title, axies titles, conditions used)
- [x] Add capability for plotting experimental results on same graph 
- [ ] Rearrange folders and filepaths for ease of use
- [ ] Add website, tutorial and launch documentation 
- [ ] Add sensitivity printing options to file 
- [ ] Add interface
- [ ] Test max temp, stag temp, and inlet velocity effect  on output.  
### Functions
To complete

### Standard Format 
To complete

### To Run
To complete

3. Install/update python to python3: https://packaging.python.org/tutorials/installing-packages/
4. Install 'Requirements Files' to use the correct libraries https://pip.pypa.io/en/stable/user_guide/

### Contributions
To contribute please raise an issue then open a pull request for review.
