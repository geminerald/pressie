$(document).ready(function () {
    console.log("app.js is linked successfully");
    if (loggedIn) {
        document.querySelectorAll('logged-in-view').classlist.add('visible')
        document.querySelectorAll('logged-out-view').classlist.add('invisible')
    }
});


const signUpModal = document.getElementById('sign-up-modal');
const loginModal = document.getElementById('login-modal');
const signInOrUp = document.getElementById('sign-in-up-list');

const logins = []

const addLogin = (email) => {
    logins.push(email);
}

let loggedIn = 0;

signUpModal.addEventListener('click', () => {
    Swal.mixin({
        input: 'text',
        confirmButtonText: 'Next &rarr;',
        showCancelButton: true,
        progressSteps: ['1', '2']
    }).queue([{
            title: 'Step 1',
            text: 'Enter your email',
            input: 'email'
        },
        {
            title: 'Step 2',
            text: 'Enter your password',
            input: 'password'
        }
    ]).then((result) => {
        if (result.value) {
            const answers = JSON.stringify(result.value)
            addLogin(answers)
            Swal.fire({
                title: 'All done!',
                confirmButtonText: 'Lovely!',

            })
        }
    })
});

console.log(logins);

const newLocal = true;
loginModal.addEventListener('click', () => {
    Swal.mixin({
        input: 'text',
        confirmButtonText: 'Next &rarr;',
        showCancelButton: true,
        progressSteps: ['1', '2']
    }).queue([{
            title: 'Step 1',
            text: 'Enter your email',
            input: 'email'
        },
        {
            title: 'Step 2',
            text: 'Enter your password',
            input: 'password'
        }
    ]).then((result) => {
        if (result.value) {
            const answers = JSON.stringify(result.value)
            if (logins.includes(answers)) {
                Swal.fire({
                    title: 'All done!',
                    confirmButtonText: 'Lovely!',
                })
                loggedIn ++
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Incorrect Email or Password',
                    footer: '<a href>Why do I have this issue?</a>'
                })
            }
        }
    })
});

console.log(loggedIn);