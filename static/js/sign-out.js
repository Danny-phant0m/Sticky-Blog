const signOutButton = document.getElementById("signOutButton");
    signOutButton.addEventListener("click", () => {
        // log out a user using ajax
      const xhr = new XMLHttpRequest(); // Create an XMLHttpRequest object
      xhr.open("POST", "/logout", true); // Open a POST request to the logout route
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // Set header for form data
      xhr.onreadystatechange  = function () {
        if (xhr.status === 200) { // Check for successful response 
          window.location.href = "home"; // Redirect to index.html
        } else {
          alert("Error: Logout failed!"); // Handle errors
        }
      };
      xhr.send(); // Send the request
    });
