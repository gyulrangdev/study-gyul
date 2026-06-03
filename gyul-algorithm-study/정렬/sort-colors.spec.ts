import { describe, expect, it } from "vitest";
import { sortColors } from "./sort-colors";

describe("sortColors", () => {
  it("should sort the colors", () => {
    const nums = [2, 0, 2, 1, 1, 0];
    sortColors(nums);
    expect(nums).toEqual([0, 0, 1, 1, 2, 2]);
  });
});
