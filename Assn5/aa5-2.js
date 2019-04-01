class KnapsackItem {
    constructor(size, value) {
        this.size = size;
        this.value = value;
    }
}

class KnapsackValue {
    constructor(fit, value) {
        this.fit = fit;
        this.value = value;
    }
}

function main() {
    let arr = [
        new KnapsackItem(2, 7),
        new KnapsackItem(7, 4),
        new KnapsackItem(9, 2),
        new KnapsackItem(3, 5)
    ];
    let m = 14;
    knapsack(arr, m)
}

function knapsack(arr, m) {
    let A = []
    A.push(new KnapsackValue(1, 0))
    for (let i = 1; i <= m; ++i) {
        if (i == 2) {
            console.log(new KnapsackValue(0, 0))
        }
        A.push(new KnapsackValue(0, 0));
    }
    for (let i = 0; i < arr.length; ++i) {
        for (let j = m; j >= 1; --j) {
            // let val = A[j];
            if (j - arr[i].size >= 0) {
                let lower = A[j - arr[i].size];
                if (lower.fit == 1) {
                    // val = Math.max(val.value, lower.value + val.value)
                    A[j].value = Math.max(lower.value + arr[i].value, A[j].value);
                    A[j].fit = 1;
                }
            }
            else if (j == arr[i].size) {
                A[j].value = arr[i].value;
                A[j].fit = 1;
            }
        }
        console.log(A);
    }
    let max = 0;
    for (let i = 0; i < A.length; ++i) {
        max = Math.max(max, A[i].value);
    }
    console.log(max);
}
