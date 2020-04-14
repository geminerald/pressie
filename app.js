$(document).ready(function () {
    console.log("app.js is linked successfully");

});


const signUpModal = document.getElementById('sign-up-modal');
const loginModal = document.getElementById('login-modal');
const signInOrUp = document.getElementById('sign-in-up-list');

const logins = []

const addLogin = (email) => {
    logins.push(email);
}

signUpModal.addEventListener('click', () => {
    Swal.mixin({
        input: 'text',
        confirmButtonText: 'Next &rarr;',
        showCancelButton: true,
        progressSteps: ['1', '2']
    }).queue([{
            title:'Step 1',
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
})

console.log(logins);