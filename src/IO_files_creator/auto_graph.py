from IO_files_creator import graphs


def plot_exp_by_gas(path_to_exp_sheet: str, heatr_list: [], colour_list: [], gas_list: [], unit: str):

    for g in gas_list:
        if unit == 'ppm':
            graphy = graphs.Graph('equivalence ratio', g + ' concentration, ppmv',
                                  g + ' Concentration for all Heat Ratios')
        else:
            graphy = graphs.Graph('equivalence ratio', g + ' concentration, %',
                                      g + ' Concentration for all Heat Ratios')

        for h, c in zip(heatr_list, colour_list):
        # create a new graph for every iteration of gas:
            graphy.add_scatter_spreadsheet(path_to_exp_sheet, 'mean_eqy', y='X_' + g,
                                               legend=f'experiment, {h} heat ratio',
                                               colour=c, filter_condition={'mean_heaty': float(h)}, best_fit_line=True,
                                               y_error='delta_X_' + g, error_colour='darkgrey',
                                               best_fit_line_filter={'mean_heaty': float(h)})
        graphy.show_and_save('chemkin_launch_files/graphs/', f'exp_{g}.png')


def plot_all_by_gas_by_heat(path_to_exp_sheet: str, heatr_list: [], colour_list: [], gas_list: [], unit: str):
    # create mechanisms from input folders:
    okafor = graphs.Solution(
        '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/okafor-solution')
    gri = graphs.Solution('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/gri')

    for g in gas_list:

        for h, c in zip(heatr_list, colour_list):
            # initialise a multiplier to convert results to ppm:

            if unit == 'ppm':
                m = 1000000
                graphy = graphs.GraphSetAxis('equivalence ratio', f'{g} concentration, ppmv',
                                      f'{g} Concentration for {h} Heat Ratio', ylim_min= 0)
            else:
                m = 100
                graphy = graphs.GraphSetAxis('equivalence ratio', f'{g} concentration, %',
                                      f'{g} Concentration for {h} Heat Ratio')

            # create a new graph for every iteration of gas and heat ratio:
            graphy.add_scatter_spreadsheet(path_to_exp_sheet, 'mean_eqy', y='X_' + g,
                                           legend=f'experiment, {h} heat ratio',
                                           colour='b', filter_condition={'mean_heaty': float(h)}, best_fit_line=False,
                                           y_error='delta_X_' + g, error_colour='darkgrey',
                                           best_fit_line_filter={'mean_heaty': float(h)})

            graphy.add_scatter_sol(okafor, 'name1', g, legend=f"Okafor et al., {h} heat ratio",
                                   filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=m,
                                   scatter=True, best_fit_line=True, colour= 'r')
            graphy.add_scatter_sol(gri, 'name1', g, legend=f"GRI-Mech3.0, {h} heat ratio", filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=m,
            scatter=True, best_fit_line=True, colour = 'g')
            graphy.show_and_save('chemkin_launch_files/graphs/', f'test_{g}_{h}.png')
