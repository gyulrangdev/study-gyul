import { describe, it, expect } from "vitest";
import { merge } from "./merge-intervals";

describe("merge intervals", () => {
  it("should return [[1, 6], [8, 10], [15, 18]]", () => {
    expect(
      merge([
        [2, 6],
        [1, 3],
        [8, 10],
        [15, 18],
      ])
    ).toEqual([
      [1, 6],
      [8, 10],
      [15, 18],
    ]);
  });

  it("should return [[4, 4]]", () => {
    expect(
      merge([
        [4, 4],
        [4, 4],
        [3, 4],
      ])
    ).toEqual([[3, 4]]);
  });
});
