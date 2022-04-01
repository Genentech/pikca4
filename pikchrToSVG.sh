#!/bin/bash
helpFunction()
{
   echo ""
   echo "Usage: $0 -i [in folder] -o [out folder]"
   echo -e "\t-i folder of input pikchr file"
   echo -e "\t-o folder of output SVG file"
   exit 1 # Exit script after printing help
}
while getopts "i:o:" opt
do
   case "$opt" in
      i ) ifolder="$OPTARG" ;;
      o ) ofolder="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done
echo "${ifolder}/*.pikchr"
for f in "${ifolder}/*.pikchr"
do 
    for file in $f
        do 
            cand=${file//$ifolder/''}
            outfile="${ofolder}${cand%.*}.svg" 
            touch outfile
            echo $file
            echo $outfile
            ./pikchr/pikchr --svg-only $file > $outfile
        done
done