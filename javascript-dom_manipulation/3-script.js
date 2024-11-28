// Selects the header and the div with the id toggle_header
const header = document.querySelector("header");
const toggleHeader = document.querySelector("#toggle_header");

// Adds a click event listener to the div
toggleHeader.addEventListener("click", function () {
    // Toggles the class between red and green
    if (header.classList.contains("red")) {
        // If the header has the class 'red', it changes it to 'green'
        header.classList.remove("red");
        header.classList.add("green");
    } else {
        // If the header doesn't have the class 'red', it changes it to 'red'
        header.classList.remove("green");
        header.classList.add("red");
    }
});
