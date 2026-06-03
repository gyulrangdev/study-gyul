// 5가지 배열 변형 메서드
// 1. filter
// 기존 배열에서 조건을 만족하는 요소들만 필터링하여 해당하는 객체를 새로운 배열로 변환

let arr1 = [
  { name: "apple", price: 1000 },
  { name: "banana", price: 1000 },
  { name: "cherry", price: 2000 },
];

const price1000 = arr1.filter((item) => {
  if (item.price === 1000) return true;
});
console.log(price1000);

// 2. map
// 배열의 모든 요소를 순회하면서, 각각 콜백함수를 실행하고 그 결과값들을 모아서 새로운 배열로 반환

let arr2 = [1, 2, 3];
const mapResult1 = arr2.map((item, idx, arr) => {
  console.log(idx, item);
  return item * 2;
});
console.log(mapResult1);

let names = arr1.map((item) => item.name);
console.log(names);

// 3. sort
// 배열을 사전순으로 정렬
let arr3 = ["b", "a", "c", 10, 3, 5];
arr3.sort();
// 10, 3, 5는 정렬이 정상적으로 되지않음
// '사전순'으로 정렬해서 (대소 비교를 하지 않음)
//

arr3.sort((a, b) => {
  // 오름차순
  if (a > b) {
    // b가 a 앞으로 와라
    return 1; // b,a 순으로 정렬
  } else if (a < b) {
    // a가 b 앞으로 와라
    return -1; // a,b 순으로 정렬
  } else {
    // 두 값의 자리를 바꾸지 마라
    return 0;
  }

  // 내림차순
  //   if(a>b){
  //     return -1
  //   }else(a<b){
  //     return 1
  //   }
  //   else{
  //     return 0
  //   }
});

// 4. toSorted
// sort와 똑같은 메소드인데, 원본 배열을 변형하지 않고 새로운 배열을 반환
let arr5 = ["b", "a", "c", 10, 3, 5];
const sorted = arr5.toSorted();
console.log(sorted);

// 5. join
// 배열의 모든 요소를 하나의 문자열로 변환하는 매서드
let arr6 = ["hi", "im", "gyuri"];
console.log(arr6.join(" ")); // hi im gyuri
