const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});


signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

const form = document.querySelector('form');
form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent form submission reload

    const keyInput = form.querySelector('input[type="text"]').value; // Get the key
    
    const response = await fetch('http://127.0.0.1:5000/verify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key: keyInput }),
    });

    const result = await response.json();
    if (result.status) {
        alert(result.message); // Authenticated
    } else {
        alert(result.message); // Not Authenticated
    }
});
