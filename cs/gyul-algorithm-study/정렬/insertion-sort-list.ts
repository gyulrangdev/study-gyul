export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export function insertionSortList(head: ListNode | null): ListNode | null {
  if (head === null || head.next === null) return head;

  // 더미 노드를 생성하여 정렬된 리스트의 시작점으로 사용
  let dummy = new ListNode(0);
  let curr: ListNode | null = head;
  let next: ListNode | null = null;

  // 원본 리스트의 각 노드를 순회하며 정렬된 리스트에 삽입
  while (curr !== null) {
    // 다음 노드를 저장
    next = curr.next;

    // 정렬된 리스트에서 삽입 위치 찾기
    let prev = dummy;
    let sortedCurr = dummy.next;

    // 삽입할 위치 찾기: curr.val보다 큰 값을 가진 노드 직전에 삽입
    while (sortedCurr !== null && sortedCurr.val < curr.val) {
      prev = sortedCurr;
      sortedCurr = sortedCurr.next;
    }

    // 현재 노드를 정렬된 리스트의 올바른 위치에 삽입
    curr.next = sortedCurr;
    prev.next = curr;

    // 다음 노드로 이동
    curr = next;
  }

  return dummy.next;
}

// 테스트를 위한 배열을 리스트로 변환하는 함수
export function arrayToList(arr: number[]): ListNode | null {
  if (arr.length === 0) return null;
  const dummy = new ListNode(0);
  let current = dummy;

  for (const val of arr) {
    current.next = new ListNode(val);
    current = current.next;
  }

  return dummy.next;
}

insertionSortList(
  new ListNode(4, new ListNode(2, new ListNode(1, new ListNode(3))))
);
