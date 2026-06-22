/**
 * 75. Sort Colors
 * https://leetcode.com/problems/sort-colors/
 *
 * nums 배열에는 0, 1, 2만 포함되어 있으며, 이를 오름차순으로 정렬해야 함
 * one-pass 알고리즘을 사용해 제자리에서 정렬
 *
 * @param nums - 0, 1, 2로 이루어진 배열
 */

function sortColors1(nums: number[]): void {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[j] > nums[j + 1]) {
        let temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }
}

// 세 개의 포인터를 사용하는 Dutch national flag algorithm
export function sortColors(nums: number[]): void {
  let low = 0;
  let mid = 0;
  let high = nums.length - 1;

  while (mid <= high) {
    if (nums[mid] === 0) {
      [nums[low], nums[mid]] = [nums[mid], nums[low]];
      low++;
      mid++;
    } else if (nums[mid] === 1) {
      mid++;
    } else if (nums[mid] === 2) {
      [nums[mid], nums[high]] = [nums[high], nums[mid]];
      high--;
    }
  }
}
