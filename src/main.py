from IO_files_creator import classes, graphs
import pandas

def main():
    # instance = classes.InpGenerator('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/stagnation_file.xlsx',
    #                                   '/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/stagnation_template.inp')
    # my_instance = graphs.Solution('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/solutions')
    # graphy = graphs.Graph('X(cm)', 'Speed, U(cm/s)', 'My Title')
    # graphy.add_scatter_sol(my_instance, x='name2', y='H2O', colour='steelblue', X_value = 1.4995, best_fit_line= True)
    # # graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx',
    # #                                x='mean_eqy', y='X_CO', colour='steelblue', filter_condition='mean_heaty',
    # #                                filter_value=0.6, y_error='delta_X_CO', legend='0.6', best_fit_line= True)
    # # graphy.add_scatter_spreadsheet('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/my_workbook.xlsx',
    # #                                x='mean_eqy', y='X_CO', colour='red', filter_condition='mean_heaty',
    # #                                filter_value=0.3, y_error='delta_X_CO', legend='0.3', best_fit_line= True)
    # graphy.show_and_save('chemkin_launch_files/graphs', 'test')

    df1 = pandas.DataFrame(data={'x': [1, 2, 3, 4, 5], 'y': [10, 11, 12, 13, 14]})
    df2 = pandas.DataFrame(data={'x': [4, 5, 6], 'z': [10, 13, 14]})
    #create blank dataframe to store values that are present in both:
    df3 = pandas.DataFrame()
    #check 'x' column of each row of each dataframe to find matches:
    for i in range (len(df1)):
        for ii in range(len(df2)):
            if df1.iloc[i]['x'] == df2.iloc[ii]['x']:
                #if there's a match, append it to df3:
                df3 = df3.append(df1.iloc[i])
    #delete df3 from df1 and rename it as df1:
    df1 = pandas.concat([df1,df3]).drop_duplicates(keep=False)
    print(df1)

    # for i in range(0,len(df2)):
    #     for
    #     print(df2.iloc[i])
    # print (df2)

if __name__ == "__main__":
    main()
