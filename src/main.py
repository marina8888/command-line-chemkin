from IO_files_creator import classes


def main():
    instance = classes.BurnerStabilizedStagnationFlame('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.csv',
                                                           'chemkin_launch_files/stagnation_template.inp')


if __name__ == "__main__":
    main()
