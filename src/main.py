from IO_files_creator import input, graphs


def main():
    # inp = input.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx', '/Users/marina/Developer/GitHub/chemkin-plot-premix/notes/stagnation_template.inp')
    sol1 = graphs.Solution(
        '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/okafor-solution')
    heat_ratio = ['0.1', '0.2', '0.3', '0.4', '0.6', '1.0']
    full_gas_list = ['CO2', 'CO', 'H2O', 'NO', 'NO2', 'N2O', 'NH3', 'HCN']
    c_list = ['gold', 'cyan', 'lime', 'magenta', 'slategrey', 'red']
    c2_list = ['peru', 'steelblue', 'darkgreen','darkviolet', 'black','maroon']
    c3_list = ['darkgoldenrod', 'dodgerblue', 'mediumaquamarine','violet','lightgrey','salmon']
    for gas in full_gas_list:
        graphy = graphs.Graph('equivalence ratio', gas + ' Concentration, ppmv',
                              gas + ' Concentration')
        for h, c, c2, c3 in zip(heat_ratio, c_list, c2_list, c3_list):
            # graphy.add_scatter_sol(sol1, 'name1', gas, legend="Okafor et al, "+ h + " heat ratio", colour=c2,
            #                        filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
            #                        scatter=True, best_fit_line=True)
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/hcn_filtered.xlsx',
                x='mean_eqy', y='X_' + gas, colour=c, filter_condition={'mean_heaty': float(h)},
                y_error='delta_X_' + gas,
                legend='Experiment,' + h + " heat ratio", best_fit_line=True,
                best_fit_line_filter={'mean_heaty': float(h)})
        string = gas + 'all.png'
        graphy.show_and_save('chemkin_launch_files/graphs/', string)

    second_list = ['H2', 'O2']
    for gas in second_list:
        graphy = graphs.Graph('equivalence ratio', gas + ' Concentration, %',
                              gas + ' Concentration')
        for h, c, c2, c3 in zip(heat_ratio, c_list, c2_list, c3_list):
            # graphy.add_scatter_sol(sol1, 'name1', gas, legend="Okafor et al, "+ h +" heat ratio", colour=c2,
            #                        filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=100,
            #                        scatter = True, best_fit_line=True)
            graphy.add_scatter_spreadsheet(
                '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/hcn_filtered.xlsx',
                x='mean_eqy', y='X_' + gas, colour=c, filter_condition={'mean_heaty': float(h)},
                y_error='delta_X_' + gas,
                legend='Experiment,' + h + " heat ratio", best_fit_line=True,
                best_fit_line_filter={'mean_heaty': float(h)})
        string = gas + 'all.png'
        graphy.show_and_save('chemkin_launch_files/graphs/', string)



if __name__ == "__main__":
    main()
