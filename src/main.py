from IO_files_creator import input, auto_graph

def main():
    # define heat ratio, gas and colours:
    h = ['0.1', '0.2', '0.3', '0.4', '0.6']
    colour = ['b','r', 'g', 'orange', 'cyan']
    gas = ['CO2', 'CO', 'H2O', 'NO', 'N2O', 'NO2', 'NH3', 'HCN']

    # create graphs ppmv:
    auto_graph.plot_exp_by_gas('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/repeatfinal4.xlsx', h, colour, gas, 'ppm')

    # create graphs %:
    gas = ['O2', 'H2']
    auto_graph.plot_exp_by_gas('/Users/marina/Developer/GitHub/chemkin-plot-premix/import_files/repeatfinal4.xlsx', h, colour, gas, 'percent')

if __name__ == "__main__":
    main()
