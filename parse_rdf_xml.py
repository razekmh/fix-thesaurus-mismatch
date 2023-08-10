from rdflib import Graph

g = Graph()
g.parse("candidate.xml", format="xml")

for s, p, o in g:
    print(s, p, o)
    # print available methods
    print("subject methods: "+ str(dir(s)))
    #print("predicate methods: "+ str(dir(p)))
    #print("object methods: "+ str(dir(o)))
    break

