// https://leetcode.com/problems/balanced-binary-tree/

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

export function isBalanced(root: TreeNode | null): boolean {
  // 균형 이진 트리
  // 왼쪽 노드와 오른쪽 노드 높이 차이가 1 이하
  function dfs(node: TreeNode | null): number {
    if (!node) return 0;

    const left = dfs(node.left);
    if (left === -1) return -1;

    const right = dfs(node.right);
    if (right === -1) return -1;

    if (Math.abs(left - right) > 1) return -1;

    return Math.max(left, right) + 1;
  }

  return dfs(root) !== -1;
}
