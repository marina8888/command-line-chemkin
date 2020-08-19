from IO_files_creator import input, graphs


def main():
    # inp = input.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/wall_temp.xlsx', '/Users/marina/Developer/GitHub/chemkin-plot-premix/notes/stagnation_all_mech.inp')
    sol1 = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/input_files/H2O')
    print(sol1)

    # heatr = ['0.1', '0.2', '0.3', '0.4', '0.6']
    colour = ['b', 'r', 'g', 'orange', 'cyan']
    # graphy = graphs.Graph('equivalence ratio', 'temperature, K', 'Actual Wall Temperature vs Equivalence Ratio')
    # for h,c in zip(heatr, colour):
    #     # graphy.add_scatter_spreadsheet('chemkin_launch_files/input_files/hcn_super_filtered.xlsx','mean_eqy', 'Tw[K]', legend=h +' heat ratio', colour=c,
    #     #     filter_condition={'mean_heaty': float(h)}, best_fit_line=True, best_fit_line_filter={'mean_heaty': float(h)})
    #     graphy.add_scatter_spreadsheet('chemkin_launch_files/input_files/hcn_super_filtered.xlsx','mean_eqy', 'Actual Plate temp', legend=h + ' heat ratio', colour=c,
    #                                    filter_condition={'mean_heaty': float(h)}, best_fit_line=True,
    #                                    best_fit_line_filter={'mean_heaty': float(h)})
    # graphy.show_and_save('chemkin_launch_files/graphs/', 'temptest.png')

    okafor = graphs.Solution('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/okafor-solution')
    gri =  graphs.Solution('/Users/marina/Documents/Work/Tohoku Uni/strain stabiolised product gas/chemkin_plots/gri')
    heatr = ['0.1']
    gasl = ['CO2']
    for g in gasl:
        graphy = graphs.Graph('equivalence ratio', g + ' concentration, ppmv',
                              g + ' Concentration for all Heat Ratios')
        for h,c in zip(heatr, colour):
            # graphy.add_scatter_spreadsheet('chemkin_launch_files/input_files/hcn_super_filtered.xlsx', 'mean_eqy', y='X_' + g, legend=f'experiment, {h} heat ratio', colour='r', filter_condition={'mean_heaty': float(h)}, best_fit_line=True, y_error='delta_X_' + g, error_colour='darkgrey', best_fit_line_filter={'mean_heaty': float(h)})

            graphy.add_scatter_sol(okafor,'name1', g, legend=f"Okafor et al., {h} heat ratio", filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
            scatter=True, best_fit_line=True, colour=c)
            # graphy.add_scatter_sol(gri, 'name1', g, legend=f"GRI-Mech3.0, {h} heat ratio", filter_condition={'name2': h}, X_value='2.0000', number_of_points=1, multip=1000000,
            # scatter=True, best_fit_line=True, colour = 'g')
        graphy.show_and_save('chemkin_launch_files/graphs/', 'blah.png')
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


if __name__ == "__main__":
    main()
