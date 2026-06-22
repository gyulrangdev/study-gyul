import { describe, expect, it } from "vitest";
import {
  ListNode,
  arrayToList,
  insertionSortList,
} from "./insertion-sort-list";

describe("insertion sort list", () => {
  it("should return the sorted list", () => {
    const head = arrayToList([4, 2, 1, 3]);
    const sorted = insertionSortList(head);
    expect(sorted).toEqual(arrayToList([1, 2, 3, 4]));
  });

  it("should return the sorted list", () => {
    const head = arrayToList([-1, 0, 3, 4, 5]);
    const sorted = insertionSortList(head);
    expect(sorted).toEqual(arrayToList([-1, 0, 3, 4, 5]));
  });
});
