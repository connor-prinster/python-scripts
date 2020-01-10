/* to have an item of value and size */
class KnapsackItem {
  constructor(size, value) {
    this.size = size;
    this.value = value;
  }
}

/* to have a knapsack of each size limit */
class KnapsackValue {
  constructor(fit, value) {
    this.fit = fit;
    this.value = value;
  }
}

function main() {
  /* Test Array */
  let arr = [
    new KnapsackItem(2, 7),
    new KnapsackItem(7, 4),
    new KnapsackItem(9, 2),
    new KnapsackItem(3, 5)
  ];
  /* Test Weight */
  let m = 14;
  knapsack(arr, m);
}

function knapsack(arr, m) {
  /* Declare an array */
  let A = [];
  /* fill the array with starting values */
  A.push(new KnapsackValue(1, 0));
  for (let i = 1; i <= m; ++i) {
    A.push(new KnapsackValue(0, 0));
  }
  /* n (number of items) complexity */
  for (let i = 0; i < arr.length; ++i) {
    /* M (different sizes of knapsacks) complexity */
    for (let j = m; j >= 1; --j) {
      /* if the size left in the knapsack is sufficient for 
      the 'i-th' item */
      if (j - arr[i].size >= 0) {
        /* 'lower' holds the value of the index where the size
          of the knapsack is equal to 
          A[current knapsack size - size of i-th item] */
        let lower = A[j - arr[i].size];
        /* if the knapsack now held in 'lower' has items that fit
        within it */
        if (lower.fit == 1) {
          /* Since we know that the i-th item will fit in the knapsack 
          there are two different possibilities as to the maximum value
          possibly held in a knapsack of size 'j':
                * the value held int the smaller-sized knapsack plus the
                value of the i-th item being placed in the knapsack of size
                'j'
                * the current value held in a knapsack of size 'j' with 
                different items 
            */
          A[j].value = Math.max(lower.value + arr[i].value, A[j].value);
          /* regardless of which knapsack has the greater value, we know that
          the current bag has items which fit inside of it */
          A[j].fit = 1;
        }
        /* if the i-th item fills the knapsack */
      } else if (j == arr[i].size) {
        /* the value of the knapsack is equal to its only item */
        A[j].value = arr[i].value;
        /* the knapsack can hold the item, so it fits */
        A[j].fit = 1;
      }
    }
  }
  /* initialize a variable */
  let max = 0;
  /* from the different maxes found at different weights, search
  in complexity M for the highest maximum value */
  for (let i = 0; i < A.length; ++i) {
    max = Math.max(max, A[i].value); 
}
  /* print the largest max value */
  console.log(max);
}
