// 기본형 타입 == 원시 타입

// 1. Number Type
let num1 = 10; // 정수
let num2 = 10.5; // 실수
let num3 = -20; // 음수

let inf = Infinity; // 무한대
let mInf = -Infinity; // 음의 무한대

let nan = NaN; // Not a Number 수치연산이 실패했을때 결과값으로 나온다.
console.log(1 * "hello");

// 2. String Type
let myName = "귤랑귤랑";
let myLocation = "용인";
let introduce = myName + myLocation;
let introduceText = ` 제 이름은 ${myName}이고, 사는 곳은 ${myLocation}입니다.`;

// 3. Boolean Type
let isSwitchOn = true;
let isEmpty = false;

// 4. Null Type (값이 없다)
let empty = null;

// 5. Undefined Type (선언은 되었지만 값이 할당되지 않았다.)
let x;
console.log(x);

// Null vs Undefined
console.log(null == undefined); // true
console.log(null === undefined); // false
