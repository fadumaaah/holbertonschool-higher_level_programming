
document.addEventListener('DOMContentLoaded', function() {

    const add_item = document.getElementById("add_item");
    const list = document.querySelector(".my_list");
    
    add_item.addEventListener('click', function() {
        const newItem = document.createElement("li");
        newItem.textContent = 'New Item';
        list.appendChild(newItem);
       
        
    });
});

