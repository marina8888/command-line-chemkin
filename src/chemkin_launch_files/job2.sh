#!/bin/bash
#$ -S /bin/bash
#$ -P general
#$ -jc dma.A
#$ -pe impi_fillup 16
#$ -l h_vmem=300g
#$ -l h_rt=0:10:00
#$ -N chemkinpro190
#$ -cwd

. /etc/profile.d/modules.sh
module load ansys/19.0
source chemkinpro_setup.ksh
module load python3/3.7.3

chem -i ./chem.inp -d ./thermo.dat -o ./chem.out
tran -i ./trans.dat > trans.out

CKReactorBurnerStabilizedStagnationFlame < ./input_files/1.4__0.4__stagnation_template.inp > ./solutions/solution2.out
python3.7 ./filter.py
