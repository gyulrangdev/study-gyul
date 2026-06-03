// 1. Falsy 한 값
let f1 = undefined;
let f2 = null;
let f3 = 0;
let f4 = -0;
let f5 = NaN;
let f6 = "";
let f7 = 0n; // BigInt 아주 큰 숫자를 저장할때 사용된다.

// 2. Truthy 한 값
// -> 7가지 Falsy한 값을 제외한 나머지 모든 값
let t1 = "hello";
let t2 = 25;
let t3 = [];
let t4 = {};
let t5 = function () {};
let t6 = () => {};

// 3. 활용 사례

function printName(person) {
  if (!person) {
    console.log("이름이 없습니다.");
    return;
  }
  console.log(person.name);
}

// let person = null; // person.name에 접근할 경우 에러 발생
let person = {}; // person.name에 접근할 경우 undefined 출력

printName(person);
