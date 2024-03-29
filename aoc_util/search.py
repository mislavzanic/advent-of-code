from collections import defaultdict
import itertools
from typing import DefaultDict, List, Any, Union

def diff_loop():
    return itertools.product([-1,0,1],[-1,0,1])

def _search(Q: List[Any], terminate, neighbor_func, hash_func, search_type) -> Union[None, DefaultDict]:
    path = defaultdict(list)
    seen = set()
    while Q:
        curr = Q.pop(search_type)
        if terminate(curr): return path
        if hash_func is not None:
            if hash_func(curr) in seen: continue
            seen.add(hash_func(curr))
        neighbors = neighbor_func(curr)
        path[curr] += neighbors
        Q += neighbors
    return None
    

def dfs(Q: List[Any], terminate, neighbor_func, hash_func) -> Union[None, DefaultDict]:
    return _search(Q, terminate, neighbor_func, hash_func, -1)
    
def bfs(Q: List[Any], terminate, neighbor_func, hash_func) -> Union[None, DefaultDict]:
    return _search(Q, terminate, neighbor_func, hash_func, 0)
