import hashlib

# -------------------- Dijkstra's Algorithm --------------------
class DijkstraGraph:
    def __init__(self):
        self.graph = {}  # adjacency list with weights

    def add_edge(self, u, v, w):
        # Add edges manually without append()
        if u not in self.graph:
            self.graph[u] = [v, w]
        else:
            self.graph[u] = self.graph[u] + [v, w]
        if v not in self.graph:
            self.graph[v] = [u, w]
        else:
            self.graph[v] = self.graph[v] + [u, w]

    def shortest_path(self, start):
        # Initialize distances
        dist = {}
        for node in self.graph:
            dist[node] = float('inf')
        dist[start] = 0

        visited = []

        while True:
            # Find unvisited node with smallest distance
            min_dist = float('inf')
            min_node = None
            for node in dist:
                if node not in visited and dist[node] < min_dist:
                    min_dist = dist[node]
                    min_node = node
            if min_node is None:
                break

            visited = visited + [min_node]  # manually add to visited

            neighbors = self.graph[min_node]
            i = 0
            while i < len(neighbors):
                neighbor = neighbors[i]
                weight = neighbors[i + 1]
                if neighbor not in visited and dist[min_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[min_node] + weight
                i += 2
        return dist


# -------------------- Bloom Filter --------------------
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size  # manual bit array

    def _hashes(self, item):
        result = []
        for i in range(self.hash_count):
            hash_obj = hashlib.md5((str(i) + item).encode())
            h = int(hash_obj.hexdigest(), 16)
            result = result + [h % self.size]  # manual append
        return result

    def add(self, item):
        hashes = self._hashes(item)
        for h in hashes:
            self.bit_array[h] = 1

    def query(self, item):
        hashes = self._hashes(item)
        for h in hashes:
            if self.bit_array[h] == 0:
                return False
        return True


# -------------------- MAIN PROGRAM --------------------
def main():
    print("Lab 10: Dijkstra’s Algorithm & Bloom Filter (User Input + Manual Implementation)")

    # ---- Create Dijkstra Graph ----
    dgraph = DijkstraGraph()
    n = int(input("\nEnter number of edges: "))
    i = 0
    while i < n:
        u = input("Enter source node: ").upper()
        v = input("Enter destination node: ").upper()
        w = int(input("Enter weight: "))
        dgraph.add_edge(u, v, w)
        i += 1

    start = input("\nEnter starting node for Dijkstra: ").upper()
    if start not in dgraph.graph:
        print("Invalid start node!")
    else:
        dist = dgraph.shortest_path(start)
        print("\nShortest Distances from", start)
        nodes = []
        for k in dist:
            nodes = nodes + [k]
        nodes.sort()
        for node in nodes:
            print(node, ":", dist[node])

    # ---- Bloom Filter ----
    bloom = BloomFilter(size=20, hash_count=3)
    count = int(input("\nEnter number of items to add to Bloom Filter: "))
    j = 0
    while j < count:
        item = input("Enter item: ").lower()
        bloom.add(item)
        print(f"'{item}' added.")
        j += 1

    # ---- Query Bloom Filter ----
    test = input("\nEnter item to check in Bloom Filter: ").lower()
    if bloom.query(test):
        print(f"'{test}' is probably in Bloom Filter.")
    else:
        print(f"'{test}' is definitely NOT in Bloom Filter.")


# -------------------- RUN --------------------
if __name__ == "__main__":
    main()
