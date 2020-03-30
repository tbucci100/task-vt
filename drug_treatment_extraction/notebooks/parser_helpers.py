import numpy as np
import pylab
import pandas as pd
import json
import os
import scispacy
import spacy


Paths=["./CORD-19-research-challenge/noncomm_use_subset/noncomm_use_subset/","./CORD-19-research-challenge/comm_use_subset/comm_use_subset/","./CORD-19-research-challenge/biorxiv_medrxiv/biorxiv_medrxiv/","./CORD-19-research-challenge/custom_license/custom_license/"]


# These functions determine what blocks are pulled from the paper for matching
def TitleBlocks(paper):
    return([{'text':paper['metadata']['title']}])

def AbstractBlocks(paper):
    return(paper['abstract'])

def BodyBlocks(paper):
    return(paper['body_text'])



# This function finds matching lemmas and notes positions of
# occurence in the relevant json block. This function uses
# the lemmatized text.
def PullMentionsLemmatized(Paths, BlockSelector,SecName, Words):
    nlp=spacy.load("en_core_sci_lg")
    Positions=[]
    FoundWords=[]
    Section=[]
    BlockID=[]
    BlockText=[]
    PaperID=[]
    
    tokenized_words=[]
    for w in Words:
        tokenized_words.append(nlp(w.lower())[0].lemma_)
    for Path in Paths:
        print(Path)

        Files=os.listdir(Path)
        for p in Files:

            readfile=open(Path+p,'r')
            paper=json.load(readfile)
            Blocks=BlockSelector(paper)

            for b in range(0,len(Blocks)):
                text=nlp(Blocks[b]['text'].lower())

                for t in text:
                    for w in tokenized_words:
                        if(w == t.lemma_):
                            Section.append(SecName)
                            FoundWords.append(w)
                            Positions.append(t.idx)
                            BlockText.append(Blocks[b]['text'])
                            BlockID.append(b)
                            PaperID.append(p[:-5])
    return {'sha':PaperID,'blockid':BlockID,'word':FoundWords,'sec':Section,'pos':Positions,'block':BlockText}


# This function finds matching words and notes positions of
# occurence in the relevant json block. This function uses
# direct text matching (not lemmatized)
def PullMentionsDirect(Paths, BlockSelector,SecName, Words):
    Positions=[]
    FoundWords=[]
    Section=[]
    BlockID=[]
    BlockText=[]
    PaperID=[]
    for wi in range(0,len(Words)):
        Words[wi]=Words[wi].lower()
    for Path in Paths:
        print(Path)

        Files=os.listdir(Path)
        for p in Files:

            readfile=open(Path+p,'r')
            paper=json.load(readfile)
            Blocks=BlockSelector(paper)

            for b in range(0,len(Blocks)):
                text=Blocks[b]['text'].lower()
                for w in Words:
                    if(w in text):
                        pos=text.find(w)
                   
                        #check we're not in the middle of another word
                        if(text[pos-1]==" " and ( (pos+len(w))>=len(text) or not text[pos+len(w)].isalpha())):
                            Section.append(SecName)
                            FoundWords.append(w)
                            Positions.append(text.find(w))
                            BlockText.append(Blocks[b]['text'])
                            BlockID.append(b)
                            PaperID.append(p[:-5])
    return {'sha':PaperID,'blockid':BlockID,'word':FoundWords,'sec':Section,'pos':Positions,'block':BlockText}


# Run to get treatment words
def ExtractToCSV(Words,Filename,Lemmatized=True, RunTitle=True, RunAbstract=True, RunBody=False):

    if(Lemmatized):
        PullMentions = PullMentionsLemmatized
    else:
        PullMentions = PullMentionsDirect
    
    DataDicts=[]
    if(RunTitle): 
        DataDicts.append(PullMentions(Paths, TitleBlocks,    "title",    Words))
    if(RunAbstract):
        DataDicts.append(PullMentions(Paths, AbstractBlocks, "abstract", Words))
    if(RunBody):
        DataDicts.append(PullMentions(Paths, BodyBlocks,     "body",     Words))

    SummedDictionary=DataDicts[0]
    for k in DataDicts[0].keys():
        for d in DataDicts:
            SummedDictionary[k]=SummedDictionary[k]+d[k]

    dat=pd.DataFrame(SummedDictionary)
    dat.to_csv(Filename)
