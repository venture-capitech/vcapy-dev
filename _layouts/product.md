---
layout: default
---

<div class="product-detail-page">
    <div class="product-images-carousel">
        {% for image in page.images %}
        <img src="{{ image.src | relative_url }}" alt="{{ image.alt }}">
        {% endfor %}
    </div>

    <div class="product-info">
        <h1>{{ page.title }}</h1>
        <p class="product-subtitle">{{ page.subtitle }}</p>
        <div class="product-price">${{ page.price }}</div>

        <div class="product-details-list">
            <h3>Details</h3>
            <ul>
                {% for detail in page.details %}
                <li><strong>{{ detail.label }}:</strong> {{ detail.value }}</li>
                {% endfor %}
            </ul>
        </div>

        <div class="product-ratings">
            {{ page.rating_stars }} ({{ page.rating }}) | <a href="#">({{ page.review_count }} Reviews)</a>
        </div>

        <div class="how-to-get">
            <h3>How to get it</h3>
            <div class="delivery-options">
                <p><strong>Delivery:</strong> Available</p>
                <p><small>Find options at checkout</small></p>
            </div>
            <div class="store-purchase">
                <p><a href="#">Check in-store stock</a></p>
            </div>
        </div>

        <button class="add-to-cart-button">Add to cart</button>

        <div class="parcel-delivery-info">
            <p><small>Parcel delivery now $5 above $50 spend.</small></p>
            <p><small>See your junior delivery as early as today. Find out more!</small></p>
        </div>
    </div>
</div>

<div class="product-details-section">
    <h2>Product Description</h2>
    {{ content }}
    
    {% if page.care_instructions %}
    <h3>Care Instructions</h3>
    <p>{{ page.care_instructions }}</p>
    {% endif %}
</div>
