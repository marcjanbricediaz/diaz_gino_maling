
  window.addEventListener("DOMContentLoaded", () => {
    const skeleton = document.getElementById("skeletonLoader");
    const actual = document.getElementById("actualTable");
    const searchInput = document.getElementById("searchInput");

    // Disable search during loading
    searchInput.disabled = true;
    searchInput.placeholder = "Loading users...";

    setTimeout(() => {
      skeleton.classList.add("hidden");
      actual.classList.remove("hidden");

      // Re-enable search after loading
      searchInput.disabled = false;
      searchInput.placeholder = "Search by Full Name...";
    }, 1000);
  });