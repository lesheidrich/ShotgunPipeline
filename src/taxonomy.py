
from Bio.Blast import NCBIWWW, NCBIXML


class Taxonomy:

    def blast_search(self, seq: str) -> {}:
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


    def filter(self):
        pass