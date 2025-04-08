<!-- _includes/product-card.html -->

<div class="product-card">
    <a href="{{ product.url | relative_url }}">
      {% if product.images.size > 0 %}
        <div class="product-image">
          <img src="{{ product.images[0].src | relative_url }}" alt="{{ product.images[0].alt }}">
        </div>
      {% endif %}
      <div class="product-info">
        <h3>{{ product.title }}</h3>
        <p class="product-subtitle">{{ product.subtitle }}</p>
        <div class="product-price">${{ product.price }}</div>
        {% if product.rating %}
          <div class="product-rating">{{ product.rating_stars }}</div>
        {% endif %}
      </div>
    </a>
  </div>