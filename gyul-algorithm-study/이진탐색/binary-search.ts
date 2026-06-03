/**
 * 이진 탐색
 * @param nums 정렬된 배열
 * @param target 찾을 값
 * @returns 찾은 값의 인덱스
 *
 * 시간복잡도: O(log n)
 * 공간복잡도: O(1)
 */

export function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (target === nums[mid]) {
      return mid;
    } else if (target < nums[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return -1;
}
