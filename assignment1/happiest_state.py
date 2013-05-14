import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    states = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


    for line in tweet_file:
        tdict= json.loads(line)
        if "text" not in tdict.keys():
            continue
        p = 0
        for word in tdict["text"].split():
            if word.lower() in scores:
                p = p + scores[word.lower()]
            if "place" in tdict.keys():
                if tdict["place"] != None:
                    if tdict["place"]["country_code"] == 'US':
                        st = ''.join(tdict["place"]["full_name"].split(',')[1:2]).strip()
                        if st in states:
                            states[st]=states[st]+p
                        else:
                            states[st]=p

    print max(states, key=states.get)




if __name__ == '__main__':
    main()


