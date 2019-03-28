

function isKthSmallestLessThanX(A, k, x) {
    /* to traverse a minheap, we have to start at index 1 */
    index = 1;
    /* to make sure we don't check more than k items */
    counter = {count: 0};
    /* go through the min heap */
    isKthSmallestLessThanXHelper(A, index, k, x, counter);
    /* when the function above returns, if there were k items
    smaller than x, counter.count will have a value equal to k
    and then print "yes." Otherwise, it will print "no" */
    if (counter.count < k) {
        return "No";
    }
    else {
        return "Yes";
    }
}

/* given a minheap, the index to look at the minheap of, the 
number of items we cannot search more than, the value we must 
compare all node.keys to and the counter object that will 
increment each time that a node has a key smaller than x */
function isKthSmallestLessThanXHelper(A, index, k, x, counter) {
    /* if the index of the minheap is less than x AND we have 
    not searched more than 'k' nodes, we increment the counter
    to say we he seen a value less than x */
    if ( A[index] < x && counter.count < k) {
        /* Going through requires an increase in the counter */
        counter.count += 1;
        /* can access index of left subtrees with (index * 2) */
        isKthSmallestLessThanXHelper(A, index * 2, k, x, counter);
        /* can access index of right subtrees with ((index * 2) + 1) */
        isKthSmallestLessThanXHelper(A, index * 2 + 1, k, x, counter);
    }
    return;
}

function main() {
    minHeap = [null, 1, 2, 4, 3, 9, 7, 8, 14, 10, 16]
    console.log(isKthSmallestLessThanX(minHeap, 5, 5,));
}