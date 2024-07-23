"""
Bio.Blast.NCBIWWW module docs:
https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html
"""
from typing import Generator
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

    def e_val_filter(self, blast: Generator[dict, None, None]) -> {}:
        min_e = 1
        print("min e", min_e)
        for result in blast:
            if result['e-value'] <= min_e:
                min_e = result['e-value']
                yield result

