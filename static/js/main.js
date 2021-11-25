//js for main
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

if (password === "pass@word") {
alert("You have successfully logged in.");
window.location = "selectlevel?"
} else {
    loginErrorMsg.style.opacity = 1;
 }
})