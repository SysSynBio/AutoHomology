# credit: Chang Joon Lee?
from Bio.PDB import *
parser = PDBParser(PERMISSIVE=1)

import gzip, os, shutil, sys, time
from os import popen, system
from os.path import exists, basename

io = PDBIO()

remote_host = ''
def download_pdb(pdb_id, dest_dir):
    print "downloading %s" % ( pdb_id )
    url = 'http://www.rcsb.org/pdb/files/%s.pdb.gz' % (pdb_id.upper())
    dest = '%s/%s.pdb.gz' % (os.path.abspath(dest_dir), pdb_id.lower()) 
    wget_cmd = 'wget --quiet %s -O %s' % (url, dest)
    print wget_cmd
    if remote_host:
        wget_cmd = 'ssh %s %s' % (remote_host, wget_cmd)
    lines = popen(wget_cmd).readlines()
    if (exists(dest)):
        return dest
    else:
        print "Error: didn't download file!"
############ end of def download_pdb(pdb_id, dest_dir):


def download_pdb_chain(*args):
    
    starting_dir = args[0]
    retrievd_csv = args[1]
    
    csv_file = open(retrievd_csv,"r")
    i = 0
    for line in csv_file:
        i = i + 1
        if (i < 3):
            splited_line = line.split(",")
            pdb_id_chain = splited_line[1]
            pdb_id = pdb_id_chain.split("_")[0]
            chain_id  = pdb_id_chain.split("_")[1]
            
            print "pdb_id:", pdb_id
            pdb_file_name = pdb_id + ".pdb"
            compressed_pdb_filename = download_pdb(pdb_id, '.')
            print compressed_pdb_filename
            
            decompressed_pdb_filename = compressed_pdb_filename[:-3]
            
            with gzip.open(compressed_pdb_filename, 'rb') as f_in:
                with open(decompressed_pdb_filename, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(compressed_pdb_filename)
            
            structure = parser.get_structure(pdb_id, decompressed_pdb_filename)
            
            model = structure[0]
            selected_chain = model[chain_id]
            os.remove(decompressed_pdb_filename)
            
            io.set_structure(selected_chain)
            output_file_name = decompressed_pdb_filename[:-4] + "_" + str(chain_id) + ".pdb"
            io.save(output_file_name)
    csv_file.close()
########### end of def download_pdb_chain(retrievd_csv):


if (__name__ == "__main__") :
    total_start_time = time.time()
    args=sys.argv[1:]

    starting_dir = args[0]
    retrievd_csv = args[1]

    util_path = starting_dir + "/util/"
    sys.path.insert(0, util_path)
    from util import *
    
    download_pdb_chain(starting_dir, retrievd_csv)
    
    total_end_time = time.time()
    process = "\npdb download and parsing"
    print show_time(process, total_start_time, total_end_time)
