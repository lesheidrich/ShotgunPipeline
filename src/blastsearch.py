from typing import Generator, Dict, Any
from Bio.Blast import NCBIWWW, NCBIXML


class BlastSearch:
    def __init__(self):
        self.min_e_val = 1

    def _get_all_matches(self, seq: str, db: str = 'nt') -> Generator[Dict[str, Any], None, None]:
        """
        BLAST search on NCBI online DB, defaults to nucleotide (nt)
        Generator yields alignment hits as dict.
        Eg:
        {'hit': 'gi|2727575369|gb|PP762207.1| Stenotrophomonas maltophilia strain MRC55455 16S ribosomal RNA gene, partial sequence',
         'length': 1403,
         'e-value': 7.21649e-124,
         'sequence': 'TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG'
        }
        :param seq: str of nucleotide sequence
        :param db: str of database to search, see notes/blast_notes.md for db list
        :return: Generator[Dict[str, Any], None, None] record hit from nt db
        """
        try:
            result = NCBIWWW.qblast("blastn", db, seq, hitlist_size=5)
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
            print(f"Error during blast search on sequence {seq} for db {db}: {e}")

    def _e_val_filter(self, blast: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
        """
        Utility method filters accepted BLAST results returning lowest e-value as long as it's smaller than the
        current smallest e-value.
        :param blast: Generator[Dict[str, Any], None, None] input from self.blast_search()
        :return: Generator[Dict[str, Any], None, None] record hit from nt db
        """
        for result in blast:
            if result['e-value'] <= self.min_e_val:
                self.min_e_val = result['e-value']
                yield result

    def get_best_match(self, seq: str) -> Dict[str, Any]:
        """
        Collects pre-filtered BLAST search results.
        Sorts by asc 'e-value' and desc 'length' making [0] the optimal result to return
        :param seq: str of sequence to process
        :return: Dict[str, Any] of BLAST result
        """
        filtered = []
        blast = self._get_all_matches(seq)
        [filtered.append(result) for result in self._e_val_filter(blast)]
        filtered.sort(key=lambda x: (x['e-value'], -x['length']))
        return filtered[0]
