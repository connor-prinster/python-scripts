const nodes = {
    's': 0,
    'a': 1,
    'c': 2,
    'b': 3,
    'e': 4,
    't': 5
}

const revNodes = {
    0: 's',
    1: 'a',
    2: 'c',
    3: 'b',
    4: 'e',
    5: 't'
}

class vertex {
    constructor(edges) {
        this.edges = edges;
        this.distance = Infinity;
        this.color = "white";
        this.pre = null;
    }
}

function main() {
    let graph = [
        new vertex(['c']),
        new vertex([]),
        new vertex(['b', 'e']),
        new vertex(['t', 'a']),
        new vertex(['t']),
        new vertex([])
    ]
    pathFromS('s', graph);
    // pathToS('s', graph);
}

function pathFromS(start, graph) {
    /* Initialize a queue */
    let queue = []
    /* From the initial graph, push the original starting vertex
    onto the queue */
    queue.push(graph[nodes[start]]);
    /* the distance of the first vertex is 0 */
    queue[0].distance = 0;
    /* the color of the first vertex is blue as it has been
    visited, but not every edge off of it has been visited */
    queue[0].color = "blue";
    /* no predecessors */
    queue[0].pre = 0;
    /* While the queue isn't empty */
    while (queue.length > 0) {
        /* let the current node be the first in the graph */
        let curNode = queue[0];
        /* pop off the first node */
        queue.splice(0, 1);
        /* for each edge attached to the node (adjacency list) */
        curNode.edges.forEach((element) => {
            /* have 'e' be equal to the vertex we are looking at 
            at a particular part of the adjacency list */
            let e = graph[nodes[element]];
            /* if the vertex hasn't been visited */
            if (e.color == 'white') {
                /* mark that the vertex has been visited */
                e.color = "blue";
                /* push it onto the queue */
                queue.push(e);
                /* the distance from 'start' has increased as we are
                one further node away*/
                e.distance = curNode.distance + 1;
                /* the predecessor of this particular node is obviously
                the node we started looking at the vertices of */
                e.pre = graph.indexOf(curNode);
            }
        })
        /* we have looked at each vertex attached to this vertex by the
        time we get here so the curNode has obviously been exhaustively
        searched and is thus red */
        curNode.color = 'red';
    }
    /* just a switch */
    let visited = true;
    /* for each element in the graph, look to see if there are any nodes
    that do not have a predecessor. If one does, the graph does not have a
    path from 'start' to every vertex in 'G' */
    graph.forEach((element) => {
        if (element.pre == null) {
            visited = false;
        }
    })
    /* print yes or no depending */
    visited ? console.log("YES") : console.log("NO");
}

function pathToS(start, graph) {
    /* initialize a graph that will be eventually be
    the reverse of the incoming variable 'graph' */
    let revGraph = []
    /* fill the new graph with vertices equal to that in
    the original graph */
    for (let i = 0; i < graph.length; ++i) {
        revGraph.push(new vertex([]));
    }
    /* for each element in the incoming 'graph', fill the
    reverse graph with it's complement */
    graph.forEach( (element) => {
        element.edges.forEach( (edge) => {
            let e = revGraph[nodes[edge]];
            e.edges.push(revNodes[graph.indexOf(element)]);
        })
    })
    /* begin the algorithm discussed in Problem 1.a with the
    reversed graph */
    pathFromS(start, revGraph);
}
