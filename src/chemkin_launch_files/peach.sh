#!/bin/bash
###UGE option###
#$ -S /bin/bash
#$ -P general
#$ -jc dma.A
#$ -pe impi_fillup 16
#$ -l h_vmem=300g
#$ -l h_rt=1:00:00
#$ -N princesspeach
#$ -cwd

# Load modules
. /etc/profile.d/modules.sh
module load ansys/19.0

# ChemkinPro
echo "Setting up the environment"
source chemkinpro_setup.ksh
chem -i ./chem.inp -d ./thermo.dat -o ./chem.out
tran -i ./trans.dat > trans.out

echo "Running analysis"
CKReactorBurnerStabilizedStagnationFlame  < ./input_files/0.65__0.1__stagnation_template.inp > ./solutions/0.65__0.1__stagnation_template.out
echo "Job complete"
