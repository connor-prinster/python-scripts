class stack {
    constructor(items) {
        this.items = items;
    }

    size() {
        return this.items.length;
    }

    peek() {
        if (this.items.length > 0) {
            return this.items[this.items.length - 1];
        }
        else {
            return 0;
        }
    }

    pop() {
        return this.items.splice(this.items.length - 1)[0];
    }

    push(item) {
        this.items.push(item);
    }
}

function main() {
    let A = [20, 5, 14, 8, 10, 3, 12, 7, 16]
    longestIncreasingSubsequence(A);
}

function longestIncreasingSubsequence(A) {
    let arr = []
    for (let i = 0; i <= A.length; ++i) {
        arr.push([])
        for (let j = 0; j <= A.length; ++j) {
            arr[i][j] = new stack([]);
        }
    }
    // console.log(arr);
    for (let i = 1; i <= A.length; ++i) {
        for (let j = 1; j <= A.length; ++j ) {
            let left = new stack(arr[i-1][j].items.slice());
            let diag = new stack(arr[i - 1][j - 1].items.slice());
            let lower = new stack(arr[i][j-1].items.slice());
            if (diag.peek() < A[j - 1]) {
                diag.push(A[j - 1]);
            }
            if (left.size() < diag.size()) {
                left = diag;
            }
            else if (diag.size() == left.size() && left.peek() < diag.peek()) {
                left = diag;
            }
            if (left.size() < lower.size()) {
                left = lower;
            }
            else if (lower.size() == left.size() && left.peek() > lower.peek()) {
                left = lower;
            }
            arr[i][j] = left;
        }
    }
    // console.log(arr);
    console.log(arr[arr.length - 1][arr[arr.length - 1].length - 1].items);
}
