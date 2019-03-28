class tuple {
  constructor(weight, value) {
    this.weight = weight;
    this.value = value;
  }
}

//need to watch for adding weights to be less than M
//do not add values after adding weights

function main() {
  let weightArr = [9, 7, 3, 2];
  let valueArr = [7, 4, 2, 5];
  let arr = [];
  for (i = 0; i < weightArr.length; i++) {
    arr.push(new tuple(weightArr[i], valueArr[i]));
  }
  let m = 14;
  //   console.log(arr)
  knapsack(arr, m);
}

function knapsack(arr, m) {
  // setting up A to hold all the fun stuff
  let A = [];
  // make sure that A contains a one in the first column
  A.push(new tuple(1, 0));
  // remainder of A must be 0s
  for (let i = 1; i <= m; ++i) {
    A.push(new tuple(0, 0));
  }
  for (let i = 0; i < arr.length; ++i) {
    for (let j = m; j >= 1; --j) {
      let val = 0;
      if (j % arr[i].weight == 0) {
        val = 1;
      }
      let ai = j - arr[i].weight;
      if (ai >= 0) {
        val = Math.max(val, A[j].weight, A[ai].weight);
      } else {
        val = Math.max(val, A[j].weight);
      }
      A[j] = new tuple(val, 0)//val;
    }
    console.log(A);
  }
  if (A[A.length - 1].value != 0) {
    console.log("YES");
  } else {
    console.log("NO");
  }
}
