from IO_files_creator import classes, graphs


def main():
    # instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
    #                                  '/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp')
    # my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    workbook = graphs.Graph('Z', 'CO Concentration', 'My Title')
    workbook.add_scatter('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.csv', x='Z',
                         y='X_CO', filter_condition='mean_heat', filter_value=0.6, round_filter_to_dp= 2)
    workbook.show_and_save('chemkin_launch_files/graphs', 'test')


if __name__ == "__main__":
    main()
