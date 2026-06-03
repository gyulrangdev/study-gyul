function largestNumber(nums: number[]): string {
  const numStrs = nums.map((num) => num.toString());
  numStrs.sort((a, b) => (b + a).localeCompare(a + b));
  if (numStrs[0] === "0") return "0";
  return numStrs.join("");
}

console.log(largestNumber([10, 2]));
