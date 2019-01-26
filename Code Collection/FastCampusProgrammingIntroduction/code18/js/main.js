//var arr = [1, 2, 3, 4, 5];
//var len = arr.length;
//for(var idx = 0; idx < len; ++idx){
//    console.log(arr[idx]);
//}
//var idx = 0;
//while(idx < len){
//    console.log(arr[idx]);
//    ++idx;
//}

//while(idx < len){
//    if(idx == 2){
//        break;
//    }
//    console.log(arr[idx]);
//    ++idx;
//}

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var result = "";
var len = arr.length;
for(var i = 0; i < len; ++i){
    for (var j = 1; j <= 9; ++j) {
        result += i * j + "<br>";
    }
}
document.write(result);