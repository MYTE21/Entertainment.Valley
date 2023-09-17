// Function to save the user's input to localStorage
        function saveUserInput() {
            let userInput = document.getElementById("text").value;
            localStorage.setItem("userInput", userInput);
        }

        // Function to populate the textarea with the saved input
        function populateTextarea() {
            let savedInput = localStorage.getItem("userInput");
            if (savedInput) {
                document.getElementById("text").value = savedInput;
            }
        }

        // Call populateTextarea() when the page loads
        window.onload = populateTextarea;