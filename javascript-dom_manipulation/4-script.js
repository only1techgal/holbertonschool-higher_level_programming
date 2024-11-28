// Selects the div with id "add_item" and the ul with class "my_list"
const addItem = document.querySelector("#add_item");
const myList = document.querySelector(".my_list");

// Adds a click event listener to the add_item element
addItem.addEventListener("click", function () {
    // Creates a new li element
    const newListItem = document.createElement("li");

    // Sets the content of the new li element
    newListItem.textContent = "Item";

    // Appends the new li element to the ul
    myList.appendChild(newListItem);
});
