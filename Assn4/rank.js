class Node {
  constructor(key) {
    this.key = key;
    this.left = null;
    this.right = null;
    this.rank = null;
  }
}

let root = new Node(null);

function rankUtility(val) {
  rank(val, root);
}

function rank(val, node) {
  /* there were no values here meaning there is no
  associated .rank value, must return 0 + 1 = 1*/
  if (node == undefined) {
    return Number(1);
  } 
  /* if the node's key is equal to the value we're 
  looking for, return the rank of the node to get 
  the rank of the value */
  else if (node.key == val) {
    return node.rank;
  }
  /* if 'val' is smaller than the node's value the
  rank will be found in the left child */
  else if (node.key > val) {
    return rank(val, node.left);
  } 
  /* if node's key is smaller than 'val', the rank 
  of the value is the total rank of the children 
  on its left and all numbers less than 'val' on
  its right */
  else if (node.key < val) {
    return rank(val, node.left) + rank(val, node.right) + 1;
  }
}
