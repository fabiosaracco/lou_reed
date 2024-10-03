import os
import numpy as np
import random
import datetime as dt
from tqdm import trange, tqdm
import igraph


def lou_reed(g, reshuffles, verbose=True):
    n=g.vcount()
    nodelist=list(range(n))
    Loug=g.community_multilevel(return_levels=False)
    edgelist=[g.es[i].tuple for i in range(len(g.es))]
    # Loug is a membership list, i.e. for every element the community it belongs to.
    mod=g.modularity(Loug)
    membership=Loug.membership
    print(_update()+'\tModularity of the original order=%.5f' %(mod))
    for ii in trange(reshuffles):
        #rifrullo=random.sample(list(range(len(nodelist))),len(nodelist))
        rifrullo=list(range(len(nodelist)))
        random.shuffle(rifrullo)
        newedges=[]
        for i in range(len(edgelist)):
            newedges.append((rifrullo[edgelist[i][0]],rifrullo[edgelist[i][1]]))
        gaux=igraph.Graph()
        gaux.add_vertices(nodelist)
        gaux.add_edges(newedges)
        Lougaux=gaux.community_multilevel(return_levels=False)
        if mod<gaux.modularity(Lougaux):
            mod=gaux.modularity(Lougaux)
            membaux=Lougaux.membership
            for i in range(len(membaux)):
                membership[i]=membaux[rifrullo[i]]
            Loug=igraph.VertexClustering(g,membership)
            if verbose:
                tqdm.write(_update()+'\tstep: {0:d}, ({1:.2f}%): Modularity={2:.5f}'.format(ii, 100*(ii+1)/reshuffles, g.modularity(Loug)))
    if not verbose:
        print(_update()+'\tFinal modularity=%.5f' %(mod))
    return Loug

def _update():
    return '[lou_reed: {:%H:%M:%S}]'.format(dt.datetime.now())



