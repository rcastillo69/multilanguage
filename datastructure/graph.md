## Graph

**Definition:**
A collection of nodes or values called vertices that might be related; relations between vertices are called edges.

[defintion](../assets/graph_definition.webp)

Many things in life can be represented by graphs; for example, a social network can be represented by a graph whose vertices are users and whose edges are friendships between the users. Similarly, a city map can be represented by a graph whose vertices are locations in the city and whose edges are roads between the locations.

**Graph Cycle:**
Simply put, a cycle occurs in a graph when three or more vertices in the graph are connected so as to form a closed loop.

**Acyclic Graph:**
A graph that has no cycles.

**Cyclic Graph:**
A graph that has at least one cycle.

**Directed Graph:**
A graph whose edges are directed, meaning that they can only be traversed in one direction, which is specified.

**Undirected Graph:**
A graph whose edges are undirected, meaning that they can be traversed in both directions.

**Connected Graph:**
A graph is connected if for every pair of vertices in the graph, there's a path of one or more edges connecting the given vertices.

In the case of a directed graph, the graph is:
- **Strongly connected:** if there are bidirectional connections between the vertices of every pair of vertices (i.e., for every vertex-pair (u, v) you can reach v from u and u from v).
- **Weakly connected:** if there are connections (but not necessarily bidirectional ones) between the vertices of every pair of vertices.

A graph that isn't connected is said to be disconnected.

**Common Operations and Complexity Analysis:**

- **Add a vertex:** O(1)
- **Add an edge:** O(1) for adjacency list, O(V) for adjacency matrix
- **Remove a vertex:** O(V + E) for adjacency list, O(V^2) for adjacency matrix
- **Remove an edge:** O(E) for adjacency list, O(1) for adjacency matrix
- **Search (DFS/BFS):** O(V + E)

**Use Cases:**

- **Social Networks:** Representing relationships between users.
- **Web Crawlers:** Representing links between web pages.
- **Maps and Navigation Systems:** Representing locations and routes.
- **Network Routing:** Representing network nodes and connections.
- **Dependency Management:** Representing tasks and their dependencies in project management.

## Types

[types](../assets/types_graph.png)




## Examples

Here are examples of how to create, add, update, and delete items in a graph for various programming languages:

### Python

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)

    def update_vertex(self, old_vertex, new_vertex):
        if old_vertex in self.graph:
            self.graph[new_vertex] = self.graph.pop(old_vertex)
            for vertices in self.graph.values():
                for i in range(len(vertices)):
                    if vertices[i] == old_vertex:
                        vertices[i] = new_vertex

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
            for vertices in self.graph.values():
                if vertex in vertices:
                    vertices.remove(vertex)

# Example usage
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_edge('A', 'B')
graph.update_vertex('A', 'C')
graph.delete_vertex('B')
print(graph.graph)
```

### TypeScript

```typescript
class Graph {
    private graph: { [key: string]: string[] } = {};

    addVertex(vertex: string): void {
        if (!this.graph[vertex]) {
            this.graph[vertex] = [];
        }
    }

    addEdge(vertex1: string, vertex2: string): void {
        if (this.graph[vertex1] && this.graph[vertex2]) {
            this.graph[vertex1].push(vertex2);
        }
    }

    updateVertex(oldVertex: string, newVertex: string): void {
        if (this.graph[oldVertex]) {
            this.graph[newVertex] = this.graph[oldVertex];
            delete this.graph[oldVertex];
            for (let vertex in this.graph) {
                const edges = this.graph[vertex];
                for (let i = 0; i < edges.length; i++) {
                    if (edges[i] === oldVertex) {
                        edges[i] = newVertex;
                    }
                }
            }
        }
    }

    deleteVertex(vertex: string): void {
        if (this.graph[vertex]) {
            delete this.graph[vertex];
            for (let vert in this.graph) {
                const edges = this.graph[vert];
                const index = edges.indexOf(vertex);
                if (index !== -1) {
                    edges.splice(index, 1);
                }
            }
        }
    }
}

// Example usage
const graph = new Graph();
graph.addVertex('A');
graph.addVertex('B');
graph.addEdge('A', 'B');
graph.updateVertex('A', 'C');
graph.deleteVertex('B');
console.log(graph);
```

### Golang

```go
package main

import "fmt"

type Graph struct {
    graph map[string][]string
}

func NewGraph() *Graph {
    return &Graph{graph: make(map[string][]string)}
}

func (g *Graph) AddVertex(vertex string) {
    if _, exists := g.graph[vertex]; !exists {
        g.graph[vertex] = []string{}
    }
}

func (g *Graph) AddEdge(vertex1, vertex2 string) {
    if _, exists1 := g.graph[vertex1]; exists1 {
        if _, exists2 := g.graph[vertex2]; exists2 {
            g.graph[vertex1] = append(g.graph[vertex1], vertex2)
        }
    }
}

func (g *Graph) UpdateVertex(oldVertex, newVertex string) {
    if edges, exists := g.graph[oldVertex]; exists {
        g.graph[newVertex] = edges
        delete(g.graph, oldVertex)
        for vertex, edgeList := range g.graph {
            for i, edge := range edgeList {
                if edge == oldVertex {
                    g.graph[vertex][i] = newVertex
                }
            }
        }
    }
}

func (g *Graph) DeleteVertex(vertex string) {
    delete(g.graph, vertex)
    for v, edgeList := range g.graph {
        for i, edge := range edgeList {
            if edge == vertex {
                g.graph[v] = append(g.graph[v][:i], g.graph[v][i+1:]...)
                break
            }
        }
    }
}



```go
// Example usage
func main() {
    graph := NewGraph()
    graph.AddVertex("A")
    graph.AddVertex("B")
    graph.AddEdge("A", "B")
    graph.UpdateVertex("A", "C")
    graph.DeleteVertex("B")
    fmt.Println(graph.graph)
}
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

class Graph {
public:
    void addVertex(const std::string& vertex) {
        if (graph.find(vertex) == graph.end()) {
            graph[vertex] = {};
        }
    }

    void addEdge(const std::string& vertex1, const std::string& vertex2) {
        if (graph.find(vertex1) != graph.end() && graph.find(vertex2) != graph.end()) {
            graph[vertex1].push_back(vertex2);
        }
    }

    void updateVertex(const std::string& oldVertex, const std::string& newVertex) {
        if (graph.find(oldVertex) != graph.end()) {
            graph[newVertex] = graph[oldVertex];
            graph.erase(oldVertex);
            for (auto& [vertex, edges] : graph) {
                std::replace(edges.begin(), edges.end(), oldVertex, newVertex);
            }
        }
    }

    void deleteVertex(const std::string& vertex) {
        graph.erase(vertex);
        for (auto& [v, edges] : graph) {
            edges.erase(std::remove(edges.begin(), edges.end(), vertex), edges.end());
        }
    }

    void printGraph() {
        for (const auto& [vertex, edges] : graph) {
            std::cout << vertex << ": ";
            for (const auto& edge : edges) {
                std::cout << edge << " ";
            }
            std::cout << std::endl;
        }
    }

private:
    std::unordered_map<std::string, std::vector<std::string>> graph;
};

// Example usage
int main() {
    Graph graph;
    graph.addVertex("A");
    graph.addVertex("B");
    graph.addEdge("A", "B");
    graph.updateVertex("A", "C");
    graph.deleteVertex("B");
    graph.printGraph();
    return 0;
}
```

### Rust

```rust
use std::collections::HashMap;

struct Graph {
    graph: HashMap<String, Vec<String>>,
}

impl Graph {
    fn new() -> Self {
        Graph {
            graph: HashMap::new(),
        }
    }

    fn add_vertex(&mut self, vertex: String) {
        self.graph.entry(vertex).or_insert(Vec::new());
    }

    fn add_edge(&mut self, vertex1: String, vertex2: String) {
        if self.graph.contains_key(&vertex1) && self.graph.contains_key(&vertex2) {
            if let Some(edges) = self.graph.get_mut(&vertex1) {
                edges.push(vertex2);
            }
        }
    }

    fn update_vertex(&mut self, old_vertex: String, new_vertex: String) {
        if let Some(edges) = self.graph.remove(&old_vertex) {
            self.graph.insert(new_vertex.clone(), edges);
            for (_vertex, edges) in self.graph.iter_mut() {
                for edge in edges.iter_mut() {
                    if *edge == old_vertex {
                        *edge = new_vertex.clone();
                    }
                }
            }
        }
    }

    fn delete_vertex(&mut self, vertex: String) {
        self.graph.remove(&vertex);
        for (_vertex, edges) in self.graph.iter_mut() {
            edges.retain(|edge| edge != &vertex);
        }
    }
}

// Example usage
fn main() {
    let mut graph = Graph::new();
    graph.add_vertex("A".to_string());
    graph.add_vertex("B".to_string());
    graph.add_edge("A".to_string(), "B".to_string());
    graph.update_vertex("A".to_string(), "C".to_string());
    graph.delete_vertex("B".to_string());

    for (vertex, edges) in &graph.graph {
        println!("{}: {:?}", vertex, edges);
    }
}
```

### Java

```java
import java.util.HashMap;
import java.util.ArrayList;

public class Graph {
    private HashMap<String, ArrayList<String>> graph = new HashMap<>();

    public void addVertex(String vertex) {
        graph.putIfAbsent(vertex, new ArrayList<>());
    }

    public void addEdge(String vertex1, String vertex2) {
        if (graph.containsKey(vertex1) && graph.containsKey(vertex2)) {
            graph.get(vertex1).add(vertex2);
        }
    }

    public void updateVertex(String oldVertex, String newVertex) {
        if (graph.containsKey(oldVertex)) {
            graph.put(newVertex, graph.remove(oldVertex));
            for (ArrayList<String> edges : graph.values()) {
                for (int i = 0; i < edges.size(); i++) {
                    if (edges.get(i).equals(oldVertex)) {
                        edges.set(i, newVertex);
                    }
                }
            }
        }
    }

    public void deleteVertex(String vertex) {
        graph.remove(vertex);
        for (ArrayList<String> edges : graph.values()) {
            edges.remove(vertex);
        }
    }

    public void printGraph() {
        for (String vertex : graph.keySet()) {
            System.out.println(vertex + ": " + graph.get(vertex));
        }
    }

    // Example usage
    public static void main(String[] args) {
        Graph graph = new Graph();
        graph.addVertex("A");
        graph.addVertex("B");
        graph.addEdge("A", "B");
        graph.updateVertex("A", "C");
        graph.deleteVertex("B");
        graph.printGraph();
    }
}
```

### Kotlin

```kotlin
class Graph {
    private val graph = mutableMapOf<String, MutableList<String>>()

    fun addVertex(vertex: String) {
        graph.putIfAbsent(vertex, mutableListOf())
    }

    fun addEdge(vertex1: String, vertex2: String) {
        if (graph.containsKey(vertex1) && graph.containsKey(vertex2)) {
            graph[vertex1]?.add(vertex2)
        }
    }

    fun updateVertex(oldVertex: String, newVertex: String) {
        if (graph.containsKey(oldVertex)) {
            graph[newVertex] = graph.remove(oldVertex) ?: mutableListOf()
            for (edges in graph.values) {
                edges.replaceAll { if (it == oldVertex) newVertex else it }
            }
        }
    }

    fun deleteVertex(vertex: String) {
        graph.remove(vertex)
        for (edges in graph.values) {
            edges.remove(vertex)
        }
    }

    fun printGraph() {
        for ((vertex, edges) in graph) {
            println("$vertex: $edges")
        }
    }
}

// Example usage
fun main() {
    val graph = Graph()
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addEdge("A", "B")
    graph.updateVertex("A", "C")
    graph.deleteVertex("B")
    graph.printGraph()
}
```


