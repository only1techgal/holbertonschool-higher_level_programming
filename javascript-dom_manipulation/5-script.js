// Selects the header element and the div with id "update_header"
const header = document.querySelector("header");
const updateHeader = document.querySelector("#update_header");

// Adds a click event listener to the update_header element
updateHeader.addEventListener("click", function () {
    // Updates the text content of the header
    header.textContent = "New Header!!!";
});
