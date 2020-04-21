$(document).ready(function () {
    console.log("app.js is linked successfully");
});

    let loggedIn = false;

    const signUpModal = document.getElementById('sign-up-modal');
    const loginModal = document.getElementById('login-modal');


    signUpModal.addEventListener('click', () => {
        let loggedIn = true;
        console.log(loggedIn);
    });

    loginModal.addEventListener('click', () => {
        let loggedIn = true;
        console.log(loggedIn);
    });
    if (loggedIn) {
        document.querySelectorAll('logged-in-view').classlist.add('visible')
        document.querySelectorAll('logged-out-view').classlist.add('invisible')
    }



/*
const logins = [
    {
        email: "zac@mail.com",
        password: "123"
    },
    {
        email: "deb@mail.com",
        password: "Hello"
    },
    {
        email: "niki@mail.com",
        password: "Pass"
    }

]

const addLogin = (email) => {
    logins.push(email);
}


const newLocal = true;
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
                loggedIn = True;
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Incorrect Email or Password',
                    footer: 'Try Again'
                })
            }
        }
    })
});

console.log(loggedIn);

*/