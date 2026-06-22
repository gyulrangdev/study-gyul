// 5가지의 요소 순회 및 탐색 매서드

// 1. forEach
// 모든 요소를 순회하면서, 각각의 요소에 특정 동작을 수행시키는 매서드

let arr1 = [1, 2, 3];
arr1.forEach(function (item, idx, arr) {
  //   console.log(idx, item * 2, arr);
});

let doubledArr = [];
arr1.forEach(function doubled(item) {
  doubledArr.push(item * 2);
});

// console.log(doubledArr);

// 2. includes
// 배열에 특정 요소가 있는지 확인하는 매서드

let arr2 = [1, 2, 3];
arr2.includes(2); // true
arr2.includes(4); // false

// 3. indexOf
// 특정 요소의 위치를 찾아서 반환
let arr3 = [1, 2, 3];
let index = arr3.indexOf(2);
arr3.indexOf(20); // -1
// console.log(index); // 1

/**
 * indexOf는 얕은 비교를 한다
 */
let objectArr = [{ name: "apple" }, { name: "banana" }];
objectArr.indexOf({ name: "banana" }); // -1

// 4. findIndex
// 모든 요소를 순회하면서, 콜백 함수를 만족하는 그런
// 특정 요소의 인덱스(위치를 반환하는 메서드)

let arr4 = [1, 2, 3, 4];
const findedIndex = arr4.findIndex((item) => item % 2 !== 0);

// 콜백 함수는 함수를 인자로 받기 때문에 복잡한 객체도 조건값만 잘 넘겨주면 인덱스를 찾을 수 있다
objectArr.findIndex((item) => item.name === "banana"); // 1

console.log(findedIndex);

// 5. find
// findIndex와 비슷하지만, 요소 자체를 반환

let arr5 = [
  { name: "apple", price: 1000 },
  { name: "banana", price: 2000 },
];

const findResult = arr5.find((item) => item.name === "banana"); // { name: 'banana', price: 2000 }
console.log(findResult);
