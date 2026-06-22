import { describe, expect, it } from "vitest";
import { search } from "./binary-search";

describe("binary-search", () => {
  it("should return the index of the target", () => {
    expect(search([-1, 0, 3, 5, 9, 12], 9)).toBe(4);
  });

  it("should return -1 if the target is not found", () => {
    expect(search([-1, 0, 3, 5, 9, 12], 2)).toBe(-1);
  });
});
