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
    
    os.chdir(destDir)
    target_fasta_file = os.path.basename(target_fasta_file)
    for pdb_file in glob.glob("*.pdb"):
        grishin_file_name = target_fasta_file[:-6] + "_" + pdb_file[:-4] + ".grishin"
        print grishin_file_name
        run_to_hybridize = open("run_to_hybridize.sh", "w")
        write_this = "partial_thread.default.macosclangrelease -in:file:fasta " + str(target_fasta_file) \
                    + " -in:file:alignment " + str(grishin_file_name) + " -in:file:template_pdb " \
                    + str(pdb_file) + "\n"
        run_to_hybridize.write(write_this)
        run_to_hybridize.close()
        
        command = "source run_to_hybridize.sh "
        os.system(command)
        
        hybridized_pdb_file = pdb_file + ".pdb"
        renamed_hybridized_pdb_file = grishin_file_name[:-8] + "_hybridized.pdb"
        shutil.copy(hybridized_pdb_file, renamed_hybridized_pdb_file)
############### end of def prepare_to_hybridize(*args):


if (__name__ == "__main__") :
    args=sys.argv[1:]
    print args
    target_fasta_file = args[0]
    
    prepare_to_hybridize(target_fasta_file)
    