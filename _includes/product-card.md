<!-- _includes/product-card.md -->
<div class="card h-100 product-card shadow-sm">
  <a href="{{ product.url | relative_url }}" class="text-decoration-none">
    {% if product.images.size > 0 %}
      <div class="product-image">
        <img src="{{ product.images[0].src | relative_url }}" alt="{{ product.images[0].alt }}" class="card-img-top">
      </div>
    {% endif %}
    <div class="card-body">
      <h5 class="card-title">{{ product.title }}</h5>
      <p class="card-text text-muted small">{{ product.subtitle }}</p>
      <div class="fs-5 fw-bold">${{ product.price }}</div>
      {% if product.rating %}
        <div class="text-warning mt-2">{{ product.rating_stars }}</div>
      {% endif %}
    </div>
  </a>
</div>