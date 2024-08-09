hit = 'gi|2727575369|gb|PP762207.1| Stenotrophomonas maltophilia strain MRC55455 16S ribosomal RNA gene, partial sequence'

subsec = hit.split('|')
# GeneInfo ID (NCBI)
gi = subsec[1]
# GenBank db accession number
gb = subsec[3]
name = subsec[4].split(',')[0].strip()

partial = True if 'partial sequence' == subsec[4].split(',')[1].strip() else False



print(gi)
print(gb)
print(name)
print(partial)
