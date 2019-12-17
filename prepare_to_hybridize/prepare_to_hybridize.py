import glob, os, shutil, sys, time

util_path = "../util/"
sys.path.insert(0, util_path)
from util import *

def prepare_to_hybridize(*args):
    target_fasta_file = args[0]
    
    os.mkdir("2_threading")
    
    current_dir = os.getcwd()
    destDir = os.path.join(current_dir, "2_threading")
    print current_dir
    print destDir
    
    shutil.copy(target_fasta_file, destDir)
    
    moveAllFilesinDir(current_dir, destDir)
############### end of def prepare_to_hybridize(*args):


if (__name__ == "__main__") :
    args=sys.argv[1:]
    print args
    target_fasta_file = args[0]
    
    prepare_to_hybridize(target_fasta_file)
    