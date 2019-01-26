// document.getElementsByName("testText")[0].onkeydown = function(e){
//     var eventCode = e.code;
//     if(eventCode == 'Digit1'){
//         document.getElementById("test").innerHTML = "<img src='static/Oimachi Tokyo.jpg'>";
//     }else if(eventCode == 'Digit2'){
//         document.getElementById("test").innerHTML = "<img src='static/p Jumping Sundog.jpg'>";
//     }
// };

// document.getElementsByName("testText")[0].onkeyup = function(e){
//     if(e.code == 'Backspace'){
//         document.getElementById("test").innerHTML = "";
//     }
// }

document.getElementsByClassName("btn")[0].onfocus = function(){
    document.getElementById("test").innerHTML = "Tab을 이용한 이벤트 -> onmouseover";
};

document.getElementsByClassName("btn")[0].onblur = function(){
    document.getElementById("test").innerHTML = "Tab을 이용한 이벤트 -> onmouseout";
};