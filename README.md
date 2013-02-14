# LINA-msc

LINA-msc is a dataset for evaluating Multi-sentence Compression in French. It is made of 40 sets of related sentences along with reference compressions composed by human assessors.

If you use this dataset, please cite :
* Florian Boudin and Emmanuel Morin, Keyphrase Extraction for N-best Reranking in Multi-Sentence Compression, Proceedings of the NAACL-HLT 2013 conference

The dataset is split into four directories :
* src : sentence clusters in raw and tokenized formats
* ref : manual compressions to be used for ROUGE/BLEU automatic evaluation
* pos : tokenized and Part-Of-Speech tagged sentences (using MElt 1.7 POs-tagger)
* xml : tokenized and Part-Of-Speech sentences in xml format

## Construction of the dataset

We collected news articles presented in clusters on the French edition of Google News over a period of three months. Clusters composed of at least 20 news articles and containing one single prevailing event were manually selected. To obtain the sets of related sentences, we extracted the first sentences from each article in the cluster, removing duplicates. Leading sentences in news articles are known to provide a good summary of the article content and are used as a baseline in summarization. The resulting dataset contains 618 sentences (33 tokens on average) spread over 40 clusters.

Three reference compressions were manually composed for each set of sentences. Human annotators, all native French speakers, were asked to carefully read the set of sentences, extract the most salient facts and generate a sentence (compression) that summarize the set of sentences. Annotators were also told to introduce as little new vocabulary as possible in their compressions. The purpose of this guideline is to reduce the number of possible mismatches, as existing evaluation metrics are based on n-gram comparison. Reference compressions have a compression rate of 60%.