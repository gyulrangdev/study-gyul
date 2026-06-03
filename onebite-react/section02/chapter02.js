// 단락 평가
// Short-Circuit Evaluation

function returnFalse() {
  console.log("False 함수");
  return false;
}

function returnTrue() {
  console.log("True 함수");
  return true;
}

// console.log(returnFalse() && returnTrue()); // True 함수는 출력이 되지 않음
// 단락 평가 // 논리 연산식에서 첫번째 피연산자 만으로도 이 연산의 값을 확정할 수 있다면 두번째 피연사자는 접근조차 하지 않는 실행방식을 말한다.

// console.log(returnTrue() && returnFalse()); // 두번째 피연산자 까지 접근

// console.log(returnFalse() || returnTrue());

// 단락평가 활용사례

function printName(person) {
  const name = person && person.name;
  console.log(name || "이름이 없습니다.");
  console.log(person && person.name);
  // 단락평가에 의해 person.name에는 접근하지 않음
  // 따라서 person의 값인 undefined가 출력됨
}
printName();
printName({ name: "John" });
