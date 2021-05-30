# Fast-HBR
Fast-HBR is duplicate reads removing tool from fastq and fasta files.
Fast-HBR is fast and memory-efficient because it does not need to store reads in string form on the memory. Instead of that, it will store their hash value as integer. Moreover, it will write directly to the output file and remove duplicate reads on-the-fly.

# Usage 

to remove duplicate reads from single end files without reverce complement option

python Fast-HBR.py -s <File name> 
  
  
 to remove duplicate reads from single end files with reverce complement option

python Fast-HBR.py -s <File name> -r
  
  
to remove duplicate reads from paierd end files without reverce complement option

python Fast-HBR.py -p1 <First File name> -p2 <Second File name>
  
  
 to remove duplicate reads from paierd end files with reverce complement option

python Fast-HBR.py -p1 <First File name> -p2 <Second File name> -r
