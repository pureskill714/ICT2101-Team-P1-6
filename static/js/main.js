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
             alert("You have successfully logged in.");
             window.location = "Configlevelpage?"
           } else {
               loginErrorMsg.style.opacity = 1;
           }
          })