$(document).ready(function () {
    console.log("app.js is linked successfully");


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