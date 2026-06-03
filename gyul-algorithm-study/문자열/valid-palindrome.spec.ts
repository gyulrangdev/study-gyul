import { describe, it, expect } from "vitest";
import { isPalindrome } from "./valid-palindrome";

describe("isPalindrome", () => {
  it("should return true for a palindrome", () => {
    expect(isPalindrome("A man, a plan, a canal: Panama")).toBe(true);
  });

  it("should return false for a non-palindrome", () => {
    expect(isPalindrome("0P")).toBe(false);
  });

  it("should return true for palindrome", () => {
    expect(isPalindrome("a")).toBe(true);
  });
});
