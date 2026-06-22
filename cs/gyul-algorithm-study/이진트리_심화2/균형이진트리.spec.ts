import { describe, it, expect } from "vitest";
import { isBalanced } from "./균형이진트리";
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val: number) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function arrayToTree(arr: (number | null)[]): TreeNode | null {
  if (!arr.length || arr[0] === null) return null;

  const root = new TreeNode(arr[0]);
  const queue = [root];
  let i = 1;

  while (queue.length && i < arr.length) {
    const node = queue.shift()!;

    if (i < arr.length && arr[i] !== null) {
      node.left = new TreeNode(arr[i] as number);
      queue.push(node.left);
    }
    i++;

    if (i < arr.length && arr[i] !== null) {
      node.right = new TreeNode(arr[i] as number);
      queue.push(node.right);
    }
    i++;
  }

  return root;
}
describe("isBalanced", () => {
  it("should return true", () => {
    expect(isBalanced(arrayToTree([3, 9, 20, null, null, 15, 7]))).toBe(true);
  });
});
