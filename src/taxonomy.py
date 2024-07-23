"""
Bio.Blast.NCBIWWW module docs:
https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html
"""
from typing import Generator
from Bio.Blast import NCBIWWW, NCBIXML


class Taxonomy:
    def __init__(self):
        self.min_e_val = 1

    def blast_search(self, seq: str) -> {}:
        """
        BLAST search on NCBI online nucleotide (nt) DB
        Generator yields alignment hits as dict.
        Eg:
        {'hit': 'gi|2727575369|gb|PP762207.1| Stenotrophomonas maltophilia strain MRC55455 16S ribosomal RNA gene, partial sequence',
         'length': 1403,
         'e-value': 7.21649e-124,
         'sequence': 'TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG'
        }
        :param seq: str of nucleotide sequence
        :return: Generator[Dict[str, Any], None, None] record hit from nt db
        """
        try:
            result = NCBIWWW.qblast("blastn", "nt", seq, hitlist_size=5)
            records = NCBIXML.parse(result)
            for record in records:
                for alignment in record.alignments:
                    for hsp in alignment.hsps:
                        yield {
                            'hit': alignment.title,
                            'length': alignment.length,
                            'e-value': hsp.expect,
                            'sequence': hsp.sbjct
                        }
        except Exception as e:
            print(f"Error during blast on sequence {seq}: {e}")

    def e_val_filter(self, blast: Generator[dict, None, None]) -> {}:
        """
        Utility method filters accepted BLAST results to current lowest e-value.
        :param blast: Generator[Dict[str, Any], None, None] input from self.blast_search()
        :return: Generator[Dict[str, Any], None, None] record hit from nt db
        """
        for result in blast:
            if result['e-value'] <= self.min_e_val:
                self.min_e_val = result['e-value']
                yield result

