from IO_files_creator import input_conditions
def main():
    df=input_conditions.csv_to_df('import_files/my_workbook.csv')
    input_conditions.generate_new_inp(df, 'chemkin_launch_files/stagnation_template.inp')
if __name__ == "__main__":
    main()