$(document).ready(function () {
    console.log("app.js is linked successfully");

    const navSlide = () => {
        const burger = document.querySelector('.burger');
        const nav = document.querySelector('.nav-links');
        const navLinks = document.querySelectorAll('.nav-links li');

        burger.addEventListener('click', () => {
            nav.classList.toggle('nav-active');
            navLinks.forEach((link, index) => {
                if (link.style.animation) {
                    link.style.animation = '';
                } else {
                    link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1}s`;
                }
            });
            burger.classList.toggle('toggle');
        });
    }

    navSlide();

    const wishSwitch = document.getElementById('wishlist-switch');
    const filterSearch = document.getElementById('finder-search')
    if (wishSwitch) {
        wishSwitch.addEventListener('click', () => {


            Swal.fire(
                'Hi There',
                'This feature is currently in Beta and non operational. It will be implemented in Final Release. <br><br> Apologies! ',
                'info'
            )
        });
    }


    if (filterSearch) {

        filterSearch.addEventListener('click', () => {
            Swal.fire(
                'Hi There',
                'This feature is currently in Beta and non operational. It will be implemented in Final Release. <br><br> Apologies! ',
                'info'
            )
        });

    }
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