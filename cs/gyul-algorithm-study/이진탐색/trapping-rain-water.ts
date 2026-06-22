function trap(height: number[]): number {
  if (height.length <= 2) return 0;

  const n = height.length;
  let result = 0;

  // 왼쪽과 오른쪽의 최대 높이를 저장할 배열 생성
  const leftMax = new Array(n).fill(0);
  const rightMax = new Array(n).fill(0);

  // 왼쪽 방향으로 최대 높이 계산
  leftMax[0] = height[0];
  for (let i = 1; i < n; i++) {
    leftMax[i] = Math.max(leftMax[i - 1], height[i]);
  }

  // 오른쪽 방향으로 최대 높이 계산
  rightMax[n - 1] = height[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    rightMax[i] = Math.max(rightMax[i + 1], height[i]);
  }

  // 각 위치마다 물의 양 계산
  for (let i = 0; i < n; i++) {
    // 현재 위치에서 고일 수 있는 물의 양은 양쪽 최대 높이 중 작은 값에서 현재 높이를 뺀 값
    result += Math.min(leftMax[i], rightMax[i]) - height[i];
  }

  return result;
}

// 더 최적화된 해결법 (투 포인터 사용)
function trapOptimized(height: number[]): number {
  if (height.length <= 2) return 0;

  let left = 0;
  let right = height.length - 1;
  let leftMax = height[left];
  let rightMax = height[right];
  let result = 0;

  while (left < right) {
    if (leftMax < rightMax) {
      // 왼쪽이 결정적이면 왼쪽으로 이동
      left++;
      leftMax = Math.max(leftMax, height[left]);
      result += leftMax - height[left];
    } else {
      // 오른쪽이 결정적이면 오른쪽으로 이동
      right--;
      rightMax = Math.max(rightMax, height[right]);
      result += rightMax - height[right];
    }
  }

  return result;
}
