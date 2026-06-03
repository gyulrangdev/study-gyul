import { describe, it, expect } from "vitest";
import { arrayPairSum } from "./array-partition";

describe("arrayPairSum", () => {
  it("should return the maximum sum of pairs", () => {
    expect(arrayPairSum([1, 4, 3, 2])).toBe(4);
  });

  it("should return the maximum sum of pairs", () => {
    expect(arrayPairSum([6, 2, 6, 5, 1, 2])).toBe(9);
  });
});
