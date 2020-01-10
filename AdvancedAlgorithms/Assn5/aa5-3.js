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
  /* Declare an array */
  let arr = [];
  /* Fill the n*m array with 0s */
  for (let i = 0; i <= A.length; ++i) {
    arr.push([]);
    for (let j = 0; j <= B.length; ++j) {
      arr[i][j] = 0;
    }
  }
  /* n complexity */
  for (let i = 1; i <= A.length; ++i) {
    /* m complexity */
    for (let j = 1; j <= B.length; ++j) {
      /*--Note: A&B will be off by one because we start i,j = 1--*/
      /* if A[i-1] and B[j-1] are the same, that means we've found a 
            common number */
      if (A[i - 1] == B[j - 1]) {
        /* the array at [i][j] is then equal to the sum of itself
                and the previous sequence (left-up diagonal) as it
                is appending the successful arr[i][j] to the largest
                common subsequence in the range arr[0...i-1][0...j-1]
                thus reporting an accurate sum for the range
                arr[i][j]*/
        arr[i][j] = A[i - 1] + arr[i - 1][j - 1];
      } else {
        /* if the cells are not the same, the spot is
                filled with the maximum value of either the A's prefix
                neighbor or the B's prefix */
        arr[i][j] = Math.max(arr[i - 1][j], arr[i][j - 1]);
      }
    }
  }

  console.log(arr[arr.length - 1][arr[arr.length - 1].length - 1]);
}
