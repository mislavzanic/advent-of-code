from collections import defaultdict
from typing import DefaultDict, List, Any, Union

def _search(Q: List[Any], end, terminate, neighbor_func, hash_func, search_type) -> Union[None, DefaultDict]:
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
    

def dfs(Q: List[Any], end: Any, terminate, neighbor_func, hash_func) -> Union[None, DefaultDict]:
    return _search(Q, end, terminate, neighbor_func, hash_func, -1)
    
def bfs(Q: List[Any], end: Any, terminate, neighbor_func, hash_func) -> Union[None, DefaultDict]:
    return _search(Q, end, terminate, neighbor_func, hash_func, 0)
