class Node {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
        this.sumRight = 0 //will hold the sum of the sums below it on the right
        this.sumLeft = 0 // same as above but on the left instead
    }
}

function rangeSum(node, xl, xr) {
    /* base case, if there is no node, don't mess with it
    and return 0 as there is no sum here */
    if(node == null) {
        return 0;
    }
    /* if the node's key is too small for the range, 
    move onto the right subtree as there may be values
    there within the appropriate range */
    if(node.key < xl) {
        return rangeSum(node.right, xl, xr)
    }
    /* if the node's key is within xl and xr, we have to 
    return the sums of the valid keys to the left added
    to the sums of the valid keys to the left */
    else if(node.key >= xl && node.key <= xr) {
        let sum = node.key
        // find sums of valid keys to the left
        sum += rangeSumLeft(node.left, xl)
        // find sums of valid keys to the right
        sum += rangeSumRight(node.right, xr)
        return sum
    }
    /* if the node's key is too large for the range, 
    move on to the left subtree as there may be values
    there within the appropriate range */
    else {
        return rangeSum(node.left, xl, xr)
    }
}

/* These are made to ensure we actually add the summations correctly */
function rangeSumLeft(node, xl){
    /* Don't play with null values */
    if (node == null) {
        return 0;
    }
    /* if the key is too small for our range, go to the
    right subtree in order to find values there */
    if (node.key < xl) {
        return rangeSumLeft(node.right, xl);
    }
    /* if the key is within our range */
    else if (node.key >= xl) {
        /* return the summation of the left-hand side, the key value
        and the sum of the right subtree already held in this 
        node */
        return rangeSumLeft(node.left, xl) + node.key +  node.sumRight;
    }
}

/* These are made to ensure we actually add the summations correctly */
function rangeSumRight(node, xr) {
    /* Don't play with null values */
    if (node == null) {
        return 0;
    }
    /* if the value is not within the range, check the left subtree */
    if (node.key > xr) {
        return rangeSumRight(node.left, xr);
    }
    /* if the key is within our range */
    else if (node.key <= xr) {
        /* return the summation of the right-hand side, the key value
        and the sum of the left subtree already held in this 
        node */
        return rangeSumRight(node.right, xr) + node.key + node.sumLeft;
    }
}