from IO_files_creator import input, graphs, auto_graph, extra_funcs

def main():
    extra_funcs.filter_sol_folder('/Users/marina/Documents/Work/Tohoku-Uni/H2-NH3/han_lam_out_files')
    han = graphs.PremixSolution('/Users/marina/Documents/Work/Tohoku-Uni/H2-NH3/han_lam_out_files/solutions')
    # for item, value in han.df_dict.items():
    #     print(item)
    #     print(value)
    han.merge_by_row(1)

if __name__ == "__main__":
    main()
