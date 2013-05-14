import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    term = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


    for line in tweet_file:
        tdict= json.loads(line)
        if "text" not in tdict.keys():
            continue
            #    print tdict["text"]
        p = 0

        for word in tdict["text"].split():
            if word in scores:
                p = p + scores[word]
                #             print word,scores[word]
        print p

if __name__ == '__main__':
    main()


