import unittest
from pathlib import Path
from src.sequence import Sequence, Sequencer


class TestQC(unittest.TestCase):
    def setUp(self):
        self.path = Path.cwd().parent / 'FASTQ_sample' / 'SRR9855890.fastq.gz'
        self.qc = Sequencer(self.path)

    def test_init_attr(self):
        self.assertEqual(self.qc.path, self.path)
        self.assertEqual(self.qc.threshold, 20)
        self.assertTrue(len(self.qc.sequence_list) > 0)

    def test_trim_seq(self):
        """
        Ensures _trim_seq cuts at first and last index non-inclusive
        Checks sequence str and phreds list for proper content
        :return: None
        """
        seq = 'TACGAATGAT'
        phreds = [32, 15, 33, 32, 18, 29, 32, 35, 19, 29]
        self.assertEqual(len(seq), len(phreds))

        seq, phreds = self.qc._trim_seq(seq, phreds)
        self.assertEqual(len(seq), len(phreds))
        self.assertEqual(phreds, [33, 32, 18, 29, 32, 35])
        self.assertTrue(seq == 'CGAATG')

    def test_sequences(self):
        """
        Ensures sequence and phreds content is created correctly
        :return: None
        """
        self.assertIn('SRR9855890.1', self.qc.sequence_list[0].id)
        self.assertGreater(len(self.qc.sequence_list[0].seq), 200)
        self.assertIn('GGGTGCAAGCGTTAATC', self.qc.sequence_list[0].seq)
        self.assertIn(17, self.qc.sequence_list[0].phreds)
        self.assertTrue(min(self.qc.sequence_list[0].phreds) >= 0)
        self.assertEqual(len(self.qc.sequence_list[0].phreds), 239)
        self.assertEqual(len(self.qc.sequence_list[0].phreds), len(self.qc.sequence_list[0].seq))


class TestSequence(unittest.TestCase):
    def setUp(self):
        self.seq_id = "seq1"
        self.sequence = "ATGC"
        self.phreds = [30, 31, 32, 33]
        self.sq = Sequence(self.seq_id, self.sequence, self.phreds)

    def test_init(self):
        self.assertEqual(self.sq.id, self.seq_id)
        self.assertEqual(self.sq.seq, self.sequence)
        self.assertEqual(self.sq.phreds, self.phreds)

    def test_str_method(self):
        expected = f"Sequence ID: {self.seq_id}\nSequence: {self.sequence}\nPhreds: {self.phreds}\n"
        self.assertEqual(str(self.sq), expected)
