from IO_files_creator import input, auto_graph


def main():
    # define heat ratio, gas and colours:
    h = ['0.1', '0.2', '0.3', '0.4', '0.6']
    colour = ['b', 'r', 'g', 'orange', 'cyan']
    gas = ['CO2', 'CO', 'H2O', 'NO', 'N2O', 'NO2', 'NH3', 'HCN']

    # create graphs ppmv:
    auto_graph.plot_exp_num_ppm_by_gas('/Users/marina/Developer/GitHub/chemkin-plot-premix/src/chemkin_launch_files/input_files/augall.xlsx', h, colour, gas)

    # create graphs %:

if __name__ == "__main__":
    main()
