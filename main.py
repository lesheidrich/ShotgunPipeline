from pathlib import Path
from src.sequence import QC
from src.taxonomy import Taxonomy

path = Path.cwd() / 'FASTQ_sample' / 'SRR9855890.fastq.gz'
threshold = 20

seq = 'TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG'


# qc = QC(path)
t = Taxonomy()

# min_e = 1
# results = []
#
# blast = t.blast_search(seq)
# for result in blast:
#
#     if result['e-value'] <= min_e:
#         results.append(result)
#         min_e = result['e-value']
#
#     print(result)
#     print(type(result['hit']))
#     print(type(result['length']))
#     print(type(result['e-value']))
#     print(type(result['sequence']))
#
# print(results)

blast = t.blast_search(seq)
for result in t.e_val_filter(blast):
    print(result['hit'])
    print(result['length'])
    print(result['e-value'])
    print(result['sequence'])

print("*"*3)
print("*"*3)
print("*"*3)

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

"""                         'hit': alignment.title,
                            'length': alignment.length,
                            'e-value': hsp.expect,
                            'sequence': hsp.sbjct
*e - value - error
prob
*length - longer is better(context)
*alignment
length - longer is better
*percentage
identity - how
similar
sequences
are
*coverage - higher is better
*additional
context - strains
mentioned
"""

# seq = 'TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG'
# phreds = [32, 33, 32, 32, 18, 29, 32, 32, 32, 29, 29, 32, 38, 38, 38, 37, 17, 36, 36, 36, 37, 38, 39, 38, 38, 38, 32, 37, 38, 37, 39, 39, 39, 34, 17, 37, 36, 36, 38, 38, 39, 39, 38, 32, 16, 33, 36, 36, 38, 38, 34, 37, 38, 39, 38, 32, 18, 15, 15, 33, 33, 38, 38, 39, 39, 37, 20, 37, 19, 37, 38, 38, 36, 39, 37, 39, 33, 38, 39, 39, 17, 37, 38, 38, 37, 38, 37, 37, 34, 38, 37, 38, 37, 39, 37, 37, 39, 38, 39, 36, 39, 35, 19, 35, 38, 37, 38, 37, 38, 37, 39, 38, 36, 14, 33, 36, 39, 39, 39, 38, 39, 39, 39, 38, 27, 38, 39, 39, 39, 39, 39, 39, 39, 38, 38, 35, 33, 38, 37, 38, 39, 38, 38, 38, 39, 37, 39, 39, 36, 39, 37, 33, 38, 38, 37, 38, 35, 38, 38, 37, 39, 38, 36, 37, 36, 37, 35, 33, 33, 38, 35, 16, 38, 35, 37, 36, 39, 36, 39, 39, 38, 38, 37, 32, 33, 16, 33, 16, 14, 34, 38, 38, 39, 39, 39, 39, 39, 39, 39, 38, 33, 32, 16, 32, 39, 39, 37, 39, 38, 36, 32, 32, 32, 33, 17, 33, 16, 37, 37, 37, 37, 37, 38, 38, 34, 38, 33, 32, 15, 15, 36, 38, 36, 37, 37, 38, 38, 38, 38, 38, 38, 37, 37, 37, 33, 37, 37, 37, 32, 32, 32, 32, 32]

# seq = 'ATCGCGCGTTATATGGC'









