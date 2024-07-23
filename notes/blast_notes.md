#### sort hit
* e-value - error prob
* length  - longer is better (context)
* alignment length - longer is better
* percentage identity - how similar sequences are
* coverage - higher is better
* additional context - strains mentioned

#### docs
https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html

#### sample output
```
<_io.StringIO object at 0x0000028D964C9900>
records <generator object parse at 0x0000028D96D34EB0>
<Bio.Blast.NCBIXML.Blast object at 0x0000028D96D6BB90>

Hit: gi|2738637555|gb|PP859116.1| Stenotrophomonas maltophilia strain OTU47M2310 16S ribosomal RNA gene, partial sequence
Length: 1469
E-value: 7.21649e-124
Sequence: TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG

Hit: gi|2727575369|gb|PP762207.1| Stenotrophomonas maltophilia strain MRC55455 16S ribosomal RNA gene, partial sequence
Length: 1403
E-value: 7.21649e-124
Sequence: TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG

Hit: gi|2577265878|gb|OR553731.1| Stenotrophomonas sp. strain F13 16S ribosomal RNA gene, partial sequence
Length: 1075
E-value: 7.21649e-124
Sequence: TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG

Hit: gi|2575652401|gb|OR534735.1| Uncultured bacterium clone 5fdd3cce9fd69b38c95afeb50b467f07 16S ribosomal RNA gene, partial sequence
Length: 379
E-value: 7.21649e-124
Sequence: TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG

Hit: gi|2505753124|gb|OQ983545.1| Stenotrophomonas sp. strain YCR3A-1 16S ribosomal RNA gene, partial sequence
Length: 1449
E-value: 7.21649e-124
Sequence: TACGAAGGGTGCAAGCGTTACTCGGAATTACTGGGCGTAAAGCGTGCGTAGGTGGTCGTTTAAGTCTGTTGTGAAAGCCCTGGGCTCAACCTGGGAACTGCAGTGGAAACTGGACGACTAGAGTGTGGTAGAGGGTAGCGGAATTCCTGGTGTAGCAGTGAAATGCGTAGAGATCAGGAGGAACATCCATGGCGAAGGCAGCTACCTGGACCAACACTGACACTGAGGCACGAAAGCGTGGGGAGCAAACAGG
```

#### DBs
| Name                           | Type    | Title                                                                                   |
|--------------------------------|---------|-----------------------------------------------------------------------------------------|
| 16S_ribosomal_RNA              | DNA     | 16S ribosomal RNA (Bacteria and Archaea type strains)                                    |
| 18S_fungal_sequences           | DNA     | 18S ribosomal RNA sequences (SSU) from Fungi type and reference material                 |
| 28S_fungal_sequences           | DNA     | 28S ribosomal RNA sequences (LSU) from Fungi type and reference material                 |
| Betacoronavirus                | DNA     | Betacoronavirus                                                                          |
| GCF_000001405.38_top_level     | DNA     | Homo sapiens GRCh38.p12 [GCF_000001405.38] chromosomes plus unplaced and unlocalized scaffolds |
| GCF_000001635.26_top_level     | DNA     | Mus musculus GRCm38.p6 [GCF_000001635.26] chromosomes plus unplaced and unlocalized scaffolds |
| ITS_RefSeq_Fungi               | DNA     | Internal transcribed spacer region (ITS) from Fungi type and reference material          |
| ITS_eukaryote_sequences        | DNA     | ITS eukaryote BLAST                                                                       |
| LSU_eukaryote_rRNA             | DNA     | Large subunit ribosomal nucleic acid for Eukaryotes                                      |
| LSU_prokaryote_rRNA            | DNA     | Large subunit ribosomal nucleic acid for Prokaryotes                                     |
| SSU_eukaryote_rRNA             | DNA     | Small subunit ribosomal nucleic acid for Eukaryotes                                      |
| env_nt                         | DNA     | Environmental samples                                                                   |
| nt                             | DNA     | Nucleotide collection (nt)                                                               |
| patnt                          | DNA     | Nucleotide sequences derived from the Patent division of GenBank                         |
| pdbnt                          | DNA     | PDB nucleotide database                                                                  |
| ref_euk_rep_genomes            | DNA     | RefSeq Eukaryotic Representative Genome Database                                         |
| ref_prok_rep_genomes           | DNA     | Refseq prokaryote representative genomes (contains refseq assembly)                      |
| ref_viroids_rep_genomes         | DNA     | Refseq viroids representative genomes                                                    |
| ref_viruses_rep_genomes         | DNA     | Refseq viruses representative genomes                                                    |
| refseq_rna                     | DNA     | NCBI Transcript Reference Sequences                                                       |
| refseq_select_rna              | DNA     | RefSeq Select RNA sequences                                                               |
| tsa_nt                         | DNA     | Transcriptome Shotgun Assembly (TSA) sequences                                           |
| env_nr                         | Protein | Proteins from WGS metagenomic projects                                                   |
| landmark                       | Protein | Landmark database for SmartBLAST                                                         |
| nr                             | Protein | All non-redundant GenBank CDS translations+PDB+SwissProt+PIR+PRF excluding environmental samples from WGS projects |
| pdbaa                          | Protein | PDB protein database                                                                      |
| pataa                          | Protein | Protein sequences derived from the Patent division of GenBank                            |
| refseq_protein                 | Protein | NCBI Protein Reference Sequences                                                          |
| refseq_select_prot              | Protein | RefSeq Select proteins                                                                   |
| swissprot                      | Protein | Non-redundant UniProtKB/SwissProt sequences                                              |
| tsa_nr                         | Protein | Transcriptome Shotgun Assembly (TSA) sequences                                           |
| cdd                            | Protein | Conserved Domain Database (CDD) is a collection of well-annotated multiple sequence alignment models represented as position-specific score matrices |
