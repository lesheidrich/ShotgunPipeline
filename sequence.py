from pathlib import Path
from typing import List, Tuple
from Bio import SeqIO
import gzip


class Sequence:
    def __init__(self, id: str, seq: str, phreds: List[int]):
        self.id = id
        self.seq = seq
        self.phreds = phreds

    def __str__(self):
        return f"Sequence ID: {self.id}\nSequence: {self.seq}\nPhreds: {self.phreds}\n"


class QC:
    def __init__(self, path: Path, threshold: int = 20):
        self.path = path
        self.threshold = threshold
        self.sequence_list = []
        self._fastq_2_list()

    def _trim_seq(self, seq: str, phreds: List[int]) -> Tuple[str, List[int]]:
        """
        Utility method trims sequence and phreds list based on first and last
        phreds confidence value that doesn't exceed QC.threshold.
        :param seq: str for nucleotide sequence
        :param phreds: List[int] phreds confidence values matching nucleotides
        :return: trimmed sequence str and phreds int list
        """
        start_i = next((i for i in range(len(phreds)) if phreds[i] <= self.threshold), None)
        end_i = next((i for i in reversed(range(len(phreds))) if phreds[i] <= self.threshold), None)

        if start_i is None or start_i == end_i:
            return seq, phreds

        return seq[start_i + 1:end_i], phreds[start_i + 1:end_i]

    def _fastq_2_list(self) -> None:
        """
        Reads FASTQ from QC.path
        Parses sequence data into Sequence instance with params: id, sequence, phreds
        Instances are appended to QC.sequence_list.
        :return: None
        """
        try:
            with gzip.open(self.path, 'rt') as f:
                for sequence in SeqIO.parse(f, 'fastq'):
                    self.sequence_list.append(Sequence(
                            sequence.id,
                            *self._trim_seq(str(sequence.seq),
                                            sequence.letter_annotations['phred_quality']))
                    )
        except Exception as e:
            print(f"Error reading {self.path}: {e}")




