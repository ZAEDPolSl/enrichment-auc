#! /bin/bash
declare -a data_types=('raw_counts' 'log2')
inpath="data\Pancreas"
outpath="results\Pancreas"
# liver gsva
# Iterate the string array using for loop
for data_type in ${data_types[@]}; do
     python calculate_scores.py $inpath $outpath $data_type
done