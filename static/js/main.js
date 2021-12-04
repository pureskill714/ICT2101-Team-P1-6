

function open_form_btn1(){
     document.getElementById('my_form').style.display = "block"
     }
function close_btn(){
     document.getElementById('my_form').style.display ="none"
     }
          const loginForm = document.getElementById("form");
          const loginButton = document.getElementById("login");
          loginButton.addEventListener("click", (e) => {
          e.preventDefault();
          const password = loginForm.password.value;

          if (password === "test") {
             window.location = "Configlevelpage?"
           } else {
               alert("Fail authentication");
               window.location = "main?"
           }
          })
function disableselect(e){
    return false
}
function reEnable(){
    return true
}
document.onselectstart=new Function ("return false")
    if (window.sidebar){
    document.onmousedown=disableselect
    document.onclick=reEnable
}
document.onkeydown = function (e)
{
        if (event.keyCode == 123) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && (e.keyCode == 'I'.charCodeAt(0) || e.keyCode == 'i'.charCodeAt(0))) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && (e.keyCode == 'C'.charCodeAt(0) || e.keyCode == 'c'.charCodeAt(0))) {
            return false;
        }
        if (e.ctrlKey && e.shiftKey && (e.keyCode == 'J'.charCodeAt(0) || e.keyCode == 'j'.charCodeAt(0))) {
            return false;
        }
        if (e.ctrlKey && (e.keyCode == 'U'.charCodeAt(0) || e.keyCode == 'u'.charCodeAt(0))) {
            return false;
        }
        if (e.ctrlKey && (e.keyCode == 'S'.charCodeAt(0) || e.keyCode == 's'.charCodeAt(0))) {
            return false;
        }
 }