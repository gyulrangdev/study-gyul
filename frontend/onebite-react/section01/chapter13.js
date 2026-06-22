// 1. 콜백함수
// 콜백이라는 말은 프로그래밍에서는 "뒷전에 실행되는, 나중에 실행되는" 이라는 뜻이다.

function main(value) {
  value();
}

function sub() {
  //   console.log("i am sub");
}

main(sub);

// 언제 써먹을 수 있을까?

// 2. 콜백함수의 활용
function repeat(count, callback) {
  for (let idx = 1; idx <= count; idx++) {
    callback(idx);
  }
}

// function repeatDouble(count) {
//   for (let idx = 1; idx <= count; idx++) {
//     console.log(idx * 2);
//   }
// }

// function repeatTriple(count) {
//   for (let idx = 1; idx <= count; idx++) {
//     console.log(idx * 3);
//   }
// }

// 콜백 함수를 이용하면 중복을 제거하고 좀 더 간결하게 코드를 작성할 수 있다.
repeat(5, function (idx) {
  console.log(idx * 2);
});
