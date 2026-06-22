function expandAroundCenter(str: string, left: number, right: number): number {
  let L = left;
  let R = right;
  while (L >= 0 && R < str.length && str[L] === str[R]) {
    L--;
    R++;
  }
  return R - L - 1;
}

function longestPalindrome(s: string): string {
  if (!s || s.length < 1) {
    return "";
  }
  let start = 0;
  let end = 0;

  for (let i = 0; i < s.length; i++) {
    // 길이 홀수일 때
    const len1 = expandAroundCenter(s, i, i);

    // 길이 짝수일 때
    const len2 = expandAroundCenter(s, i, i + 1);

    const maxLen = Math.max(len1, len2);

    if (maxLen > end - start) {
      start = i - Math.floor((maxLen - 1) / 2);
      end = i + Math.floor(maxLen / 2);
    }
  }
  return s.substring(start, end + 1);
}
