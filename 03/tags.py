from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    try:
        with open(RSS_FEED,'r') as f:
            s=f.read()
            tags=TAG_HTML.findall(s)
            return tags
    except:
        print("Cannot open file {}.".format(RSS_FEED))

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    # Put the tags list in Counter object
    c=Counter(tags)
    # Get the 10 most common tags
    com_tags=c.most_common(TOP_NUMBER)
    return com_tags



def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    prod=product(tags,repeat=2)
    similar=[]
    for t in prod:
        if t[0][0] == t[1][0]:
            s=SequenceMatcher(None,t[0],t[1])
            if s.quick_ratio()>SIMILAR:
                    similar.append(t)
    return similar



if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
