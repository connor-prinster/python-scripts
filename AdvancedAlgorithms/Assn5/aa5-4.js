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
    } else {
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
  let A = [20, 5, 14, 8, 10, 3, 12, 7, 16];
  longestIncreasingSubsequence(A);
}

function longestIncreasingSubsequence(A) {
  /* Declare the array */
  let arr = [];
  /* Set up the array with 'stack' items */
  for (let i = 0; i <= A.length; ++i) {
    arr.push([]);
    for (let j = 0; j <= A.length; ++j) {
      arr[i][j] = new stack([]);
    }
  }

  /* n complexity */
  for (let i = 1; i <= A.length; ++i) {
    /* n complexity */
    for (let j = 1; j <= A.length; ++j) {
      /* cell to the left */
      let left = new stack(arr[i - 1][j].items.slice());
      /* cell up-left diagonal */
      let diag = new stack(arr[i - 1][j - 1].items.slice());
      /* cell up */
      let lower = new stack(arr[i][j - 1].items.slice());
      /* if the cell above has a number greater than the current
      cell's number, append the smaller number to the array of 
      the diagonal's */
      if (diag.peek() < A[j - 1]) {
        diag.push(A[j - 1]);
      }
      /* if the size of the left's array is smaller than the diagonal 
      array, set the left array equal to the diagonal. */
      if (left.size() < diag.size()) {
        left = diag;
      } 
      /* if the left and diagonal's array lengths are the same, we must
      then look at the numbers in the arrays. if the left's first number
      is smaller than the diagonal's, set the left equal to the diagonal */
      else if (diag.size() == left.size() && left.peek() < diag.peek()) {
        left = diag;
      }
      /* if the size of the left is smaller than the size of the lower,
      set the left equal to the lower */
      if (left.size() < lower.size()) {
        left = lower;
      } 
      /* if the sizes of the left and the lower are the same, check the arrays
      of both. if the left has a last value higher than lower does, set left
      equal to lower */
      else if (lower.size() == left.size() && left.peek() > lower.peek()) {
        left = lower;
      }
      /* set the value of arr[i][j] to the value held in left */
      arr[i][j] = left;
    }
  }
  // console.log(arr);
  console.log(arr[arr.length - 1][arr[arr.length - 1].length - 1].items);
}
