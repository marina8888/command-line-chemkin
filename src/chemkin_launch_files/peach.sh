#!/bin/bash
#$ -S /bin/bash
#$ -P GR04APR19
#$ -jc dma.A
#$ -pe impi_fillup 16
#$ -l h_vmem=300G
#$ -l h_rt=24:00:00
#$ -N princess
#$ -cwd

. /etc/profile.d/modules.sh
module load ansys/19.0
source chemkinpro_setup.ksh

chem -i ./chem.inp -d ./thermo.dat -o ./chem.out
tran -i ./trans.dat > trans.out

