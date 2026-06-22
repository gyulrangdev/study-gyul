export function productExceptSelf(nums: number[]): number[] {
  // 핵심 아이디어: 나눗셈 없이 O(n) 시간에 해결하기!
  //
  // 힌트 1: 각 위치 i에서의 결과 = (i 왼쪽 모든 원소의 곱) × (i 오른쪽 모든 원소의 곱)
  // 힌트 2: 두 번의 순회로 해결할 수 있습니다
  // 힌트 3: 첫 번째 순회에서 왼쪽 곱들을 계산
  // 힌트 4: 두 번째 순회에서 오른쪽 곱들을 계산하면서 최종 결과 완성

  const answer = new Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    answer[i] = answer[i - 1] * nums[i - 1];
  }

  let right = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    answer[i] = answer[i] * right;
    right = right * nums[i];
  }

  // negative zero를 positive zero로 변환
  return answer.map((val) => (val === 0 ? 0 : val));
}
