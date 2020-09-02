from IO_files_creator import input, graphs, auto_graph, extra_funcs

def main():
    h = ['0.1', '0.2', '0.3', '0.4', '0.6']
    colour = ['b', 'r', 'g', 'orange', 'cyan']
    gas = ['CO2', 'CO', 'H2O', 'NO', 'N2O', 'NO2', 'NH3', 'HCN']
    for g in gas:
        graphy = graphs.GraphSetAxis('heat ratio', g + ' concentration, ppm',
                                             g + ' Concentration at 1.2 Equivalence Ratio')
                # create a new graph for every iteration of gas:
        graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/input_files/repeatfinal4.xlsx', 'mean_heaty', y='X_' + g,
                                               colour='b', filter_condition={'mean_eqy': float(1.2)}, best_fit_line=True,
                                               y_error='delta_X_' + g, error_colour='darkgrey',
                                               best_fit_line_filter={'mean_eqy': float(1.2)})
        graphy.show_and_save('chemkin_launch_files/graphs/', f'heat_{g}.png')

if __name__ == "__main__":
    main()
