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
        this.shortestPathToT = 0;
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
    /* Set up a queue for the modified BFS */
    let queue = []
    /* push the 'start' vertex into the queue */
    queue.push(graph[nodes[start]]);
    /* mark 'start' as having been visited */
    queue[0].visited = true;
    /* mark that the shortest path to itself is
    '0' */
    queue[0].shortestPathToT = 0;
    /* mark that there is currently only 1 defined path to itself */
    queue[0].numShortestPaths = 1;
    /* while the queue isn't empty */
    while (queue.length > 0) {
        /* the current vertex is the first in the queue */
        let curNode = queue[0];
        /* for each edge in the graph */
        curNode.edges.forEach((element) => {
            /* let n be the vertex in the graph where the 
            chosen vertex is */
            let n = graph[nodes[element]];
            /* if the vertex has already been visited */
            if (n.visited) {
                /* if the next node from 'curNode' has a shortest path that's only one node longer than the one at 
                'curNode', that means that there is another path of the same length that passes here. Basically the 
                'n' vertex is a merging point of two paths of the same length */
                if (n.shortestPathToT == curNode.shortestPathToT + 1) {
                    /* the shortest path to 'n' is then increased by all shortest paths that passed through the 
                    past 'curNode' as a way of 'merging' the paths */
                    n.numShortestPaths += curNode.numShortestPaths;
                }
                else if (n.shortestPathToT > curNode.shortestPathToT) {
                    /* if the shortest path to 't' of the next vertex  in the adjacency list is larger than one greater 
                    than that at 'curNode', we essentially override the previous shortest path with the new smaller 
                    one from 'curNode' and adding one to it. The paths from curNode also become the shortest paths for 
                    'n' */
                    n.shortestPathToT = curNode.shortestPathToT + 1;
                    n.numShortestPaths = curNode.numShortestPaths;
                }
            }
            /* if the vertex has not been visited yet */
            else {
                /* say it's been visited */
                n.visited = true;
                /* the shortest path to 't' from the current node has increased by one at this node as we have moved
                one vertex further from 't' */
                n.shortestPathToT = curNode.shortestPathToT + 1;
                /* the number of shortest paths here then equals the number of shortest paths from the previous vertex */
                n.numShortestPaths = curNode.numShortestPaths;
                /* push this node onto the queue */
                queue.push(n);
            }
        })
        /* remove 'curNode' from the queue as it has been 'colored red' by visiting all vertices in it's adjacency list */
        queue.splice(0, 1);
    }
    /* the ending vertex will contain the number of the shortest paths found by this algorithm */
    return graph[nodes[end]].numShortestPaths;
}
