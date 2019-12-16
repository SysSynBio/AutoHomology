from Bio.PDB import *
import os

pdbl = PDBList()

csv_file = open("ZFHADRTG016-Alignment-HitTable.csv","r")

i = 0
for line in csv_file:
    i = i + 1
    if (i < 3):
        splited_line = line.split(",")
        pdb_id_chain = splited_line[1]
        pdb_id = pdb_id_chain.split("_")[0]
        chain  = pdb_id_chain.split("_")[1]
        
        print "pdb_id:", pdb_id
        pdbl.retrieve_pdb_file(pdb_id)
        
        cif_filename = pdb_id + ".cif"
        print "cif_filename:", cif_filename
        cif_filename_w_path = pdb_id[1] + pdb_id[2] + "/" + cif_filename
        command = "phenix.cif_as_pdb " + cif_filename_w_path
        os.system(command)
        
        
csv_file.close()
