document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll(".collapsible");
  
    sections.forEach(function(section) {
      const toggleIcon = section.querySelector(".toggle-icon");
      const content = section.querySelector(".content");
  
      toggleIcon.addEventListener("click", function() {
        const isActive = section.classList.contains("active");
  
        // Close all sections
        sections.forEach(function(s) {
          s.classList.remove("active");
          s.querySelector(".content").style.opacity = 0;
        });
  
        if (!isActive) {
          section.classList.add("active");
          setTimeout(function() {
            content.style.opacity = 1;
          }, 100);
        }
      });
    });
  });
  