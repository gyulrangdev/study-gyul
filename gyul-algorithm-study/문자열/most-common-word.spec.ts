import { describe, expect, it } from "vitest";
import { mostCommonWord } from "./most-common-word";

describe("mostCommonWord", () => {
  it("should return the most common word in the paragraph", () => {
    expect(
      mostCommonWord(
        "Bob hit a ball, the hit BALL flew far after it was hit.",
        ["hit"]
      )
    ).toBe("ball");
  });

  it("should return the most common word in the paragraph", () => {
    expect(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])).toBe("b");
  });
});
