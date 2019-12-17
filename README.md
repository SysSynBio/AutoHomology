# AutoHomology
Automatically performs rosetta based Homology modeling. For now, semi-automatic.

For any suggestions/inquiries, please email doonam.kim@pnnl.gov


- Procedures

1. Run psi-blast with pdb databank at
https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE=Proteins&PROGRAM=blastp&RUN_PSIBLAST=on

2. Download Hit Table (CSV)
For example, ZFHADRTG016-Alignment-HitTable.csv

3. python run_me.py <fasta> <csv>

4. Upload input_for_clustal_omega.fasta at https://www.ebi.ac.uk/Tools/msa/clustalo
