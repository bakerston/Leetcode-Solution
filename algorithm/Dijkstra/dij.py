import sys
max = sys.maxunicode

vertices_number = 6
adj_matrix = [[0,1,10,-1,-1,2],[10,0,1,-1,-1,-1],[1,10,0,-1,-1,-1],[-1,-1,2,0,1,10],[-1,-1,-1,10,0,1],[-1,-1,-1,1,10,0]]
start = []
dest = ['2','5']
key = []

def init_keys(s:int):
    global key
    key = [max] * vertices_number
    key[s] = 0

def dijkstra(from_vertex, dest_vertex):
    fid=int(from_vertex)-1
    tid=int(dest_vertex)-1
    init_keys(fid)
    rel = [fid]
    min_vertex = fid
    hop_path = {}

    while len(rel) <= vertices_number and min_vertex != tid:
        for i in range(vertices_number):
            if i!=min_vertex and i not in rel and adj_matrix[min_vertex][i]>0 and key[i] > adj_matrix[min_vertex][i]:
                key[i] = key[min_vertex]+adj_matrix[min_vertex][i]
                hop_path.update({i+1: {"from": min_vertex+1,"cost":adj_matrix[min_vertex][i]}})
        if min_vertex not in rel:
            rel.append(min_vertex)
        min_vertex = tid
        for i in range(vertices_number):
            if i not in rel and key[i]<key[min_vertex]:
                min_vertex = i
    if len(hop_path) ==0 or int(dest_vertex) not in hop_path:
        return -1,-1
    else:
        next_hop = int(dest_vertex)
        path_str = dest_vertex
        while hop_path[next_hop]["from"] != int(from_vertex):
            cost= hop_path[next_hop]["cost"]
            next_hop = hop_path[next_hop]["from"]
            path_str = "{}-({})->{}".format(str(next_hop),cost,path_str)
        path_str = "{}-({})->{}".format(str(next_hop),hop_path[next_hop]["cost"],path_str)

        return key[tid], path_str


def find_shortest_router():
    for s in start:
        print("Forwarding Table for {}".format(s))
        print("{:>10} {:>10}       {}".format("To", "Cost", "Path"))
        for d in dest:
            c, n = dijkstra(s, d)
            print("{:>10} {:>10}       {}".format(d, c, n))

print(dijkstra(1,2))
