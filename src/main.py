from IO_files_creator import input, graphs


def main():

    full_gas_list = ['CO2', 'CO', 'H2O', 'NO', 'NO2', 'N2O', 'NH3', 'H2', 'O2']
    gas_list = ['CO2', 'CO', 'H2O', 'NO', 'NO2', 'N2O', 'NH3']
    for gas in gas_list:
        graphy = graphs.Graph('CO2 Flowrate, SLM', gas + ' Concentration, ppmv',
                              gas + ' Concentration vs. Dilution Gas Flowrate')

        graphy.add_scatter_spreadsheet(
            '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/CO2_workbook.xlsx',
            x='CO2/Air upper actual ', y='X_' + gas, colour='b', y_error='delta_X_' + gas,
            legend=gas + ", first experiment", best_fit_line=True)
        graphy.add_scatter_spreadsheet(
            '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/CO2_workbook2.xlsx',
            x='CO2/Air upper actual ', y='X_' + gas, colour='r', y_error='delta_X_' + gas,
            legend=gas + ", repeat experiment", best_fit_line=True)

        graphy.show_and_save('chemkin_launch_files/graphs/', 'dilution_flow_' + gas)
if __name__ == "__main__":
    main()
