import pandas as pd
import numpy as np
import sys
import os
import glob

files = list(glob.glob(os.path.join('*.csv')))

#input_file = sys.argv[1]
#output_file = sys.argv[2]

for file in files:
    with open(file, 'r') as input:
        f = pd.read_csv(input)
        df = pd.DataFrame(f)
        Size_min = df['Size(bp)'].min()
        Size_max = df['Size(bp)'].max()
        Size_mean = df['Size(bp)'].mean()
        exons_min = df['Number_of_exons'].min()
        exons_max = df['Number_of_exons'].max()
        exons_mean = df['Number_of_exons'].mean() 
        print('filename:',file,'Size-min:',Size_min,'Size-max:',Size_max,'Size-mean:',Size_mean,'Number_of_exons-min:',exons_min,'Number_of_exons-max:',exons_max,'Number_of_exons-mean:',exons_mean)
        val ='filename:',file,'Size-min:',Size_min,'Size-max:',Size_max,'Size-mean:',Size_mean,'Number_of_exons-min:',exons_min,'Number_of_exons-max:',exons_max,'Number_of_exons-mean:',exons_mean
        with open("outfile.txt", "a") as fh_out:
            fh_out.write(str(val))
            fh_out.write("\n")

