document.addEventListener('DOMContentLoaded', function() {

    const red_header = document.getElementById("red_header");
    
    red_header.addEventListener('click', function() {
        red_header.style.color = "#FF0000"
    });
});