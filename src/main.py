from IO_files_creator import input, graphs

def main():
    # instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
    #                                 '/Users/marina/Developer/GitHub/chemkin-plot-premix/notes/stagnation_template.inp')
    my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    graphy = graphs.Graph('X(cm)', 'CO Concentration', 'CO Concentration By Heat Percentage')
    # graphy.add_scatter_sol(my_instance, x='name2', y='H2O', colour='steelblue', X_value = 1.4995, best_fit_line= True)
    graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx',
                                   x='mean_eqy', y='X_CO', colour='steelblue', filter_condition={'mean_heaty':0.6, 'Tracer gas type': 0}, y_error='delta_X_CO', legend='0.6', best_fit_line= True)
    graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx',
                                   x='mean_eqy', y='X_CO', colour='red', filter_condition={'mean_heaty':0.3, 'Tracer gas type': 0}, y_error='delta_X_CO', legend='0.3', best_fit_line= True)
    graphy.show_and_save('chemkin_launch_files/graphs/', 'test')


if __name__ == "__main__":
    main()
