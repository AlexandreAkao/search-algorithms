import search
from graph import Graph
from dfs import DFS
from bfs import BFS
from ucs import UCS
from gbfs import GBFS
from a_star import AStar

if __name__ == "__main__":
    # Setting graph we initiated to search class...
    graph = Graph()
    search.graph = graph

    # ====================================
    # ======= Busca em Profundidade ======
    # search.depth_first_search()
    # DFS(graph).solve()
    # ====================================
    
    # ====================================
    # ========= Busca em Largura =========
    # search.breath_first_search()
    # BFS(graph).solve()
    # ====================================

    # ====================================
    # ===== Busca de Custo Uniforme  =====
    # search.uniform_cost_search()
    # UCS(graph).solve()
    # ====================================
    
    # ====================================
    # = Busca Gulosa pela Melhor Escolha =
    # search.greedy_best_first_search()
    # GBFS(graph).solve()
    # ====================================

    # ====================================
    # ================ A* ================
    search.a_star_search()
    AStar(graph).solve()
    # ====================================
