'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''

def dfs(adj,o): 
    return dfs_aux(adj,o,set(),{})
 
def dfs_aux(adj,o,vis,pai): 
    vis.add(o) 
    for d in adj[o]:
        if d not in vis: 
            pai[d] = o 
            dfs_aux(adj,d,vis,pai) 
    return vis

def maior(vizinhos):
    adj = {}
    for conj in vizinhos:
        for pais1 in conj:
            if pais1 not in adj:
                adj[pais1] = []
            for pais2 in conj:
                if pais1 != pais2:
                    adj[pais1].append(pais2)
    
    max = 0
    for o in adj:
        vis = dfs(adj,o)
        if len(vis) > max:
            max = len(vis)
    return max
