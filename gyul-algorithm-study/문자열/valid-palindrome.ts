import { measureExecutionTime, whichIsFaster } from "../util/time";

// export function isPalindrome(s: string): boolean {
//   const cleaned = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
//   return cleaned === cleaned.split("").reverse().join("");
// }

// export function isPalindrome(s: string): boolean {
//   s = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
//   for (let i = 0; i < s.length; i++) {
//     if (s[i] !== s[s.length - i - 1]) {
//       return false;
//     }
//   }

//   return true;
// }

// 투 포인터 방식
export function isPalindromeTowPointer(s: string): boolean {
  s = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

export function isPalindrome(s: string): boolean {
  s = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  const len = s.length;
  if (len === 0 || len === 1) return true;
  for (let i = 0; i < Math.floor(len / 2); i++) {
    if (s[i] !== s[len - i - 1]) {
      return false;
      break;
    }
  }

  return true;
}

console.log(
  "isPalindrome :: ",
  measureExecutionTime(isPalindrome, "A man, a plan, a canal: Panama")
);
console.log(
  "isPalindromeTowPointer :: ",
  measureExecutionTime(isPalindromeTowPointer, "A man, a plan, a canal: Panama")
);

console.log(
  "whichIsFaster :: ",
  whichIsFaster(
    isPalindrome,
    isPalindromeTowPointer,
    "A man, a plan, a canal: Panama"
  )
);
