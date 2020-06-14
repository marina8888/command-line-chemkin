#!/bin/bash
#$ -S /bin/bash
#$ -P GR04APR19
#$ -jc dma.A
#$ -pe impi_fillup 16
#$ -l h_vmem=300G
#$ -l h_rt=24:00:00
#$ -N cleanup
#$ -cwd

python ./filter.py
