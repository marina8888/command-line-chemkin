from IO_files_creator import input, graphs


def main():
    # inp = input.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx', '/Users/marina/Developer/GitHub/chemkin-plot-premix/notes/stagnation_template.inp')
    sol1 = graphs.Solution(
        '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/okafor-solution')
    heat_ratio = ['0.1', '0.2', '0.3', '0.4', '0.6', '1.0']
    colour_list = ['red', 'red', 'red', 'red', 'red', 'red']
    colour_list2 = ['b', 'b', 'b', 'b', 'b', 'b']
    full_gas_list = ['CO2', 'CO', 'H2O', 'NO', 'NO2', 'N2O', 'NH3']
    for gas in full_gas_list:
        for h in heat_ratio:
            graphy = graphs.Graph('equivalence ratio', gas + ' Concentration, ppmv',
                                  gas + ' Concentration for ' + h + ' Heat Ratio')
            graphy.add_scatter_sol(sol1, 'name1', gas, legend="Okafor stagnation model", colour='red',
                                   filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
                                   scatter=False, best_fit_line=True)
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/all_results_ever.xlsx',
                x='mean_eqy', y='X_' + gas, colour='blue', filter_condition={'mean_heaty': float(h), 'Datey': 1},
                y_error='delta_X_' + gas,
                legend='first experiment', best_fit_line=True,
                best_fit_line_filter={'mean_heaty': float(h), 'Datey': 1})
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/all_results_ever.xlsx',
                x='mean_eqy', y='X_' + gas, colour='orange', y_error='delta_X_' + gas,
                filter_condition={'mean_heaty': float(h), 'Datey': 2},
                legend='second experiment', best_fit_line=True,
                best_fit_line_filter={'mean_heaty': float(h), 'Datey': 2})
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/all_results_ever.xlsx',
                x='mean_eqy', y='X_' + gas, colour='green', y_error='delta_X_' + gas,
                filter_condition={'mean_heaty': float(h), 'Datey': 3}, best_fit_line=True, legend='third experiment',
                best_fit_line_filter={'mean_heaty': float(h), 'Datey': 3})

            string = gas + 'date_' + h + '.png'
            graphy.show_and_save('chemkin_launch_files/graphs/', string)

    second_list = ['H2', 'O2']
    for gas in second_list:
        for h in heat_ratio:
            graphy = graphs.Graph('equivalence ratio', gas + ' Concentration, %',
                                  gas + ' Concentration for ' + h + ' Heat Ratio')
            graphy.add_scatter_sol(sol1, 'name1', gas, legend="Okafor stagnation model", colour='red',
                                   filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=100,
                                   scatter = False, best_fit_line=True)
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/all_results_ever.xlsx',
                x='mean_eqy', y='X_' + gas, colour='blue', filter_condition={'mean_heaty': float(h), 'Datey': 1},
                y_error='delta_X_' + gas,
                legend='first experiment', best_fit_line=True,
                best_fit_line_filter={'mean_heaty': float(h), 'Datey': 1})
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/all_results_ever.xlsx',
                x='mean_eqy', y='X_' + gas, colour='orange', y_error='delta_X_' + gas,
                filter_condition={'mean_heaty': float(h), 'Datey': 2},
                legend='second experiment', best_fit_line=True,
                best_fit_line_filter={'mean_heaty': float(h), 'Datey': 2})
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/all_results_ever.xlsx',
                x='mean_eqy', y='X_' + gas, colour='green', y_error='delta_X_' + gas,
                filter_condition={'mean_heaty': float(h), 'Datey': 3}, best_fit_line=True, legend='third experiment',
                best_fit_line_filter={'mean_heaty': float(h), 'Datey': 3})
            string = gas + 'date_' + h + '.png'
            graphy.show_and_save('chemkin_launch_files/graphs/', string)

if __name__ == "__main__":
    main()
