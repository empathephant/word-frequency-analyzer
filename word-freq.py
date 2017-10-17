import os;
from glob import glob
    
from nltk import word_tokenize
from nltk.probability import FreqDist

registers = {'HI': "HI_how_to_instructional",
             'ID': "ID_interactive_discussion",
             'IN': "IN_informational_wikipedia",
             'IP': "IP_informational_persuasion",
             'LY': "LY_song_lyrics",
             'NA': "NA_news_reports",
             'OP': "OP_opinion_blogs",
             'SP': "SP_interview_transcripts"}

if not os.path.isdir("freq_lists"):
    os.makedirs("freq_lists")

for abbrev, name in registers:
    filename = name + ".freqdist"
    if not os.path.isfile(filename):
        newFreqDict = open(os.path.join('./freq_lists', filename), "w+")

    for corpus in glob('./Mini-CORE/1+' + abbrev + '+*'):
        corpus_text = corpus.read()
        fd = FreqDist(word_tokenize(corpus_text))

        FreqDictFile = open(os.path.join('./freq_lists', filename), "w+")
        FreqDictFile.write(fd)
