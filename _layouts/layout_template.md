---
title: ${product.title} - My Shop
layout: product
---

{% include header.md %}

<div class="product-container" markdown="1">
${product.title}
<div class="product-price">
  $${product.price}
</div>
<div class="product-gallery">
  <div class="gallery-main">
    <img src="${product.featured_image}" alt="${product.title}" id="featuredImage">
  </div>
  <div class="gallery-dots">
    {% for image in product.images %}
      <span class="gallery-dot" data-image="{{ image.url }}"></span>
    {% endfor %}
    {% for video in product.videos %}
      <span class="gallery-dot video-dot" data-video="{{ video.url }}"></span>
    {% endfor %}
  </div>
</div>
Product Description
${product.description}
</div>

{% include footer.md %}
