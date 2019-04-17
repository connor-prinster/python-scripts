const nodes = {
    's': 0,
    'a': 1,
    'b': 2,
    'c': 3,
    't': 4,
}

class vertex {
    constructor(edges) {
        this.edges = edges;
        this.weight = Infinity;
        this.length = 0;
    }
}

function main() {
    let graph = [
        new vertex([['t', 5], ['a', 1], ['c', 4]]),
        new vertex([['b', 1]]),
        new vertex([['t', 1]]),
        new vertex([['t', 3]]),
        new vertex([])
    ]
    kLinkShortestPath('s', 't', graph, 2);
}

function kLinkShortestPath(start, end, graph, k) {
    /* initialize the 2d array */
    let arr = []
    /* create an array that is k * graph.length */
    for (let i = 0; i <= k; ++i) {
        arr.push([]);
        for (let j = 0; j < graph.length; ++j) {
            arr[i].push(Infinity);
        }
    }

    /* have all the starting points in the array start with a weight
    of 0 similar to all other forms of dynamic programming graphs */
    graph[nodes[start]].weight = 0;

    /* keep the k * (m + n) going */
    for (let i = 1; i <= k; ++i) {
        /* go through the length of the graph for all the nodes' adjacency lists */
        for (let j = 0; j < graph.length; ++j) { // For each vertex from s to t in topological order
            /* let the current node be the jth node in the graph */
            let curNode = graph[j];
            /* if the length of the path from the 'start' to the current node is less than or equal
            to the current value of 'k' */
            if (curNode.length + 1 <= i) {
                /* for each node in the adjacency list */
                curNode.edges.forEach( (edge) => {
                    /* let 'e' be the node of name edge[0] */
                    let e = graph[nodes[edge[0]]];
                    /* if the weight of the node adjacent to curNode is greater curNode.weight plus the
                    weight of the node adjacent, replace the weight in the next node. Increase the
                    weight of the path as well */
                    if (e.weight > curNode.weight + edge[1]) {
                        e.length = curNode.length + 1;
                        e.weight = curNode.weight + edge[1];
                    }
                    /* have the dependency relation be for the minimum weight */
                    arr[i][nodes[edge[0]]] = Math.min(arr[i - 1][nodes[edge[0]]], arr[i][nodes[edge[0]]], e.weight);
                })
            }
        }
    }

    /* make sure the length is equal to the k passed in the function declaration */
    let length = k;
    /* the smallest value will be in the top left corner */
    let smallest = arr[k][nodes[end]];
    /* check all the different values that 't' can have from 1 to k */
    for (let i = k; i >= 0; --i) {
        /* if the weight at a smaller 'k' is less than at the largest value
        of 'k', replace it */
        if (arr[i][nodes[end]] <= smallest) {
            smallest = arr[i][nodes[end]];
            length = i;
        }
        else if (arr[i][nodes[end]] == smallest) {
            length = i;
        }
    }
    console.log(arr);
    console.log(graph);
    console.log('the weight of the smallest length is', smallest);
}