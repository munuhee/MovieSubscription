document.getElementById("sidebarToggle").addEventListener("click", function () {
  document.getElementById("sidebar").classList.toggle("-translate-x-full");
});

document.getElementById("sidebarClose").addEventListener("click", function () {
  document.getElementById("sidebar").classList.toggle("-translate-x-full");
});

/*-- profile Dropdown --*/
document.addEventListener("DOMContentLoaded", function () {
  // Toggle user menu visibility
  document
    .getElementById("userMenuButton")
    .addEventListener("click", function (event) {
      event.stopPropagation(); // Prevent the event from propagating to the window
      var userMenu = document.getElementById("userMenu");
      // Toggle the 'hidden' class to show/hide the dropdown menu
      userMenu.classList.toggle("hidden");
    });

  // Close the user menu when clicking outside the menu or the button
  window.addEventListener("click", function (event) {
    var userMenu = document.getElementById("userMenu");
    var userMenuButton = document.getElementById("userMenuButton");
    if (event.target !== userMenu && event.target !== userMenuButton) {
      // If the click is outside the menu or the button, close the menu
      userMenu.classList.add("hidden");
    }
  });
});

/** Messages */
document.getElementById('closeButton').addEventListener('click', function() {
  this.parentElement.style.display = 'none';
});

