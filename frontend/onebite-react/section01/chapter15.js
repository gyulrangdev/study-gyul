// 1. 객체 생성
let obj1 = new Object(); // 객체 생성자
let obj2 = {}; // 객체 리터럴

// 2. 객체 프로퍼티 (객체 속성)
// 프로퍼티 키 : 프로퍼티 값
// 키 : 문자열이나 숫자로만 가능
//
let person = {
  name: "김규리",
  age: 27,
  hobby: "자전거타기",
  job: "FE Developer",
  extra: {},
  "key with space": true, // 키에 공백이 있는 경우
};

// 3. 객체 프로퍼티 다루는 방법
// 3.1 특정 프로퍼티에 접근 (점 표기법, 괄호 표기법)

let name2 = person.name;

let age = person["age"];

let property = "hobby";
let hobby = person[property];

// 3.2 새로운 프로퍼티를 추가하는 방법
person["favoritefood"] = "초밥";

// 3.3 프로퍼티 수정
person.job = "BE Developer";

// 3.4 프로퍼티 삭제
delete person.extra;
delete person["favoritefood"];

// 3. 프로퍼티 존재 여부 확인
let result1 = "name" in person;
let result2 = "cat" in person;
