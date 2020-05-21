from IO_files_creator import classes, graphs


def main():
    # instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
    #                                  '/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp')
    my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    graphy = graphs.Graph('X(cm)', 'Speed, U(cm/s)', 'My Title')
    graphy.add_scatter_sol(my_instance, x='X(cm)', y='H2O', name='0.8__0.4__stagnation_template', colour='steelblue')
    graphy.show_and_save('chemkin_launch_files/graphs', 'test')


if __name__ == "__main__":
    main()
