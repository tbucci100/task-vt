# Introduction

This implementation attempts to detect negation in medical statements with a drug and treatment term co-occurance. 
Each notebook implements a different method and the pros and cons are discussed in the corrresponding notebook. The results are compared in the evaluation notebook.
The stanfordCoreNLP server is used to tokenize and parse the text. A list of trigger terms that imply negation (https://github.com/ckbjimmy/clneg) is used as reference in some notebooks.

# Structure

1. The 'data' folder contains:
- Input files containing text to be analysed for negation
- neg_list_complete.txt : A list of terms that imply negation, as per https://github.com/ckbjimmy/clneg
- output\ : Folder with output files containing an addiitonal column that specifies if the text is a negation.
- Human annotated input for evaluation
- Consolidated results across models
2. The 'notebooks' folder contains:
- a notebook for each implementation method
- a notebook for establishing connection to StandFordCoreNLP
- a notebook for evaluating results
3. helper_funcstions.py contains helper functions used across notebooks

# Setup

1. Execute the following command line instructions under the data\ folder:

	wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip; \
	unzip stanford-corenlp-full-2018-02-27.zip; \
	rm stanford-corenlp-full-2018-02-27.zip; \
	wget https://nlp.stanford.edu/software/stanford-tregex-2018-02-27.zip; \
	unzip stanford-tregex-2018-02-27.zip; \
	rm stanford-tregex-2018-02-27.zip; \

# Citations

1.@article{weng2020clinical,
  title={Clinical Text Summarization with Syntax-Based Negation and Semantic Concept Identification},
  author={Weng, Wei-Hung and Chung, Yu-An and Schrasing Tong},
  journal={arXiv preprint arXiv:2003.00353},
  year={2020}
}

2.Manning, Christopher D., Mihai Surdeanu, John Bauer, Jenny Finkel, Steven J. Bethard, and David McClosky. 2014. 
   The Stanford CoreNLP Natural Language Processing Toolkit In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 55-60. [pdf] [bib]

3.@inproceedings{Neumann2019ScispaCyFA,
  title={ScispaCy: Fast and Robust Models for Biomedical Natural Language Processing},
  author={Mark Neumann and Daniel King and Iz Beltagy and Waleed Ammar},
  year={2019},
  Eprint={arXiv:1902.07669}
}