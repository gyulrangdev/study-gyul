// 1. null 병합 연산자
// 존재하는 값을 추려낸다.
// null, undefined가 아닌 값을 찾아낸다.

let var1;
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2;
console.log(var4);
console.log(var2 ?? var3);

let userName;
let userNickName;
let user = userName ?? userNickName ?? "guest";
console.log(user);

// 2. typeof 연산자
// 값의 타입을 문자열로 반환한다.

let var7 = true;
console.log(typeof var7);

// 3. 삼항 연산자
// 조건식 ? 참일때 반환값 : 거짓일때 반환값
let var8 = 10;
let var9 = 1;

let res = var8 % 2 == 0 ? "짝수" : "홀수";
console.log(res);
console.log(var8 ? "참" : "거짓");
