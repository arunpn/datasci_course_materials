import sys
import json
import operator


def main():
    tweet_file = open(sys.argv[1])
    top_htags = {} # initialize an empty dictionary

    for line in tweet_file:
        tdict= json.loads(line)
        if "entities" in tdict.keys():
            if "hashtags" in tdict["entities"].keys():
                for htag in tdict["entities"]["hashtags"]:
                    if htag["text"] in top_htags:
                        top_htags[htag["text"]] = top_htags[htag["text"]] + 1
                    else:
                        top_htags[htag["text"]] =1


    top_ten = sorted(top_htags.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
    for tags in top_ten:
        print tags[0],float(tags[1])

if __name__ == '__main__':
    main()


