'''
Created on Mar 12, 2014

@author: yqian33
'''
    
def proteinEvalue():
    from Bio.Blast import NCBIWWW
    from Bio.Blast import NCBIXML
    from Bio import SeqIO
    from Bio import AlignIO
    
    peptide = "tpdavmgnpk"
    myEntrezQuery = "Homo sapiens[Organism]"
    
    record_handle = SeqIO.parse("/home/yqian33/APPI/dataset/ProteinSequences/seq1.fasta", "fasta")
    for record in record_handle:
        print record.seq
        #/home/yqian33/Public/ncbi-blast-2.2.29+/db/uniprot-human_protein.fasta
        result  = NCBIWWW.qblast("blastp", "/home/yqian33/Public/ncbi-blast-2.2.29+/db/SGD_orf_trans_all.fasta", record)
        records = NCBIXML.parse(result)
        print 'blast'
        blast_record = records.next()
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                #if hsp.expect < 5:
                print "***** RECORD ****"
                    #print "sequence:", alignment.title
                print "E-value:", hsp.expect
                
def blast2seq():
    
    import os
    import commands
    
    os.chdir('/home/yqian33/APPI/dataset/ProteinSequences')
    #result = os.popen('time blastp -query seq1.fasta -subject seq2.fasta')
    result = os.popen('time blastp  -query Yiwei_Yeast_protensemble.fas -subject SGD_orf_trans_all.fasta -out result.txt')
    #result = os.popen('time blastp  -query seq2.fasta -subject seq1.fasta')
    print result.read()

    result.close()
    #for line in result:
        #print line

def countProtein():
    ins = open('/home/yqian33/APPI/dataset/AlignMCLdataset/ort/human-fly.ort', 'r')  #14615
    out = open("human_proteinSeq.txt", "w")
    #ins = open('/home/yqian33/APPI/dataset/AlignMCLdataset/ppi/human.all.nif', 'r')
    
    count = 0;
    preProtein = ''
    for line in ins:
        eachLine = line.split('\t')
        #print preProtein != eachLine[0]
        if preProtein != eachLine[0]:
            out.write(eachLine[0]+'\n')
            count = count + 1
        preProtein = eachLine[0]
        #print preProtein
    print count
    ins.close()
    out.close()


  
def countProteinInFasta():
    #human(H.s) protein
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/uniprot-human9606.fasta', 'r')                 #20264
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/Ensembl_Homo_sapiens.GRCh37.75.pep.all.fa', 'r')  #104763
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/ncbi_human_sequence.fasta', 'r')   #70104
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/uniprot_human9606.fasta', 'r')   #88703 UNIPROT     *********
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/human_refseqprotein.fa', 'r')   #71338
    
    #yeast(S.c) protein  - near 6700
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/SGD_orf_trans_all.fasta', 'r')                                  #6717 *********
    #ins = open('/home/yqian33/APPI/dataset/Yiwei_Yeast_protensemble.fas', 'r')                                               #6692
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/Ensembl_Saccharomyces_cerevisiae.R64-1-1.75.pep.all.fa', 'r')   #6692
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/uniprot-yeast4932.fasta', 'r')   #7802 from web interface   **********
    #ins = open('/home/yqian33/Downloads/4932.seq', 'r')   #7379
    #ins = open('/home/yqian33/Downloads/YEAST.fasta', 'r')   #6643 UNIPROT
    
    #full DIP
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/DIP_fasta20131201.seq', 'r')     #25749
    
    #fly(D.m) protein
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/Ensembl_Drosophila_melanogaster.BDGP5.75.pep.all.fa', 'r')         #26950, 23388 in Entrez
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/Ensembl_Drosophila_melanogaster.BDGP5.75.pep.abinitio.fa', 'r')     #41246
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/flybase_dpse-all3.1.fasta', 'r')   #16857 ********** tax id is not 7227 is 529925
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/ncbi_fly_sequence.fasta', 'r')   #27552
    #ins = open('/home/yqian33/Downloads/DROME.fasta', 'r')   #20980 uniprot 7227

    #worm(C.e) protein
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/Wormbase_C_Elegans.PRJNA13758.WS241.protein.fa', 'r')     #26983  *******
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/worm6293.fasta', 'r')     #26046
    #ins = open('/home/yqian33/Downloads/CAEEL.fasta', 'r')   #26906 uniprot
    
    #mouse
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/mouse/uniprot_mouse10090.fasta', 'r')   #51388 uniprot
    #ins = open('/home/yqian33/APPI/dataset/ProteinSequences/mouse/ensembl_Mus_musculus.GRCm38.75.pep.abinitio.fa', 'r')   #56884 ensembl
    ins = open('/home/yqian33/APPI/dataset/ProteinSequences/mouse/ncbi_mouse10090.fasta', 'r')   #74891 ncbi
    
    count = 0;
    for line in ins:
        #eachLine = line.split('\t')
        #print preProtein != eachLine[0]
        if line[0] =='>':
            #print 'here'
            count = count + 1
        #print preProtein
    print count
    ins.close()

def cleanE():
    ins = open("/home/yqian33/APPI/dataset/E-value/psiBLAST/psiblast-1passTop10/yeast-human.blast", 'r')
    ous = open("/home/yqian33/APPI/dataset/E-value/psiBLAST/psiblast-1passTop10/yeast-human.blaste10", 'w')
    count = 0
    for line in ins:
        eachline = line.split("\t")
        evalue = float(eachline[2])
        if evalue < 1e-10:
            ous.write(line)
            count = count + 1 
            
    print count
    ins.close()
    ous.close()
    
def formatBLAST():
    ins = open('/home/yqian33/APPI/dataset/E-value/psiBLAST/psiresult/worm-fly-blast.txt','r')   
    ous = open('/home/yqian33/APPI/dataset/E-value/psiBLAST/worm-fly-blast.txt', 'w')
    
    for line in ins:
        item = line.split('\t')
        ous.write(item[0]+'\t'+item[1]+'\t'+item[10]+'\n')
    ins.close()
    ous.close()
    print 'done'
    
if __name__ == '__main__':
    #pass
    #blast2seq();
    #proteinEvalue()
    #countProtein()
    #countProteinInFasta()
    #getEntrezIdFromSeq()
    cleanE()
    #formatBLAST()
    pass