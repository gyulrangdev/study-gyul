function solution(n: number, times: number[]): number {
  // 이분탐색의 범위 설정
  let left = 1; // 최소 시간
  let right = Math.max(...times) * n; // 최대 시간 (가장 느린 심사관이 모든 사람을 심사하는 경우)
  let answer = right;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    // mid 시간 동안 심사할 수 있는 총 인원 수 계산
    let totalPeople = 0;
    for (const time of times) {
      totalPeople += Math.floor(mid / time);
      // 이미 n명 이상 처리 가능하면 더 계산할 필요 없음
      if (totalPeople >= n) break;
    }

    if (totalPeople >= n) {
      // n명 이상 처리 가능하면 시간을 줄여서 최소값 찾기
      answer = mid;
      right = mid - 1;
    } else {
      // n명 처리 불가능하면 시간을 늘리기
      left = mid + 1;
    }
  }

  return answer;
}
