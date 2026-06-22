// 실행 시간 측정 함수
export function measureExecutionTime(
  fn: Function,
  input: any,
  iterations: number = 1000
): number {
  const start = performance.now();
  for (let i = 0; i < iterations; i++) {
    fn(input);
  }
  const end = performance.now();
  return (end - start) / iterations; // 평균 실행 시간 반환
}

// 어떤 함수가 더 빠른지 알려주는 함수
export function whichIsFaster(fn1: Function, fn2: Function, input: any) {
  const time1 = measureExecutionTime(fn1, input);
  const time2 = measureExecutionTime(fn2, input);
  return time1 < time2 ? fn1 : fn2;
}
