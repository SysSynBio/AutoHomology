import os, sys, time

starting_dir = os.getcwd()
util_path = starting_dir + "/util/"
sys.path.insert(0, util_path)
from util import *

def run_AutoHomology(fasta_file, retrievd_csv):
    command = "python download_pdb_chain/download_pdb_chain.py " + retrievd_csv
    os.system(command)
########### end of def run_AutoHomology(fasta_file, retrievd_csv):


if (__name__ == "__main__") :
  total_start_time = time.time()
  args=sys.argv[1:]
  
  if len(args) < 2:
      print "\nPlease provide fasta file for homology modeling and psi-blasted.csv"
      print "Usage:         python run_me.py <fasta file> <csv file>"
      print "Example usage: python DGAT.fasta ZFHADRTG016-Alignment-HitTable.csv"
  
  else:        
    fasta_file = os.path.join(starting_dir, args[0])
    retrievd_csv = os.path.join(starting_dir, args[1])
    
    run_AutoHomology(fasta_file, retrievd_csv)
  
  total_end_time = time.time()
  process = "\nTotal AutoHomology run"
  print show_time(process, total_start_time, total_end_time)
