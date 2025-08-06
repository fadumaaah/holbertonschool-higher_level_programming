document.addEventListener('DOMContentLoaded', function() {

    const header = document.querySelector("header");
    const toggle_header = document.getElementById("toggle_header");
    
    toggle_header.addEventListener('click', function() {
        if (header.classList.contains('red'))
        {
            header.classList.remove('red')
            header.classList.add('green')

        }
        else {
            header.classList.remove('green')
            header.classList.add('red')
        }
    });
});


