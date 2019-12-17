import glob, os, sys

from Bio import pairwise2, SeqIO
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist
matrix = matlist.blosum62


def make_grishin_files(*args):
    target_fasta_file = args[0]
    
    targe_fasta_sequences = SeqIO.parse(open(target_fasta_file), 'fasta')
    target_sequence = ''
    for targe_fasta in targe_fasta_sequences:
        name, target_sequence = targe_fasta.id, str(targe_fasta.seq)
        print "target_sequence:", target_sequence
    
    if (os.path.isfile("input_for_clustal_omega.fasta") == True):
            os.remove("input_for_clustal_omega.fasta")
        
    for pdb_file in glob.glob("*.pdb"):
        command = "perl ../util/single_pdb2fasta.pl " + pdb_file
        print command
        os.system(command)
        
        query_fasta_file = pdb_file[:-4] + ".fasta"
        query_fasta_sequences = SeqIO.parse(open(query_fasta_file), 'fasta')
        for query_fasta in query_fasta_sequences:
            name, query_sequence = query_fasta.id, str(query_fasta.seq)
            print "query_sequence:", query_sequence
        
            for a in pairwise2.align.globaldx (target_sequence, query_sequence, matrix):
                
                first_aligned = ''
                second_aligned = ''
                first_aligned_finished = False
                total_string = ''
                for char in format_alignment(*a):
                    total_string = total_string + str(char)
                    Score_candidate = total_string[len(total_string)-5:len(total_string)]
                    if (Score_candidate == "Score"):
                        second_aligned = second_aligned[1:len(second_aligned)-4]
                        break
                    if ((char != "|") \
                         and (char != ".") \
                         and (char != " ")):
                        if (first_aligned_finished == False):
                            first_aligned = first_aligned + str(char)
                        else:
                            second_aligned = second_aligned + str(char)
                    elif ((char == "|") \
                       or (char == ".") \
                       or (char == " ")):
                        first_aligned_finished = True
                        continue
                print "first_aligned:",first_aligned
                print "second_aligned:",second_aligned
        
        target_fasta_file = os.path.basename(target_fasta_file)
        grishin_file_name = target_fasta_file[:-6] + "_" + query_fasta_file[:-6] + ".grishin"
        print grishin_file_name
        
        f_out = open(grishin_file_name, 'w')
        write_this = "## " + target_fasta_file[:-6] + " " + query_fasta_file[:-6] + "\n"
        print write_this
        f_out.write(write_this)
        f_out.write("#\n")
        f_out.write("scores from program: 0\n")
        write_this = "0 " + first_aligned
        f_out.write(write_this)
        write_this = "0 " + second_aligned
        f_out.write(write_this)
        f_out.close()
############### end of def make_grishin_files(*args):


if (__name__ == "__main__") :
    args=sys.argv[1:]
    print args
    target_fasta_file = args[0]
    make_grishin_files(target_fasta_file)
    