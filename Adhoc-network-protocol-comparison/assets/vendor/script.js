document.addEventListener("DOMContentLoaded", function() {
  const sections = document.querySelectorAll(".collapsible");

  sections.forEach(function(section) {
    const toggleIcon = section.querySelector(".toggle-icon");
    const content = section.querySelector(".content");

    toggleIcon.addEventListener("click", function() {
      section.classList.toggle("active");

      if (section.classList.contains("active")) {
        content.style.opacity = 0;
        setTimeout(function() {
          content.style.opacity = 1;
        }, 100);
      } else {
        content.style.opacity = 0;
      }
    });
  });
});


