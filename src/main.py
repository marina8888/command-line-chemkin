from IO_files_creator import classes, graphs


def main():
    # instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
    #                                  '/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp')
    # my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    workbook = graphs.Graph('blah', 'blah', 'foo')
    workbook.show_and_save('chemkin_launch_files/graphs', 'test')

if __name__ == "__main__":
    main()

