/**
 * 주어진 문자열에서 가장 많이 등장하는 단어를 반환합니다.
 * @param paragraph 주어진 문자열
 * @param banned 금지된 단어 배열
 * @returns 가장 많이 등장하는 단어
 * 시간 복잡도 : O(n + m)
 * 공간 복잡도 : O(n)
 * n은 문자열의 길이, m은 금지된 단어의 수
 */
export function mostCommonWord(paragraph: string, banned: string[]): string {
  const words = paragraph.toLowerCase().split(/[!?',;. ]/g);
  const map = new Map<string, number>();

  for (const word of words) {
    if (word !== "") {
      map.set(word, (map.get(word) ?? 0) + 1);
    }
  }

  for (const ban of banned) {
    map.delete(ban);
  }

  let maxWord = "";
  let maxCount = 0;

  // sort 메소드를 사용하면 시간 복잡도가 O(n log n)이 되어 비효율적이므로
  // 직접 최대값을 찾는 방식으로 구현
  for (const [word, count] of map.entries()) {
    if (count > maxCount) {
      maxWord = word;
      maxCount = count;
    }
  }

  return maxWord;
}
