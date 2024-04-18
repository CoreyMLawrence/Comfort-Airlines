document.addEventListener('DOMContentLoaded', function () {
  // Toggle dropdown menu visibility when clicking on the logo
  document.getElementById('datetime').addEventListener('click', function () {
    const dropdownContent = document.querySelector('.dropdown-content');
    console.log(dropdownContent.style.display);
    if (dropdownContent.style.display != 'flex') {
      dropdownContent.style.display = 'flex';
    } else {
      dropdownContent.style.display = 'none';
    }
  });
});
