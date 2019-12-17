#!/usr/bin/perl
####################################################
#perl pdb2fasta.pl pdbfile
#
#convert pdb file to fasta file format for MSA
#
#modified on JUNE 13,2005 by huxz (credit Jenny Hu)
####################################################
if (@ARGV<1) {
  print "USAGE: pdb2fasta.pl PDBFILE \n";
  exit;
}

$pdb = $ARGV[0];
$leng = length($pdb);
$pcode = substr($pdb,0,$leng-3);

#read the usual matix
open(IN, "<$ARGV[0]");
if(!IN){
  print "not able to open\n";
}

open(IN, "< $ARGV[0]");
$nres = 0;
while ((<IN>)) {
  if (substr($_, 0, 6) eq "ATOM  ") {
    $atom   = substr($_, 12, 3);
    $res    = substr($_, 17, 3);
    $chid   = substr($_, 21, 1);
    if ($atom eq " CA") { #read the sequence, CA atom
	$CA[$nres] = $res;
	$Chain[$nres] = $chid;
      $nres++;
    }
	}
}

close(IN);

open(OUT,">$pcode" . "fasta");

#print the header
print OUT ">" . " " . $pdb ."|CHAIN: " . $Chain[0] . " |SEQUENCE" . "\n";
for ($i = 0; $i<$nres; $i++) {
	$seq = convert($CA[$i]);
	if ( $i > 0){
	    if ( $Chain[$i] ne $Chain[$i-1]) {
		print OUT "\n" . ">" . " " . $pdb ."|CHAIN: " . $Chain[$i] . " |SEQUENCE" . "\n";
	    }
	}
	print OUT "$seq";
}
print OUT "\n";
close(OUT);

#subroutine to convert 3 letter sequence to 1 letter sequence
sub convert{
	my($seq_1);
	my($seq) = $_[0];
	if ($seq eq "ALA"){
		$seq_1 = 'A';
	}elsif ($seq eq "CYS"){
		$seq_1 = 'C';
	}elsif ($seq eq "ASP"){
		$seq_1 = 'D';
	}elsif ($seq eq "GLU"){
		$seq_1 = 'E';
	}elsif ($seq eq "PHE"){
		$seq_1 = 'F';
	}elsif ($seq eq "GLY"){
		$seq_1 = 'G';
	}elsif ($seq eq "HIS"){
		$seq_1 = 'H';
	}elsif ($seq eq "ILE"){
		$seq_1 = 'I';
	}elsif ($seq eq "LYS"){
		$seq_1 = 'K';
	}elsif ($seq eq "LEU"){
		$seq_1 = 'L';
	}elsif ($seq eq "MET"){
		$seq_1 = 'M';
	}elsif ($seq eq "ASN"){
		$seq_1 = 'N';
	}elsif ($seq eq "PRO"){
		$seq_1 = 'P';
	}elsif ($seq eq "GLN"){
		$seq_1 = 'Q';
	}elsif ($seq eq "ARG"){
		$seq_1 = 'R';
	}elsif ($seq eq "SER"){
		$seq_1 = 'S';
	}elsif ($seq eq "THR"){
		$seq_1 = 'T';
	}elsif ($seq eq "VAL"){
		$seq_1 = 'V';
	}elsif ($seq eq "TRP"){
		$seq_1 = 'W';
	}elsif ($seq eq "TYR"){
		$seq_1 = 'Y';
	}else{
		$seq_1 = 'X';
	}
	return $seq_1;
}
