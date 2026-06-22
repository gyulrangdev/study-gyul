// 1. 함수 표현식

function funcA() {
  console.log("funcA");
}

let varA = funcA;
varA();

// 익명 함수
// 콜백 함수에서 유용하게 사용할 수 있다.
// 함수를 값으로 할당할 경우에는 호이스팅이 적용되지 않는다.
let varB = function () {
  console.log("funcB");
};
varB();

// 2. 화살표 함수
let varC = (value) => {
  console.log("varC");
  return 1 + value;
};

console.log(varC(10));
