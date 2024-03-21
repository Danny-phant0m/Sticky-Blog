let pass1 = document.querySelector('#password');
let pass2 = document.querySelector('#confirm_password');
let result = document.querySelector('#match')

function checkPassword () {
    if (pass1.value && pass2.value) {
        result.innerText = pass1.value == pass2.value ? null : "Oops! It looks like the passwords you entered don't match. Please try again.";
      } else {
        result.innerText = null
      }
}

pass1.addEventListener ('keyup', () => {
    if(pass2.value.length != 0) checkPassword();
})

pass2.addEventListener('keyup', checkPassword);