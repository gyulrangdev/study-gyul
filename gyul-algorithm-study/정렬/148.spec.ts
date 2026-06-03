import { describe, expect, test } from "vitest";
import { ListNode, sortList, listToArray, arrayToList } from "./148";

describe("sortList", () => {
  test("정렬된 리스트를 반환해야 합니다", () => {
    // 테스트 케이스 준비
    const input = arrayToList([4, 2, 1, 3]);
    const expected = [1, 2, 3, 4];

    // 실행
    const result = sortList(input);

    // 검증 - 배열로 변환하여 비교
    expect(listToArray(result)).toEqual(expected);
  });

  test("음수를 포함한 리스트도 정렬해야 합니다", () => {
    const input = arrayToList([4, -1, 2, 1, 3]);
    const expected = [-1, 1, 2, 3, 4];

    const result = sortList(input);

    expect(listToArray(result)).toEqual(expected);
  });

  test("빈 리스트는 null을 반환해야 합니다", () => {
    expect(sortList(null)).toBeNull();
  });
});
