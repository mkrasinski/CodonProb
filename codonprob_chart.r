codonprob_chart <- function(aa, data_file){

 if( identical(aa, "Alanine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("GCU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Alanine prob", ylab="Codon prob")
  points(df1[grep("GCC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("GCA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("GCG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("GCU", "GCC", "GCA", "GCG"), col=c("red","blue","green","yellow"), pch=19)
  return()
 } else

 if( identical(aa, "Leucine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UUA",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Leucine prob", ylab="Codon prob")
  points(df1[grep("UUG",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("CUU",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("CUC",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  points(df1[grep("CUA",df1$V3),c('V2','V4')], type="p", pch = 19, col="orange")
  points(df1[grep("CUG",df1$V3),c('V2','V4')], type="p", pch = 19, col="purple")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UUA", "UUG", "CUU", "CUC", "CUA", "CUG"), 
  col=c("red","blue","green","yellow","orange","purple"), pch=19)
  return()
 } else
 
 if( identical(aa, "Arginine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("CGU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Arginine prob", ylab="Codon prob")
  points(df1[grep("CGC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("CGA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("CGG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  points(df1[grep("AGA",df1$V3),c('V2','V4')], type="p", pch = 19, col="orange")
  points(df1[grep("AGG",df1$V3),c('V2','V4')], type="p", pch = 19, col="purple")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("CGU", "CGC", "CGA", "CGG", "AGA", "AGG"), 
  col=c("red","blue","green","yellow","orange","purple"), pch=19)
  return()
 } else

 if( identical(aa, "Lysine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("AAA",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Lysine prob", ylab="Codon prob")
  points(df1[grep("AAG",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("AAA", "AAG"), 
  col=c("red","blue"), pch=19)
  return()
 } else

 if( identical(aa, "Asparagine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("AAU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Asparagine prob", ylab="Codon prob")
  points(df1[grep("AAC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("AAU", "AAC"), 
  col=c("red","blue"), pch=19)
  return()
 } else
 
 if( identical(aa, "Methionine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("AUG",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Methionine prob", ylab="Codon prob")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("AUG"), 
  col=c("red"), pch=19)
  return()
 } else
 
 if( identical(aa, "Aspartic_acid") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("GAU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Aspartic acid prob", ylab="Codon prob")
  points(df1[grep("GAC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("GAU", "GAC"), 
  col=c("red","blue"), pch=19)
  return()
 } else
 
 if( identical(aa, "Phenylalanine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UUU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Phenylalanine prob", ylab="Codon prob")
  points(df1[grep("UUC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UUU", "UUC"), 
  col=c("red","blue"), pch=19)
  return()
 } else
 
 if( identical(aa, "Cysteine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UGU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Cysteine prob", ylab="Codon prob")
  points(df1[grep("UGC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UGU", "UGC"), 
  col=c("red","blue"), pch=19)
  return()
 } else 
 
 if( identical(aa, "Proline") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("CCU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Proline prob", ylab="Codon prob")
  points(df1[grep("CCC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("CCA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("CCG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("CCU", "CCC", "CCA", "CCG"), 
  col=c("red","blue","green","yellow"), pch=19)
  return()
 } else
 
 if( identical(aa, "Glutamine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("CAA",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Glutamine prob", ylab="Codon prob")
  points(df1[grep("CAG",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("CAA", "CAG"), 
  col=c("red","blue"), pch=19)
  return()
 } else 
 
 if( identical(aa, "Serine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UCU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Serine prob", ylab="Codon prob")
  points(df1[grep("UCC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("UCA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("UCG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  points(df1[grep("AGU",df1$V3),c('V2','V4')], type="p", pch = 19, col="orange")
  points(df1[grep("AGC",df1$V3),c('V2','V4')], type="p", pch = 19, col="purple")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UCU", "UCC", "UCA", "UCG", "AGU", "AGC"), 
  col=c("red","blue","green","yellow","orange","purple"), pch=19)
  return()
 } else
 
 if( identical(aa, "Glutamic_acid") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("GAA",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Glutamic acid prob", ylab="Codon prob")
  points(df1[grep("GAG",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("GAA", "GAG"), 
  col=c("red","blue"), pch=19)
  return()
 } else
 
 if( identical(aa, "Threonine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("ACU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Threonine prob", ylab="Codon prob")
  points(df1[grep("ACC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("ACA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("ACG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("ACU", "ACC", "ACA", "ACG"), 
  col=c("red","blue","green","yellow"), pch=19)
  return()
 } else
 
 if( identical(aa, "Glycine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("GGU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Glycine prob", ylab="Codon prob")
  points(df1[grep("GGC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("GGA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("GGG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("GGU", "GGC", "GGA", "GGG"), 
  col=c("red","blue","green","yellow"), pch=19)
  return()
 } else
 
 if( identical(aa, "Tryptophane") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UGG",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Tryptophane prob", ylab="Codon prob")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UGG"), 
  col=c("red"), pch=19)
  return()
 } else
 
 if( identical(aa, "Histidine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("CAU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Histidine prob", ylab="Codon prob")
  points(df1[grep("CAC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("CAU", "CAC"), 
  col=c("red","blue"), pch=19)
  return()
 } else
 
 if( identical(aa, "Tyrosine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UAU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Tyrosine prob", ylab="Codon prob")
  points(df1[grep("UAC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UAU", "UAC"), 
  col=c("red","blue"), pch=19)
  return()
 } else
 
 if( identical(aa, "Isoleucine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("AUU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Isoleucine prob", ylab="Codon prob")
  points(df1[grep("AUC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("AUA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("AUU", "AUC", "AUA"), 
  col=c("red","blue","green"), pch=19)
  return()
 } else
 
 if( identical(aa, "Valine") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("GUU",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="Valine prob", ylab="Codon prob")
  points(df1[grep("GUC",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("GUA",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  points(df1[grep("GUG",df1$V3),c('V2','V4')], type="p", pch = 19, col="yellow")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("GUU", "GUC", "GUA", "GUG"), 
  col=c("red","blue","green","yellow"), pch=19)
  return()
 } else
 
 if( identical(aa, "STOP") ) {
  df<-read.table(data_file)
  df1<-df[grep(aa,df$V1),]
  plot(df1[grep("UAA",df1$V3),c('V2','V4')], type="p", pch = 19, col="red", 
  xlim=c(0,max(df1$V2)+(0.3*max(df1$V2))), ylim=c(0,max(df1$V4)+(0.3*max(df1$V4))), xlab="STOP prob", ylab="Codon prob")
  points(df1[grep("UGA",df1$V3),c('V2','V4')], type="p", pch = 19, col="blue")
  points(df1[grep("UAG",df1$V3),c('V2','V4')], type="p", pch = 19, col="green")
  legend(max(df1$V2)+(0.1*max(df1$V2)), max(df1$V4)+(0.3*max(df1$V4)), c("UAA", "UGA", "UAG"), 
  col=c("red","blue","green"), pch=19)
  return()
 } else
 
 
 cat("Usage: codonprob_chart(\"AminoAcid\",\"data_file\")\n\n")
 cat("AminoAcids : Alanine,Leucine,Arginine,Lysine,Asparagine,Methionine\n,Aspartic_acid, Phenylalanine,Cysteine,Proline,Glutamine,Serine,\nGlutamic_acid,Threonine,Glycine,Tryptophane,Histidine,Tyrosine,\nIsoleucine,Valine,STOP\n")
}

