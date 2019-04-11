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
    
    console.log(numberPathsDAG('s', 't', graph));
}

function numberPathsDAG(start, end, graph) {
    graph.forEach((element) => {
        element.edges.forEach((element) => {
            let e = graph[nodes[element]];
            e.inDegree += 1
        })
    })
    
    let queue = []
    queue.push(graph[nodes[start]]);
    queue[0].paths = 1;
    queue[0].visited = true;

    graph.forEach( (element) => {
        if (element.inDegree == 0 && !element.visited) {
            element.visited = true;
            queue.push(element);
        }
    })
    while (queue.length > 0) {
        let curNode = queue[0];
        queue.splice(0, 1);
        curNode.edges.forEach((element) => {
            let e = graph[nodes[element]];
            e.inDegree -= 1;
            e.paths += curNode.paths;
            if (e.inDegree == 0) {
                queue.push(e);
            }
        })
    }
    console.log(graph);
    return graph[nodes[end]].paths;
}
