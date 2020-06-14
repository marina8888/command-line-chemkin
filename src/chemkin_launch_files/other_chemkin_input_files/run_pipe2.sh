
#!/bin/bash
#$ -S /bin/bash
#$ -P general
#$ -jc dma.A
#$ -pe impi_fillup 16
#$ -l h_vmem=300g
#$ -l h_rt=2:00:00
#$ -N chemkinpro190
#$ -cwd

. /etc/profile.d/modules.sh
module load ansys/19.0
source chemkinpro_setup.ksh

chem -i ./chem.inp -d ./thermo.dat -o ./chem.out
tran -i ./trans.dat > trans.out

for filename in ./input_files/*.inp; do
    y=${filename%%.*}
    CKReactorBurnerStabilizedStagnationFlame < "$filename" >"${filename%.*}.out"
    echo "${filename##*/}"
done

