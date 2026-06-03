// 6가지의 요소 조작 메서드

// 1. push
// 배열이 맨 뒤에 새로운 요소를 추가하는 매서드

let arr1 = [1, 2, 3];
arr1.push(4, 5, 6, 7);
// console.log(arr1); // [1, 2, 3, 4, 5, 6, 7]

// 2. pop
// 배열의 맨 뒤 요소를 제거하고 반환하는 매서드

let arr2 = [1, 2, 3];
const poppedItem = arr2.pop();
// console.log(poppedItem); // 3

// 3. shift
// 배열의 맨 앞 요소를 제거하고 반환하는 매서드

let arr3 = [1, 2, 3];
const shiftedItem = arr3.shift();
// console.log(shiftedItem); // 1

// 4. unshift
// 배열의 맨 앞에 새로운 요소를 추가하는 매서드
let arr4 = [1, 2, 3];
arr4.unshift(4, 5, 6, 7);
// console.log(arr4); // [4, 5, 6, 7, 1, 2, 3]

// 🌟shift와 unshift는 push와 pop보다 느리다.
// 인덱스를 한 칸씩 이동시키기 때문에 배열의 길이가 길어질수록 성능이 떨어진다.

// 5. slice
// 배열의 특정 범위를 잘라내서 새로운 배열로 변환

let arr5 = [1, 2, 3, 4, 5];
const slicedArr = arr5.slice(2, 5);
const slicedArr2 = arr5.slice(2);
const slicedArr3 = arr5.slice(-3);

console.log(slicedArr); // [3, 4, 5]
console.log(slicedArr2); // [3, 4, 5]
console.log(slicedArr3); // [3, 4, 5]

// 6. concat
// 두개의 서로 다른 배열을 합쳐서 새로운 배열을 반환

let arr6 = [1, 2, 3];
let arr7 = [4, 5, 6];

let concatArr = arr6.concat(arr7);
console.log(concatArr); // [1, 2, 3, 4, 5, 6]
