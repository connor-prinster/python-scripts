const nodes = {
    's': 0,
    'a': 1,
    'c': 2,
    'b': 3,
    'e': 4,
    't': 5
}

class vertex {
    constructor(edges) {
        this.edges = edges;
        this.visited = false;
        this.shortestPathToS = 0;
        this.numShortestPaths = 0;
    }
}

function main() {
    let graph = [
        new vertex(['a', 'c']),
        new vertex(['s', 'b']),
        new vertex(['s', 'b', 'e']),
        new vertex(['a', 'c', 't']),
        new vertex(['c', 't']),
        new vertex(['b', 'e'])
    ]
    console.log(numShortestPaths('s', 't', graph));
}

function numShortestPaths(start, end, graph) {
    let queue = []
    queue.push(graph[nodes[start]]);
    queue[0].visited = true;
    queue[0].shortestPathToS = 0;
    queue[0].numShortestPaths = 1;
    while (queue.length > 0) {
        let curNode = queue[0];
        curNode.edges.forEach((element) => {
            let n = graph[nodes[element]];
            if (n.visited) {
                if (n.shortestPathToS == curNode.shortestPathToS + 1) {
                    n.numShortestPaths += curNode.numShortestPaths;
                }
                else if (n.shortestPathToS > curNode.shortestPathToS) {
                    n.shortestPathToS = curNode.shortestPathToS + 1;
                    n.numShortestPaths = curNode.numShortestPaths;
                }
            }
            else {
                n.visited = true;
                n.shortestPathToS = curNode.shortestPathToS + 1;
                n.numShortestPaths = curNode.numShortestPaths;
                queue.push(n);
            }
        })
        queue.splice(0, 1);
    }
    return graph[nodes[end]].numShortestPaths;
}
