from IO_files_creator import graphs

def plot_exp_num_ppm_by_gas(path_to_exp_sheet:str, heatr_list: [], colour_list:[], gas_list: []):

    # create mechanisms from input folders:
    okafor = graphs.Solution(
        '/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/okafor-solution')
    gri = graphs.Solution('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/gri')

    for g in gas_list:
        # create a new graph for every iteration of gas:
        graphy = graphs.Graph('equivalence ratio', g + ' concentration, ppmv',
                              g + ' Concentration for all Heat Ratios')

        for h, c in zip(heatr_list, colour_list):
            graphy.add_scatter_spreadsheet(path_to_exp_sheet, 'mean_eqy', y='X_' + g, legend=f'experiment, {h} heat ratio', colour=c, filter_condition={'mean_heaty': float(h)}, best_fit_line=True, y_error='delta_X_' + g, error_colour='darkgrey', best_fit_line_filter={'mean_heaty': float(h)})

            # graphy.add_scatter_sol(okafor, 'name1', g, legend=f"Okafor et al., {h} heat ratio",
            #                        filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
            #                        scatter=True, best_fit_line=True, colour= 'b')
            # graphy.add_scatter_sol(gri, 'name1', g, legend=f"GRI-Mech3.0, {h} heat ratio", filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
            # scatter=True, best_fit_line=True, colour = 'g')
        graphy.show_and_save('chemkin_launch_files/graphs/', f'test_{g}.png')

    def plot_exp_num_ppm(path_inp_folder: str, heatr_list: [], colour_list: [], gas_list: [], okafor, gri):
        pass
# gasl = ['H2', 'O2']
# for g in gasl:
#     graphy = graphs.Graph('equivalence ratio', g + ' concentration, %',
#                           g + ' Concentration for all Heat Ratios')
#     for h in heatr:
#         graphy.add_scatter_spreadsheet('chemkin_launch_files/input_files/hcn_super_filtered.xlsx', 'mean_eqy',
#                                        y='X_' + g, legend=f'experiment, {h} heat ratio', colour='r', error_colour='darkgrey', y_error='delta_X_' + g,
#         filter_condition={'mean_heaty': float(h)}, best_fit_line=True,
#         best_fit_line_filter={'mean_heaty': float(h)})
#
#         graphy.add_scatter_sol(okafor,'name1', g, legend=f'experiment, {h} heat ratio', filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
#         scatter=True, best_fit_line=True, colour='b')
#         graphy.add_scatter_sol(gri, 'name1', g, legend=f"GRI-Mech3.0, {h} heat ratio", filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
#         scatter=True, best_fit_line=True, colour = 'g')
#     graphy.show_and_save('chemkin_launch_files/graphs/', f'{g}all.png')



# graphy = graphs.Graph('equivalence ratio', 'temperature, K', 'Actual Wall Temperature vs Equivalence Ratio')
# for h,c in zip(heatr, colour):
#     # graphy.add_scatter_spreadsheet('chemkin_launch_files/input_files/hcn_super_filtered.xlsx','mean_eqy', 'Tw[K]', legend=h +' heat ratio', colour=c,
#     #     filter_condition={'mean_heaty': float(h)}, best_fit_line=True, best_fit_line_filter={'mean_heaty': float(h)})
#     graphy.add_scatter_spreadsheet('chemkin_launch_files/input_files/hcn_super_filtered.xlsx','mean_eqy', 'Actual Plate temp', legend=h + ' heat ratio', colour=c,
#                                    filter_condition={'mean_heaty': float(h)}, best_fit_line=True,
#                                    best_fit_line_filter={'mean_heaty': float(h)})
# graphy.show_and_save('chemkin_launch_files/graphs/', 'temptest.png')
