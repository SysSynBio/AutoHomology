from Bio.PDB import *

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
        filename = pdb_id + ".pdb"
        print "pdb_id:", pdb_id
        print "filename:", filename
        pdbl.retrieve_pdb_file(pdb_id)
        io = PDBIO()
        io.set_structure(s)
        io.save(filename)
     
csv_file.close()
