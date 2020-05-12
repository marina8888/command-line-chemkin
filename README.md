# Chemkin Plot Premix

### Overview
In ANSYS CHEMKIN modelling, often a range of input conditions need to be tested for an overall impression of flame bahaviour. The process can be accelerated through generating a spreadsheet with all required conditions and launching them to command line. Furthermore, post-processing CHEMKIN files to extract the critical information can be time consuming. 

When complete, this script should allow for excel spreadsheet input of conditions to generate chemkin command line input files for the premixed stagnation flame model. Once the results have been generated, they can be post-processed to calculate the flame product gases at each condition. Plotting options allow for the selection of a legend, colour settings and for the results to be plotted against experimental results. 

Note only the generation of the input.inp file is considered in the script and the mechanism, thermal and transport data for the considered flame should be aquired from the author of the mechanism or a reputable database (e.g GRI-Mech 3.0). 

### To Do:
- [x] Generate input file that launches the correct solver with the suitable temperature conditions and allows a custom name for the output file. 
- [ ] Generate an excel spreadsheet that includes all the conditions required for input. Use the BigWorkbook class excel format from the marina888/dilution-gas repo. 
- [ ] Generate this same input file from python file parsing an excel spreadsheet with these conditions. 
- [ ] Add a final job file to project that produces an output file named and containing the details of the conditions used. It should include - eq, heat ratio and mechanism used. 
- [ ] Generate a python file that takes an input of chemkin (output) results files and sorts them for plotting 
- [ ] Add input for experimental results on the same graph 
- [ ] Add suitable plotting functions with parameters for legend, title, axies titles, conditions used. 

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
