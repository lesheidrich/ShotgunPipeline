from pathlib import Path
from src.blastsearch import BlastSearch
from src.sequence import Sequencer

path = Path.cwd() / 'FASTQ_sample' / 'SRR9855890.fastq.gz'
threshold = 20

if __name__ == '__main__':
    seq = Sequencer(path, threshold)
    blast = BlastSearch()

    filtered = []

    for sequence in seq.sequence_list:
        print(f"\nCommencing next sequence:\n{sequence.seq}\n{sequence.phreds}")

        allmatches = blast._get_all_matches(sequence)
        for m in allmatches:
            print("Next match:")
            print(m['hit'])
            print(m['length'])
            print(m['e-value'])
            print(m['sequence'])
        print("Best Match:")

        try:
            match = blast.get_best_match(sequence)
            print(match)
        except IndexError as e:
            print(f"Empty list returned for match on {sequence}: {e}")
        except Exception as e:
            print(f"Error finding best match for {sequence}: {e}")
