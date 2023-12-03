## Authorship

Jane Austen was an early 19th-century author famous for her English romance novels. Mary Wollstonecraft Shelley was an early 19th-century author famous for her SF novels, especially Frankenstein. Their writing styles are quite distinct.

I have obtained the public-domain text of four novels from [Project Gutenberg](https://gutenberg.org/)

* Mary Wollstonecraft Shelley: Frankenstein, The First Man
* Jane Austen: Pride and Prejudice, Northanger Abbey  

I cleaned up these novels by purging them of header and footer material, proper names, and other irrelevant information. I also cleaned up some formatting irregularities.

The cleaned up files are available as

* `austen-northanger-abbey.txt`
* `austen-pride-and-prejudice.txt`
* `shelley-frankenstein.txt`
* `shelley-the-last-man.txt`  

at our Github repo http://github.com/pdx-cs-ai/miniproject-data-fall2023Links to an external site..

Construct a machine learner that can classify paragraphs as Austen vs Shelley. Achieve at least 70% accuracy against a an independent validation set you construct from the text, or as a mean in 10-way cross-validation.

Hints:

The "normal" way to go about this would be the "big bag of words" approach: treat each paragraph as an unordered collection of words. You can binarize by having the absence or presence of a word as a feature, or you can count instances.

You will need to use feature selection to find words that are good at distinguishing Austen paragraphs from Shelley paragraphs. You will probably want not to use features that are good at distinguishing the two novels by the same author, as these are book-specific features.

Decision tree (ID3) works well here.