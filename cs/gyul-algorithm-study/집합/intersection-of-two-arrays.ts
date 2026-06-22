function intersection(nums1: number[], nums2: number[]): number[] {
  const set1 = new Set(nums1);
  const set2 = new Set(nums2);
  const result: number[] = [];

  set1.forEach((v) => {
    if (set2.has(v)) result.push(v);
  });

  return result;
}

// 필터를 사용한 방법
function intersectionWithFilter(nums1: number[], nums2: number[]): number[] {
  const set2 = new Set(nums2);
  return [...new Set(nums1.filter((num) => set2.has(num)))];
}

// 이중 반복문을 사용한 방법 (브루트 포스)
function intersectionWithNestedLoop(
  nums1: number[],
  nums2: number[]
): number[] {
  const result = new Set<number>();

  for (const num1 of nums1) {
    for (const num2 of nums2) {
      if (num1 === num2) {
        result.add(num1);
        break; // 현재 num1에 대한 일치를 찾았으므로 내부 루프 종료
      }
    }
  }

  return [...result];
}

// 정렬 후 투 포인터 방식
function intersectionWithTwoPointers(
  nums1: number[],
  nums2: number[]
): number[] {
  // 중복 제거 및 정렬
  const sorted1 = [...new Set(nums1)].sort((a, b) => a - b);
  const sorted2 = [...new Set(nums2)].sort((a, b) => a - b);

  const result: number[] = [];
  let p1 = 0,
    p2 = 0;

  while (p1 < sorted1.length && p2 < sorted2.length) {
    if (sorted1[p1] < sorted2[p2]) {
      p1++;
    } else if (sorted1[p1] > sorted2[p2]) {
      p2++;
    } else {
      // 값이 같을 때 (교집합)
      result.push(sorted1[p1]);
      p1++;
      p2++;
    }
  }

  return result;
}

// Map을 사용한 방법
function intersectionWithMap(nums1: number[], nums2: number[]): number[] {
  const map = new Map<number, boolean>();
  const result: number[] = [];

  // 첫 번째 배열의 고유 값들을 맵에 저장
  for (const num of nums1) {
    map.set(num, true);
  }

  // 두 번째 배열을 순회하며 맵에 있는 값을 결과에 추가하고, 맵에서 제거
  for (const num of nums2) {
    if (map.has(num)) {
      result.push(num);
      map.delete(num); // 중복 추가 방지
    }
  }

  return result;
}

// 이진 검색을 활용한 방법
function intersectionWithBinarySearch(
  nums1: number[],
  nums2: number[]
): number[] {
  // 두 개의 배열 중 작은 것을 기준으로 검색하는 것이 효율적
  let smaller = [...new Set(nums1)];
  let larger = [...new Set(nums2)];

  if (smaller.length > larger.length) {
    [smaller, larger] = [larger, smaller]; // 배열 교환
  }

  // 큰 배열 정렬
  larger.sort((a, b) => a - b);

  const result: number[] = [];

  // 이진 검색 함수
  function binarySearch(arr: number[], target: number): boolean {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);

      if (arr[mid] === target) {
        return true;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return false;
  }

  // 작은 배열의 각 요소에 대해 큰 배열에서 이진 검색
  for (const num of smaller) {
    if (binarySearch(larger, num)) {
      result.push(num);
    }
  }

  return result;
}
