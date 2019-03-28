function builder(A, B) {
  let F = [];
  for (i = 0; i < A.length + 1; i++) {
    let temp = [];
    for (j = 0; j < B.length + 1; j++) {
      temp.push(0);
    }
    F.push(temp);
  }

  return F;
}

function main() {
  let A = [36, -12, 40, 2, -5, 7, 3];
  let B = [2, 7, 36, 5, 2, 4, 3, -5, 3];
  let F = builder(A, B);

  for (i = 1; i <= A.length; i++) {
    for (j = 1; j <= B.length; j++) {
      if (A[i - 1] == B[j - 1]) {
        F[i][j] = F[i - 1][j - 1] + A[i - 1];
      } else {
        F[i][j] = Math.max(F[i - 1][j], F[i][j - 1]);
      }
    }
  }

  console.log(F[A.length][B.length]);
}
