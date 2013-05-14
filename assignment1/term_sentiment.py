import sys
import json
import re


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    terms = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


    for line in tweet_file:
        tdict= json.loads(line)
        if "text" not in tdict.keys():
            continue
        p = 0
        for word in tdict["text"].split():
            if word in scores:
                p = p + scores[word]
        if p <> 0:
            for word in tdict["text"].split():

                pattern=re.compile("[^\w']|_|-|'")

                word = pattern.sub('',word)
                word = word.strip()

                if word not in scores and len(word)>0:
                    if word in terms:
                        if p > 0 :
                            terms[word] = terms[word] + 1
                        else:
                            terms[word] = terms[word] - 1
                    else:
                        if p > 0 :
                            terms[word] = 1
                        else:
                            terms[word] = 1


    for k in terms:
        print k,float(terms[k])




if __name__ == '__main__':
    main()





