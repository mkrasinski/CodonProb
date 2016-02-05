#!/usr/bin/perl -w
#
use strict;
use warnings;

if ($#ARGV != 3) {die "Program requires parameters! [file] [delim] [mode] [cutoff]\n";}

my $n1=substr($ARGV[0],0,rindex($ARGV[0],"."));
my $delim=$ARGV[1];
$delim = "\t" if $ARGV[1] eq "tab";
my $mode=$ARGV[2];
my $cutoff=$ARGV[3];
#print "$delim $mode $cutoff\n";

open(GOUT, "> $n1.svmprep ") or die "Can not open an input file: $!";#output file

open(DANE1, "< $ARGV[0]") or die "Can not open an input file: $!";#reads in the file
my @file1=<DANE1>;
close (DANE1);
chomp @file1;


for my $i (0..$#file1){
	my ($class);
	my $blin=$file1[$i];	
	my @blinia=split(/$delim/,$blin);
	if($mode eq "r"){$class=$blinia[1];}
	elsif($mode eq "c"){
		if($blinia[0] <= $cutoff){
		$class=-1;
		}
		elsif($blinia[0] >= $cutoff){
		$class=1;
		}
	}
	my $comment=$blinia[1];
	printf GOUT "$class\t";
	for my $k (2..$#blinia){
		my $feature=$k-1;
		if(defined $blinia[$k]) {
			my $value=$blinia[$k];
			if($value eq ""){
				$value=0;
				printf GOUT "$feature:$value\t";
			}
			elsif($value=~/[a-zA-Z]+/){
                                $value=0;
                                printf GOUT "$feature:$value\t";
                        }
			else{
			printf GOUT "$feature:$value\t";
			}
		}	
		else{
			my $value=0;
			printf GOUT "$feature:$value\t";
		}
	}	
	print GOUT "\#$comment\n";
}
