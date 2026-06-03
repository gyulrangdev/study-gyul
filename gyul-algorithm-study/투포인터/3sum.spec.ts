import { threeSum } from "./3sum";
import { describe, expect, it } from "vitest";

describe("threeSum", () => {
  it("should return the correct result", () => {
    expect(threeSum([-1, 0, 1, 2, -1, -4])).toEqual([
      [-1, -1, 2],
      [-1, 0, 1],
    ]);
  });
});
