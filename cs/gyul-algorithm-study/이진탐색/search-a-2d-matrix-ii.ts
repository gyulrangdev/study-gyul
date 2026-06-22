function searchMatrix(matrix: number[][], target: number): boolean {
  if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
    return false;
  }

  // 행렬의 크기
  const m = matrix.length;
  const n = matrix[0].length;

  // 오른쪽 위 모서리에서 시작
  let row = 0;
  let col = n - 1;

  // 행렬의 범위 내에 있는 동안 반복
  while (row < m && col >= 0) {
    if (matrix[row][col] === target) {
      return true; // 타겟을 찾았으면 true 반환
    } else if (matrix[row][col] < target) {
      row++; // 현재 값이 타겟보다 작으면 아래로 이동
    } else {
      col--; // 현재 값이 타겟보다 크면 왼쪽으로 이동
    }
  }

  return false; // 타겟을 찾지 못하면 false 반환
}
