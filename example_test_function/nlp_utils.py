import spacy


def example_spacy_doc_loader(in_text):
    """
    A simple function for loading text into a SpaCy doc. Its purpose is to illustrate how NLP utils and tests would work

    :param in_text: text to be loaded into a SpaCy doc
    :return: SpaCy doc object
    """

    # NOTE: the following code is from the spacy.io homepage

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_sm")

    # Process whole documents
    text = in_text
    doc = nlp(text)

    return doc
