from IO_files_creator import classes, graphs

def main():
    # instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
    #                                  '/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp')
    my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    graphy = graphs.Graph('X(cm)', 'Speed, U(cm/s)', 'My Title')
    graphy.add_scatter_sol(my_instance, x='name2', y='H2O', colour='steelblue', X_value = 1.4995)
    graphy.show_and_save('chemkin_launch_files/graphs', 'test')


if __name__ == "__main__":
    main()
