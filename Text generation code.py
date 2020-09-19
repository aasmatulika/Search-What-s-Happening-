
# coding: utf-8

import spacy
import random
import tracery
from tracery.modifiers import base_english

nlp = spacy.load('en_core_web_sm')

text = open("tweet-corpus.txt").read() #replace 'tweet-corpus.txt' with the filename of the extracted tweets

doc = nlp(text)


sentences = list(doc.sents)
words = [w for w in list(doc) if w.is_alpha]
noun_chunks = list(doc.noun_chunks)
entities = list(doc.ents)


for item in random.sample(sentences, 10):
    print(">", item.text.strip().replace("\n", " "))


nouns = [w for w in words if w.pos_ == "NOUN"]
verbs = [w for w in words if w.pos_ == "VERB"]
adjs = [w for w in words if w.pos_ == "ADJ"]
advs = [w for w in words if w.pos_ == "ADV"]
past_tense_verbs = [w for w in words if w.tag_ == 'VBD']
prep_phrases = [w for word in doc if word.dep_ == 'prep']


people = [e for e in entities if e.label_ == "PERSON"]
locations = [e for e in entities if e.label_ == "LOC"]
times = [e for e in entities if e.label_ == "DATE"]
apparatus = [e for e in entities if e.label_ == "ORG"]
place = [e for e in entities if e.label_ == "GPE"]



subjects = [chunk for chunk in noun_chunks if chunk.root.dep_ == 'nsubj']
objects = [chunk for chunk in noun_chunks if chunk.root.dep_ == 'dobj']



# for item in random.sample(people, 30): # change "times" to "people" or "locations" to sample those lists
#     print(item.text.strip())



# The following rules are just an example template.
# The structure can be changed to suit the kind of sentence structure you want to generate.

rules = {
    "subject": [w.text for w in subjects],
    "object": [w.text for w in objects],
    "verb": [w.text for w in past_tense_verbs],
    "adverb": [w.text for w in advs],
    "adj": [w.text for w in adjs],
    "people": [w.text for w in people],
    "loc": [w.text for w in locations],
    "time": [w.text for w in times],

    "origin": "#scene#\n\n[charA:#subject#][charB:#subject#][prop:#object#]#sentences#",
    "scene": "SCENE: #time.lowercase#",
    "sentences": [
        "#sentence#\n#sentence#",
        "#sentence#\n#sentence#\n#sentence#",
        "#sentence#\n#sentence#\n#sentence#\n#sentence#"
        "#sentence#\n#sentence#\n#sentence#\n#sentence#"
    ],

    "sentence": [
        "#charA.capitalize# #verb# #prop#.",
        "#charB.capitalize# #verb# #prop#.",
        "#prop.capitalize# became #adj#.",
        "#charA.capitalize# and #charB# greeted each other.",
        "'Did you hear about #object.lowercase#?' said #charA#.",
        "'#subject.capitalize# is #adj#,' said #charB#.",
        "#charA.capitalize# and #charB# #verb# #object#.",
        "#charA.capitalize# and #charB# looked at each other.",
        "#sentence#\n#sentence#"
    ]
}
grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)



for i in range(3):
    print(grammar.flatten("#origin#"))
    print()
