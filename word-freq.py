import os;
from glob import glob

from nltk import word_tokenize
from nltk.probability import FreqDist

registers = {'HI': 'HI_how_to_instructional',
             'ID': 'ID_interactive_discussion',
             'IN': 'IN_informational_wikipedia',
             'IP': 'IP_informational_persuasion',
             'LY': 'LY_song_lyrics',
             'NA': 'NA_news_reports',
             'OP': 'OP_opinion_blogs',
             'SP': 'SP_interview_transcripts'}


freqdists = dict.fromkeys(registers.keys(), FreqDist()) #make corresponding FreqDists
for abbrev, item in freqdists.items():
    print(abbrev, item)

if not os.path.isdir("freq_dists"): #create the directory to store the word lists
    os.makedirs("freq_dists")

for abbrev, name in registers.items(): #for each register
    filename = name + ".freqdist" #make a .freqdist file
    if not os.path.isfile(filename):
        newFreqDict = open(os.path.join('./freq_dists', filename), "w+")

    for corpus in glob('./Mini-CORE/1+' + abbrev + '+*'):
        corpus_file = open(corpus, "r")
        corpus_text = corpus_file.read()
        freqdists[abbrev].update(word_tokenize(corpus_text))

    FreqDictFile = open(os.path.join('./freq_dists', filename), "w+")
    for word in freqdists[abbrev].keys():
        FreqDictFile.write(word + ", ")

print("Analysis finished.")
