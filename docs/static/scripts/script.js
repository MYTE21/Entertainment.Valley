// Save User's Input To Local Storage
function saveUserInput() {
    let userInput = document.getElementById("text").value;
    localStorage.setItem("userInput", userInput);
}

// Populate Text Area With Saved Input
function populateTextarea() {
    let savedInput = localStorage.getItem("userInput");
    if (savedInput) {
        document.getElementById("text").value = savedInput;
    }
}

// Call populateTextarea Method When Page Loads
window.onload = populateTextarea;
