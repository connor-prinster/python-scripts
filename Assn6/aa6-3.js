// const nodes = {
//     's': 0,
//     'a': 1,
//     'b': 2,
//     't': 3
// }

const nodes = {
    's': 0,
    'e': 1,
    'c': 2,
    'a': 3,
    'b': 4,
    'g': 5,
    't': 6
}

class vertex {
    constructor(edges) {
        this.edges = edges;
        this.paths = 0;
        this.inDegree = 0;
        this.visited = false;
    }
}

function main() {
    // let graph = [
    //     new vertex(['a', 'b', 't']),
    //     new vertex(['b']),
    //     new vertex(['t']),
    //     new vertex([])
    // ]

    let graph = [
        new vertex(['c', 'e']),
        new vertex(['c']),
        new vertex(['t']),
        new vertex(['b', 'c']),
        new vertex(['c', 'g']),
        new vertex(['t']),
        new vertex([])
    ]
    
    numberPathsDAG('s', 't', graph)
}

function numberPathsDAG(start, end, graph) {
  /* for each element in the graph of adjacency lists */
    graph.forEach((element) => {
      /* for each edge in the adjacency list */
        element.edges.forEach((element) => {
          /* if there is a vertex in the adjacency list, increase
          the inDegree by one as 'element' points into 'e' */
            let e = graph[nodes[element]];
            e.inDegree += 1
        })
    })
    
    /* initialize a queue */
    let queue = []
    /* push the starting vertex into the queue */
    queue.push(graph[nodes[start]]);
    /* there is obviously a path from 's' to 't' */
    queue[0].paths = 1;
    /* the starting point has been visited */
    queue[0].visited = true;

    /* for each element that the inDegree is 0 and it is 
    visited, push it onto the queue for the topological
    sort algorithm */
    graph.forEach( (element) => {
        if (element.inDegree == 0 && !element.visited) {
            element.visited = true;
            queue.push(element);
        }
    })
    /* while the queue isn't empty */
    while (queue.length > 0) {
      /* grab the first vertex in the queue */
        let curNode = queue[0];
        /* remove the 'curNode' from the queue */
        queue.splice(0, 1);
        /* for each element adjacent to curNode */
        curNode.edges.forEach((element) => {
          /* let e be an element in the adjacency list for curNode*/
            let e = graph[nodes[element]];
            /* dock a degree for the topological sorting algorithm */
            e.inDegree -= 1;
            /* the path of 'e' will be increased by the paths to the
            previous node */
            e.paths += curNode.paths;
            /* for topological sort, push 'e' into the queue if the 
            indegree is 0 */
            if (e.inDegree == 0) {
                queue.push(e);
            }
        })
    }

    console.log(graph[nodes[end]].paths)
}
