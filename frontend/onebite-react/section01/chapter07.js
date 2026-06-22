// 1. 대입 연산자
let var1 = 1;

// 2. 산술 연산자
let num1 = 3 + 2;
let num2 = 3 - 2;
let num3 = 3 * 2;
let num4 = 3 / 2;
let num5 = 3 % 2;

// 3. 증감 연산자
let num6 = 1;
console.log(++num6); // 전위 연산 : 증가 후 출력
console.log(num6--); // 후위 연산 : 출력 후 감소

// 4. 복합 대입 연산자
let num7 = 1;
num7 += 3;
num7 -= 3;
num7 *= 3;
num7 /= 3;
num7 %= 3;
console.log(num7);

// 5. 비교 연산자
let num8 = 3;
let num9 = 2;
console.log(num8 > num9);
console.log(num8 < num9);
console.log(num8 >= num9);
console.log(num8 <= num9);
console.log(num8 == num9);
console.log(num8 != num9);

// 6. 논리 연산자
let a = true;
let b = false;
console.log(a && b);
console.log(a || b);
console.log(!a);

// 7. 타입 연산자
let num10 = 1;
console.log(typeof num10);
console.log(typeof "문자열");
console.log(typeof true);
console.log(typeof null);
console.log(typeof undefined);
console.log(typeof {});
console.log(typeof []);
console.log(typeof function () {});

// 8. 문자열 연결 연산자
let str1 = "안녕";
let str2 = "하세요";
let str3 = str1 + str2;
console.log(str3);

// 9. 삼항 연산자
let num11 = 10;
let num12 = 20;
let numResult = num11 > num12 ? num11 : num12;
console.log(numResult);

// 10. 연산자 우선순위
console.log(3 + 2 * 4);
console.log((3 + 2) * 4);
console.log(3 > 2 && 2 > 1);
console.log(3 > 2 || 2 > 3);
console.log(!true);
console.log(3 + "hello");
console.log(3 - "hello");
console.log(3 * "hello");
console.log(3 / "hello");
console.log(3 % "hello");
console.log(3 + 2 + "hello");
console.log("hello" + 3 + 2);

// 11. 비트 연산자
let num13 = 10;
let num14 = 2;
console.log(num13 & num14);
console.log(num13 | num14);
console.log(num13 ^ num14);
console.log(~num13);
console.log(num13 << num14);
console.log(num13 >> num14);
console.log(num13 >>> num14);

// 12. 논리 연산자
let ab = true;
let bb = false;
console.log(ab && bb);
console.log(ab || bb);
console.log(!ab);
