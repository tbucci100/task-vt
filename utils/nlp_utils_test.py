import unittest
from utils import nlp_utils 


class TestSpacyDoc(unittest.TestCase):

    def test_example_spacy_doc_loader(self):
        text = ("When Sebastian Thrun started working on self-driving cars at "
                "Google in 2007, few people outside of the company took him "
                "seriously. “I can tell you very senior CEOs of major American "
                "car companies would shake my hand and turn away because I wasn’t "
                "worth talking to,” said Thrun, in an interview with Recode earlier "
                "this week.")
        doc = nlp_utils.example_spacy_doc_loader(text)
        for entity in doc.ents:
            print(entity.text, entity.label_)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
