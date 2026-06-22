// 1. 상수 객체
const animal = {
  type: "토끼",
  name: "토순이",
  color: "white",
};

// 오류 발생
// animal = { a: 1 };

animal.age = 2; // 추가
animal.name = "토토"; // 수정
delete animal.color; // 삭제

// 2. 매서드
// 값이 함수인 프로퍼티

const person = {
  sayHi: function () {
    console.log("hi");
  },
  sayHello() {
    console.log("hello"); // 함수를 선언할 수도 있다
  },
};

person.sayHi();
person.sayHello(); // 동작을 정의하는데 사용이 된다.
