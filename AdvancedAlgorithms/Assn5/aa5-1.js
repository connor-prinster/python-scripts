function main() {
    let arr = [9, 7, 3, 2]
    let m = 14
    knapsack(arr, m);
}

/*pass in an array and the weight M allowed*/
function knapsack(arr, m) {
    /*set up the opening array*/
    let A = []
    A.push(1);
    for (let i = 1; i <= m; ++i) {
        A.push(0);
    }
    console.log(A)
    /*--M*n time compexity for-loop--*/
    /* n complexity (different items to be placed) */
    for (let i = 0; i < arr.length; ++i) {
        /* M complexity (varying size of knapsack) */
        for (let j = m; j >= 1; --j) {
            /*  initialize a variable to be used later  */
            let val = 0;
            /*  if the value at arr[i] is a divisor
                of j, we know for sure that the item
                used here can be placed in the knapsack
                'x' amount of times and reach weight 'j' */ 
            if (j % arr[i] == 0) {
                val = 1;
            }
            /*  ai represents the weight left over after
                adding the previous item */
            let ai = j - arr[i];
            /* space still left in the sack */
            if (ai >= 0) {
                /*  return the max value:
                    * if 'val' is one, arr[i] was a divisor
                    and thus can be placed in the knapsack x times
                    * if 'A[j]' is one, we already know that the 
                    weight specified has a solution
                    * if 'A[ai]' is one, we know that the remaining
                    weight in the bag can be filled with whatever
                    allowed A[ai] to be filled completely
                    ** Regardless of the outcome, the val is either
                    one or zero */
                val = Math.max(val, A[j], A[ai])
            }
            /* no space left in knapsack */
            else {
                /*  return max value
                    * if 'val' is one, arr[i] was a divisor
                    and thus can be placed in the knapsack x times 
                    * if 'A[j]' is one, we already know that the 
                    weight specified has a solution */
                val = Math.max(val, A[j])
            }
            /* the table at weight 'j' equals the either one or zero */
            A[j] = val;
        }
        console.log(A);
    }
    /*  print the value at the right-most index or at the weight specified
        in the main() function */
    if (A[A.length - 1] != 0) {
        console.log('YES');
    }
    else {
        console.log('NO');
    }
}
