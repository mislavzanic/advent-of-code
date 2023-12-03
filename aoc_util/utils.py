from collections import defaultdict
from typing import List, Any

def _search(Q: List[Any], end, neighbor_func, add_func):
    path = defaultdict(list)
    seen = set()
    while Q:
        curr = Q.pop()
        if curr == end: return path
        if curr in seen: continue
        neighbors = neighbor_func(curr)
        Q = add_func(Q, neighbors)
    return None
    

def dfs(Q: List[Any], end: Any, neighbor_func):
    return _search(Q, end, neighbor_func, lambda x, y: y + x)
    
def bfs(Q: List[Any], end: Any, neighbor_func):
    return _search(Q, end, neighbor_func, lambda x, y: x + y)
