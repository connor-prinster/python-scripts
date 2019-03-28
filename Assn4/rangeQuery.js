class Node {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

function rangeQuery(node, xl, xr) {
    /* don't try to follow a node that doesn't exist*/
    if( node != null) {
        /* if the node's key is too small, follow the 
        right subtree as there may be values in there 
        within xl and xr */
       if(node.key < xl) {
           rangeQuery(node.right, xl, xr)
       }
       /* if the node's key is between xl and xr we
       must traverse both its subtrees and look for values
       there. We have to print the value of the node's key
       after the left keys are printed and before the right
       keys are printed in order for the keys to be printed
       in order */
       else if(node.key > xl && node.key < xr) {
           rangeQuery(node.left, xl, xr)
           console.log(node.key)
           rangeQuery(node.right, xl, xr)
       }
       /* if the key is greater than xr, follow the left
       subtree as there may be valid values there */
       else {
           rangeQuery(node.left, xl, xr)
       }
    }
    return;
}