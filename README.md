#Code of CRFTM
CRFTM is a topic model of short text that not only develops a generalized solution to alleviate the sparsity problem by aggregating short texts into pseudo-documents, but also leverages a Condition Random Field (CRF) regularized model that encourages correlated words to share the same topic assignment.

**Incorporating Word Embeddings into Topic Modeling of Short Texts.**
anonymous authors

## Description

This repository doesn't contain the preprocess steps. So if you want to use this code, you should prepare the data by yourself. 

Also this repository doesn't contain the metric code for classification and UCI score. 

The code includes a runnable example, you can directly run *src/models/GibbsSamplingCRFTM.java* with default parameter settings.

It trains CRFTM over the pseudo-documents in *psdsample.txt* and output the topics. The *psdsample.txt* contains all the training pseudo-documents, where each line represents one pseudo-documents with words separated by space as:
> word1 word2 word3 ....

The *sample.txt* contains all the original short texts and *corrlations.txt* consists of all the semantic correlations in each pseudo-document.

(*Note: the sample data is only used for illustration of the usage of the code. It is not the dataset used in the paper.*)

## Parameter Explanation

`alpha`: Specify the hyper-parameter alpha. The default value is 50/numTopic.

`beta`: Specify the hyper-parameter beta. The default value is 0.01.

`num_iter`: Specify the number of iteration for gibbs sampling progress. The default value is 1,000.

`k`: Specify the number of topics. The default value is 40.

`topic_words`: Specify the number of the most probable topical words. The default value is 20.

`corpus_path`: Specify the path to the input corpus file.

`correlation_path`: Specify the path to the input correlation file.

## Model Result Explanation

`*.paras`: This file contains some parameters of CRFTM model.

`*.theta`: This file contains the topic-document distributions, each line is a document and each column is a topic.

`*.phi`: This file contains the word-topic distributions, each column is a word in the vocabulary.

`*.topicAssignments`: This file contains the topic assignments for words in training data. 

`*.vocabulary`：This file contains the maps between words and word's IDs (integer). 

`*.topWords`: This file contains `topic_words` most likely words of each topic. This is used for UCI Coherence task.

`*.pzd`: This file contains the topic-level representation for each short texts generated by *generate_pzd.py*. Each line is a topic distribution for one short text. This is used for classification task.
