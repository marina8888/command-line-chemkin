from IO_files_creator import input, graphs

def main():
    graphy = graphs.Graph('CO2 Flowrate, SLM', 'Gas Concentration, %', 'Gas Concentration vs. Dilution Gas Flowrate')
    full_gas_list = ['CO2','CO', 'H2O', 'NO', 'NO2', 'N2O', 'NH3','H2', 'O2']
    gas_list = ['H2', 'O2']
    # for gas in gas_list:
    graphy.add_scatter_spreadsheet('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/CO2_workbook.xlsx',
                                       x='CO2/Air upper actual ', y='X_H2', colour='lawngreen', y_error='delta_X_H2', legend="H2, first experiment", best_fit_line=True)
    graphy.add_scatter_spreadsheet('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/CO2_workbook2.xlsx',
                                       x='CO2/Air upper actual ', y='X_H2', colour='darkseagreen', y_error='delta_X_H2', legend='H2, repeat experiment', best_fit_line=True)
    graphy.add_scatter_spreadsheet('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/CO2_workbook.xlsx',
                                       x='CO2/Air upper actual ', y='X_O2', colour='firebrick', y_error='delta_X_O2', legend="O2, first experiment", best_fit_line=True)
    graphy.add_scatter_spreadsheet('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/CO2_workbook2.xlsx',
                                       x='CO2/Air upper actual ', y='X_O2', colour='red', y_error='delta_X_O2', legend='O2, repeat experiment',best_fit_line=True)
    graphy.show_and_save('chemkin_launch_files/graphs/', 'test')


if __name__ == "__main__":
    main()
