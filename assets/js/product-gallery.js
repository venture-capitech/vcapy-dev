// assets/js/product-gallery.js

document.addEventListener('DOMContentLoaded', function() {
    const dots = document.querySelectorAll('.gallery-dot');
    const featuredImage = document.getElementById('featuredImage');
    
    // Initialize with first dot active
    if (dots.length > 0) {
      dots[0].classList.add('active');
    }
    
    // Add click event to each dot
    dots.forEach((dot, index) => {
      dot.addEventListener('click', function() {
        // Remove active class from all dots
        dots.forEach(d => d.classList.remove('active'));
        
        // Add active class to clicked dot
        this.classList.add('active');
        
        // Update featured media (image or video)
        if (this.hasAttribute('data-video')) {
          // Create video element if it's a video
          const videoUrl = this.getAttribute('data-video');
          featuredImage.parentNode.innerHTML = `
            <video id="featuredImage" controls autoplay>
              <source src="${videoUrl}" type="video/mp4">
              Your browser does not support the video tag.
            </video>
          `;
        } else {
          // Update image source if it's an image
          const imageUrl = this.getAttribute('data-image');
          featuredImage.parentNode.innerHTML = `
            <img src="${imageUrl}" alt="Product Image" id="featuredImage">
          `;
        }
      });
    });
  });