// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

/**
 * Best Time to Buy and Sell Stock
 *
 * 문제: 주식 가격 배열에서 한 번 사고 한 번 팔아 최대 이익을 구하기
 *
 * 접근법 1: 원패스 알고리즘 (O(n) 시간, O(1) 공간)
 * - 지금까지 본 최소 가격을 추적
 * - 각 날에 팔았을 때의 이익을 계산하여 최대값 업데이트
 */

function maxProfit(prices: number[]): number {
  if (prices.length <= 1) return 0;

  let minPrice = prices[0]; // 지금까지의 최소 가격
  let maxProfit = 0; // 최대 이익

  for (let i = 1; i < prices.length; i++) {
    const currentPrice = prices[i];

    // 현재 가격이 지금까지의 최소 가격보다 낮으면 업데이트
    if (currentPrice < minPrice) {
      minPrice = currentPrice;
    } else {
      // 현재 가격에 팔았을 때의 이익 계산
      const currentProfit = currentPrice - minPrice;
      maxProfit = Math.max(maxProfit, currentProfit);
    }
  }

  return maxProfit;
}

/**
 * 접근법 2: 슬라이딩 윈도우 (Two Pointer)
 * - 왼쪽 포인터: 구매일 (최소값 추적)
 * - 오른쪽 포인터: 판매일 (순회)
 * - 손실이 발생하면 왼쪽 포인터를 오른쪽으로 이동
 */
function maxProfitSlidingWindow(prices: number[]): number {
  if (prices.length <= 1) return 0;

  let left = 0; // 구매 포인터
  let right = 1; // 판매 포인터
  let maxProfit = 0;

  while (right < prices.length) {
    // 현재 이익 계산
    const currentProfit = prices[right] - prices[left];

    if (currentProfit > 0) {
      // 이익이 있으면 최대값 업데이트
      maxProfit = Math.max(maxProfit, currentProfit);
    } else {
      // 손실이면 새로운 시작점으로 이동
      left = right;
    }

    right++;
  }

  return maxProfit;
}

/**
 * 접근법 3: 카데인 알고리즘 (Kadane's Algorithm) 변형
 * - 연속된 차이값의 최대 부분 배열 합을 구하는 문제로 변환
 */
function maxProfitKadane(prices: number[]): number {
  if (prices.length <= 1) return 0;

  let maxCurrent = 0; // 현재까지의 최대 이익
  let maxGlobal = 0; // 전체 최대 이익

  for (let i = 1; i < prices.length; i++) {
    // 전날 대비 가격 변화
    const dailyProfit = prices[i] - prices[i - 1];

    // 현재까지의 최대 이익 계산
    maxCurrent = Math.max(dailyProfit, maxCurrent + dailyProfit);

    // 전체 최대 이익 업데이트
    maxGlobal = Math.max(maxGlobal, maxCurrent);
  }

  return maxGlobal;
}

// 테스트 케이스
console.log("=== Best Time to Buy and Sell Stock 테스트 ===");

const testCases = [
  [7, 1, 5, 3, 6, 4], // 예상: 5 (1에서 사고 6에서 팔기)
  [7, 6, 4, 3, 1], // 예상: 0 (계속 하락)
  [1, 2, 3, 4, 5], // 예상: 4 (1에서 사고 5에서 팔기)
  [2, 4, 1], // 예상: 2 (2에서 사고 4에서 팔기)
  [1], // 예상: 0 (하루만 있음)
  [], // 예상: 0 (빈 배열)
];

testCases.forEach((prices, index) => {
  console.log(`\n테스트 케이스 ${index + 1}: [${prices}]`);
  console.log(`원패스 알고리즘: ${maxProfit(prices)}`);
  console.log(`슬라이딩 윈도우: ${maxProfitSlidingWindow(prices)}`);
  console.log(`카데인 알고리즘: ${maxProfitKadane(prices)}`);
});

// 메인 솔루션 (가장 직관적이고 효율적)
export default maxProfit;
