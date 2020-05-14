$(document).ready(function () {
    console.log("app.js is linked successfully");



});


document.getElementById('wishlist-switch').addEventListener('click', () => {
    Swal.fire(
        'Hi There',
        'This feature is currently in Beta and non operational. It will be implemented in Final Release. <br> Apologies! ',
        'info'
    )
});


/**
 *
 * Swal.fire(
  'The Internet?',
  'That thing is still around?',
  'question'
)
 *
 */