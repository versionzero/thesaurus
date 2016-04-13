import sys
import json

# http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return izip(*[iter(iterable)]*n)


def main():
    
    if not len(sys.argv) > 1:
        print "Please supply a filename."
        sys.exit()

    filename = sys.argv[1]
    print "Parsing: %s" % filename

    with open(filename) as f:
        data = f.read().splitlines()
        data = data[1:]  # chop off format specifier

    # Convert data of the type:
    #    
    # fawn|5
    # (noun)|dun|grayish brown|greyish brown|light brown
    # (noun)|deer|cervid
    # (verb)|crawl|creep|cringe|cower|grovel|bend|flex
    # (verb)|toady|truckle|bootlick|kowtow|kotow|suck up|flatter|blandish
    # (verb)|litter
    #
    # to:
    #
    # "fawn": [
    #   {"list": ["dun", "grayish brown", "greyish brown", "light brown"],
    #    "type": "(noun)" },
    #   ...
    # ]    
    i = 0
    thesaurus = {}
    while i != len(data):
        word, count = tuple(data[i].split('|'))
        count = int(count)
        words = [data[i+j+1].split('|') for j in range(count)]
        synonyms = [{'type': w[0], 'list': w[1:]} for w in words]
        thesaurus[word] = synonyms
        i += count + 1

    print json.dumps(thesaurus, indent=4)    

if __name__ == "__main__":
    main()
