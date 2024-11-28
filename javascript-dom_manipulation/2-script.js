// Selects the div with id "red_header"
const redHeader = document.querySelector("#red_header");

// Selects the header element
const header = document.querySelector("header");

// Adds an event listener to the div
redHeader.addEventListener("click", function () {
    // Adds the 'red' class to the header
    header.classList.add("red");
});
