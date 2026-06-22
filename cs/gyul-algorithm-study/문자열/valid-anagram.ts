/**
 *시간복잡도: O(n)
 * s 문자열을 순회: O(n)
 * t 문자열을 순회: O(n)
 * Map의 get, set, has, delete 연산은 O(1)
 * 총 O(n + n) = O(n)
 *
 *공간복잡도: O(n)
 * charsMap 크기: O(n)
 * 총 O(n)
 */
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  const charsMap = new Map<string, number>();
  for (const char of s) {
    const prevCount = charsMap.get(char) ?? 0;
    charsMap.set(char, prevCount + 1);
  }

  for (const char of t) {
    if (!charsMap.has(char)) {
      return false;
    }

    const prevCount = charsMap.get(char);
    if (prevCount && prevCount > 1) {
      charsMap.set(char, prevCount - 1);
    } else {
      charsMap.delete(char);
    }
  }

  return charsMap.size === 0;
}

/**
 * 시간복잡도: O(n)
 * s 문자열을 순회: O(n)
 * t 문자열을 순회: O(n)
 * Map의 get, set, has, delete 연산은 O(1)
 * 총 O(n + n) = O(n)
 *
 * 공간복잡도: O(n)
 * map 크기: O(n)
 * 총 O(n)
 */
function isAnagram2(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const map = new Map<string, number>();

  for (let i = 0; i < s.length; i++) {
    map.set(s[i], (map.get(s[i]) ?? 0) + 1);
  }

  for (let i = 0; i < t.length; i++) {
    if (!map.has(t[i])) {
      return false;
    }

    if (map.has(t[i])) {
      if ((map.get(t[i]) ?? 0) - 1 === 0) {
        map.delete(t[i]);
      } else {
        map.set(t[i], (map.get(t[i]) ?? 0) - 1);
      }
    }
  }

  return true;
}
