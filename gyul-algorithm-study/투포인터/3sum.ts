export function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];

  // 배열이 3개 미만이면 빈 배열 반환
  if (nums.length < 3) {
    return result;
  }

  // 배열을 오름차순으로 정렬
  nums.sort((a, b) => a - b);

  // 첫 번째 숫자를 고정하고 나머지 두 숫자를 투포인터로 찾기
  for (let i = 0; i < nums.length - 2; i++) {
    // 중복된 첫 번째 숫자 건너뛰기
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        // 합이 0인 조합 발견
        result.push([nums[i], nums[left], nums[right]]);

        // 중복된 left 값 건너뛰기
        while (left < right && nums[left] === nums[left + 1]) {
          left++;
        }
        // 중복된 right 값 건너뛰기
        while (left < right && nums[right] === nums[right - 1]) {
          right--;
        }

        left++;
        right--;
      } else if (sum < 0) {
        // 합이 0보다 작으면 left 포인터를 오른쪽으로 이동
        left++;
      } else {
        // 합이 0보다 크면 right 포인터를 왼쪽으로 이동
        right--;
      }
    }
  }

  return result;
}

// Map과 complement를 활용한 대안 솔루션
export function threeSumWithMap(nums: number[]): number[][] {
  const result: number[][] = [];
  const resultSet = new Set<string>(); // 중복 제거를 위한 Set

  if (nums.length < 3) {
    return result;
  }

  // 배열을 정렬 (중복 제거와 결과 정규화를 위해)
  nums.sort((a, b) => a - b);

  // 첫 번째 숫자를 고정
  for (let i = 0; i < nums.length - 2; i++) {
    // 중복된 첫 번째 숫자 건너뛰기
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    const target = -nums[i]; // nums[i] + nums[j] + nums[k] = 0이므로 nums[j] + nums[k] = -nums[i]
    const complementMap = new Map<number, number>(); // value -> index

    // 두 번째, 세 번째 숫자를 Map으로 찾기
    for (let j = i + 1; j < nums.length; j++) {
      const complement = target - nums[j]; // nums[k] = target - nums[j]

      if (complementMap.has(complement)) {
        // complement가 이미 Map에 있다면 triplet 발견
        const triplet = [nums[i], complement, nums[j]].sort((a, b) => a - b);
        const tripletKey = triplet.join(",");

        if (!resultSet.has(tripletKey)) {
          result.push(triplet);
          resultSet.add(tripletKey);
        }
      }

      // 현재 숫자를 Map에 추가
      complementMap.set(nums[j], j);
    }
  }

  return result;
}

// 더 최적화된 Map 기반 솔루션 (중복 처리 개선)
export function threeSumWithMapOptimized(nums: number[]): number[][] {
  const result: number[][] = [];

  if (nums.length < 3) {
    return result;
  }

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // 첫 번째 숫자의 중복 건너뛰기
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    const target = -nums[i];
    const seen = new Set<number>();

    for (let j = i + 1; j < nums.length; j++) {
      const complement = target - nums[j];

      if (seen.has(complement)) {
        result.push([nums[i], complement, nums[j]]);

        // 중복된 두 번째 숫자 건너뛰기
        while (j + 1 < nums.length && nums[j] === nums[j + 1]) {
          j++;
        }
      }

      seen.add(nums[j]);
    }
  }

  return result;
}
