import sys
import argparse
from tqdm import tqdm
from time import sleep

def main(): 
    '''
    Everything in this section will be run when you run the script
    '''
    trim(fastq_input = args.fastq_file,
         left_trim = args.left,
         right_trim = args.right)

def read_options():
    '''
    This is where you specify options for your script, here we have three arguments:
    fastq_file, left, and right
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--fastq_file", default = "missing", type = str)
    parser.add_argument("--left", default = 0, type = int)
    parser.add_argument("--right", default = 0, type = int)

    args = parser.parse_args()
    if args.fastq_file == "missing":
        raise ValueError("missing input, fastq_file")

    return args


def trim(fastq_input, left_trim, right_trim):
    '''
    trim takes a fastq_input and outputs a hardcoded trim value for the left and right sides.
    trim will return the DNA seq between left and right trim.
    '''

    file = open(fastq_input,'r')
    new_ls = []
    
    print('trimming the fastq file...')
    for index, line in enumerate(tqdm(file.readlines())):
        if index%4 ==1 or index%4==3:  #gets the DNA sequences string in repeating format
            v = line.strip('\n')       #removes newline escape
            new_ls.append(v[left_trim:right_trim]+'\n')
        else:
            new_ls.append(line)
    
    
    new_file = fastq_input.replace('.fastq','')
    new_file = new_file + '_locus_out.fastq'
    
    f = open(new_file,'w')
    
    print('writing file...')
    for i in tqdm(new_ls):
        f.write(i)

        
if __name__ == '__main__': ## if function is called in bash, run main.
    args = read_options()
    main()
