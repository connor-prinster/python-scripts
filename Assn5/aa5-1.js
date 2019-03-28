function main() {
    let arr = [9, 7, 3, 2]
    let m = 14
    knapsack(arr, m);
}

function knapsack(arr, m) {
    let A = []
    A.push(1);
    for (let i = 1; i <= m; ++i) {
        A.push(0);
    }
    console.log(A);
    for (let i = 0; i < arr.length; ++i) {
        for (let j = m; j >= 1; --j) {
            let val = 0;
            if (j % arr[i] == 0) {
                val = 1;
            }
            let ai = j - arr[i];
            if (ai >= 0) {
                val = Math.max(val, A[j], A[ai])
            }
            else {
                val = Math.max(val, A[j])
            }
            A[j] = val;
        }
        console.log(A);
    }
    if (A[A.length - 1] != 0) {
        console.log('YES');
    }
    else {
        console.log('NO');
    }
}
