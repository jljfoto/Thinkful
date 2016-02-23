import collections
ingredients = collections.defaultdict(int)

ingredients = {
    "butter"  : ("butter", 118.3),
    "sugar"   : ("sugar", 236.6),
    "vanilla" : ("vanilla", 4.929),
    "eggs"    : ("eggs", 2), # whole eggs
    "cocoa"   : ("cocoa", 118.3),
    "flour"   : ("flour", 118.3)
}

for k,v in ingredients.iteritems():
    print "k={0} v1={1} v2={2}".format(k,v[0],v[1])
