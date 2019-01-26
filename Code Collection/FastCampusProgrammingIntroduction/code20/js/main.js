var date = new Date("1969-12-31");
// 하루 24시간, 1시간 60분, 1분 60초, 1초 1000밀리초
console.log(date.getTime());
console.log(24 * 60 * 60 * 1000)

var str1 = "FastCampus";
var str2 = "Sewon Shin";

console.log(str1.length);
console.log(str2.length);

//charAt(index)
console.log(str1.charAt(0));
console.log(str1.charAt(1));
//split(구분자)
console.log(str2.split(","));
//indexOf(찾을 문자)
console.log(str2.indexOf("n"));