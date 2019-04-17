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
    let arr = []
    for (let i = 0; i <= k; ++i) {
        arr.push([]);
        for (let j = 0; j < graph.length; ++j) {
            arr[i].push(Infinity);
        }
    }

    graph[nodes[start]].weight = 0;

    for (let i = 1; i <= k; ++i) {
        for (let j = 0; j < graph.length; ++j) { // For each vertex from s to t in topological order
            let curNode = graph[j];
            if (curNode.length + 1 <= i) {
                curNode.edges.forEach( (edge) => {
                    let e = graph[nodes[edge[0]]];
                    if (e.weight > curNode.weight + edge[1]) {
                        e.length = curNode.length + 1;
                        e.weight = curNode.weight + edge[1];
                    }
                    arr[i][nodes[edge[0]]] = Math.min(arr[i - 1][nodes[edge[0]]], arr[i][nodes[edge[0]]], e.weight);
                })
            }
        }
    }

    let length = k;
    let smallest = arr[k][nodes[end]];
    for (let i = k; i >= 0; --i) {
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
    console.log(length);
}

