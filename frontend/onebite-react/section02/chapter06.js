// 객체와 배열 순회(Iteration)하기

// 1. 배열 순회
let arr = [1, 2, 3, 4, 5];

// 1.1 배열 인덱스
for (let i = 0; i < arr.length; i++) {
  //   console.log(arr[i]);
}

// 1.2 for of 반복문
for (let item of arr) {
  console.log(item);
}

// 2. 객체 순회

let person = {
  name: "김규리",
  age: 28,
  hobby: "코딩",
};

// 2.1 Object.keys 사용
// 객체에서 key 값만 추출하여 배열로 반환

let keys = Object.keys(person);

for (let key of keys) {
  console.log(key, person[key]);
}

// 2.2 Object.values 사용
let values = Object.values(person);

for (let value of values) {
  console.log(value);
}

// 2.3 for in // 객체 순회
for (let key in person) {
  const value = person[key];
  console.log(key, value);
}
