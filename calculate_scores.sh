#! /bin/bash
# declare -a data_types=('seurat' 'row')
declare -a data_types=('seurat')
inpath="data\PBMC"
outpath="results\PBMC"
# Iterate the string array using for loop
for data_type in ${data_types[@]}; do
     python calculate_scores.py $inpath $outpath $data_type
done
