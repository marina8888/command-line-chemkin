from IO_files_creator import input, graphs


def main():
    # inp = input.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx', '/Users/marina/Developer/GitHub/chemkin-plot-premix/notes/stagnation_template.inp')
    sol1 = graphs.Solution('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/okafor-solution')
    heat_ratio = ['0.1', '0.2', '0.3', '0.4', '0.6', '1.0']
    colour_list = ['red', 'red', 'red', 'red', 'red', 'red']
    colour_list2 = ['b', 'b', 'b', 'b', 'b', 'b']
    full_gas_list = ['CO2', 'CO', 'H2O', 'NO', 'NO2', 'N2O', 'NH3', 'H2', 'O2']
    for gas in full_gas_list:
        for h, c, c2 in zip(heat_ratio, colour_list, colour_list2):
            graphy = graphs.Graph('equivalence ratio', gas + ' Concentration, ppmv',
                                  gas + ' Concentration for ' + h + ' Heat Ratio')
            graphy.add_scatter_sol(sol1, 'name1', gas, legend="Okafor stagnation model", colour='darkgreen',
                                   filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, best_fit_line=True)
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/main.xlsx',
                x='mean_eqy', y='X_' + gas, colour=c, y_error='delta_X_' + gas,
                filter_condition={'mean_heaty': h, 'Tracer gas type': 0},
                legend='without dilution', best_fit_line=True, best_fit_line_filter={'mean_heaty': h})
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/main.xlsx',
                x='mean_eqy', y='X_' + gas, colour=c2, y_error='delta_X_' + gas,
                filter_condition={'mean_heaty': h, 'Tracer gas type': 1, 'Tracer gas type': 2},
                legend='with dilution', best_fit_line=True, best_fit_line_filter={'mean_heaty': h})

            string = gas + 'new_' + h + '.png'
            graphy.show_and_save('chemkin_launch_files/graphs/', string)

if __name__ == "__main__":
    main()
