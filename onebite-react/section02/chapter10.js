// 1. Date 객체를 생성하는 방법

let date1 = new Date(); // 생성자
// console.log(date1); // 현재 시간

let date2 = new Date("1996.01.12.10:10:10");
console.log(date2); // 1996-01-12T00:00:00.000Z

// 1월을 0으로 해야 January가 나옴
let date3 = new Date(1996, 0, 12, 10, 10, 10);
console.log(date3); // 1996-01-12T01:10:10.000Z

// 2. 타임 스탠프
// 특정 시간이 "1970.01.01. 00:00:00" 이후로 몇 ms가 지났는지 의미하는 숫자값
// UTC
let ts1 = date1.getTime();

let date4 = new Date(ts1);

console.log(date1, date4);

// 3. 시간 요소를 추출하는 방법
let year = date1.getFullYear();
// js에서 월은 0부터 시작
let month = date1.getMonth() + 1;
let date = date1.getDate();

let hour = date1.getHours();
let minute = date1.getMinutes();
let second = date1.getSeconds();

// console.log(year, month, date, hour, minute, second);

// 4. 시간 수정하기
date1.setFullYear(2023);
date1.setMonth(2); // js에서는 0부터 시작하기 때문에 3월
date1.setDate(15);

// 5. 시간을 여러 포맷으로 출력하기
console.log(date1.toDateString());
console.log(date1.toLocaleString());
console.log(date1.toLocaleDateString());
