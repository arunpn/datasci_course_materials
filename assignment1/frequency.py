import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary



    for line in tweet_file:
        tdict= json.loads(line)
        if "text" not in tdict.keys():
            continue
        p = 0
        for word in tdict["text"].split():
            if word in scores:
                scores[word] = scores[word] + 1
            else:
                scores[word] = 1
    for keys in scores:
        print keys,(scores[keys]/float(len(scores)))


if __name__ == '__main__':
    main()



