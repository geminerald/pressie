$(document).ready(function () {
    console.log("app.js is linked successfully");

});
const loginModal = document.getElementById('login-modal');

loginModal.addEventListener('click', () => {
    Swal.fire({
        icon: 'info',
        title: 'Sign In',
        input: 'email',
        inputPlaceholder: 'Enter your email address',
        footer: '<a href>Why do I have this issue?</a>'
    })
});