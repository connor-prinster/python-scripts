function main() {
    let A = [36, -12, 40, 2, -5, 7, 3];
    let B = [2, 7, 36, 5, 2, 4, 3, -5, 3];
    // let A = [0, -9, -6, -10, -1, 1, -9, -2, 2, 5, 7, 7, 8, 9, 6, 2, -4, -2];
    // let B = [0, 8, -6, -7, 5, -8, -7, 8, -10, 0, -9, -7, 9, 2, 1, -6, 3];
    // let A = [1, 2, 3, 4, 5, 6];
    // let B = [2, 1, 4, 3, 6, 5];
    maxSumSubsequence(A, B);   
}

function maxSumSubsequence(A, B) {
    let arr = []
    for (let i = 0; i <= A.length; ++i) {
        arr.push([]);
        for (let j = 0; j <= B.length; ++j) {
            arr[i][j] = 0;
        }
    }
    for (let i = 1; i <= A.length; ++i) {
        for (let j = 1; j <= B.length; ++j) {
            if (A[i-1] == B[j-1]) {
                arr[i][j] = A[i-1] + arr[i-1][j-1];
            }
            else {
                arr[i][j] = Math.max(arr[i-1][j], arr[i][j-1])
            }
        }
    }
    // console.log(arr)
    console.log(arr[arr.length - 1][arr[arr.length - 1].length - 1])
}
