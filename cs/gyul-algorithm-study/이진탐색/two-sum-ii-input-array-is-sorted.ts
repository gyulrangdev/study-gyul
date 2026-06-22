/**
 * MAP을 이용한 풀이
 * @param numbers
 * @param target
 * @returns
 */
function twoSum(numbers: number[], target: number): number[] {
  const map = new Map();

  for (let i = 0; i < numbers.length; i++) {
    const c = target - numbers[i];
    if (map.has(c)) {
      return [map.get(c) + 1, i + 1];
    } else {
      map.set(numbers[i], i);
    }
  }
  return [-1, -1];
}

/**
 * Two Pointer 풀이
 */
function twoSumTwoPointer(numbers: number[], target: number): number[] {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const sum = numbers[left] + numbers[right];
    if (sum === target) {
      return [left + 1, right + 1];
    } else if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
  return [-1, -1];
}
