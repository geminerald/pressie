$(document).ready(function () {
    console.log("app.js is linked successfully");

    // Page Element Selectors
    const surpriseSwitch = document.getElementById('surprise-switch');
    const orderedSwitch = document.getElementById('ordered-switch');
    const privateSwitch = document.getElementById('private-switch')
    const filterSearch = document.getElementById('finder-search');
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');


    /**
     * Navigation Slide function for small devices
     */
    const navSlide = () => {

        burger.addEventListener('click', () => {
            nav.classList.toggle('nav-active');
            navLinks.forEach((link, index) => {
                if (link.style.animation) {
                    link.style.animation = '';
                } else {
                    link.style.animation = `navLinkFade 0.3s ease-in forwards ${index/7+1}s`;
                }
            });
            burger.classList.toggle('toggle');
        });
    }

    navSlide();

    /**
     * 
     * @param Element
     * Takes an element in beta and notifies user via an alert 
     */
    const betaNotification = (element) => {
        element.addEventListener('click', () => {
            Swal.fire(
                'Hi There',
                'This feature is currently in Beta and non operational. It will be implemented in Final Release. <br><br> Apologies! ',
                'info'
            )
        });
    };

    // Add beta notifications to beta elements on page
    if (surpriseSwitch) {
        betaNotification(surpriseSwitch);
    }
    if (filterSearch) {
        betaNotification(filterSearch);
    }
    if (orderedSwitch) {
        betaNotification(orderedSwitch);
    }
    if (privateSwitch) {
        betaNotification(privateSwitch);
    }
});
