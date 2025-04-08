---
layout: default
---

<div class="container my-5">
    <div class="row">
        <div class="col-lg-6 mb-4">
            <div class="product-images-carousel">
                {% for image in page.images %}
                <img src="{{ image.src | relative_url }}" alt="{{ image.alt }}" class="img-fluid rounded">
                {% endfor %}
            </div>
        </div>

        <div class="col-lg-6">
            <h1>{{ page.title }}</h1>
            <p class="lead text-muted">{{ page.subtitle }}</p>
            <div class="fs-2 fw-bold my-3">${{ page.price }}</div>

            <div class="card mb-3">
                <div class="card-header">
                    <h5 class="mb-0">Details</h5>
                </div>
                <div class="card-body">
                    <ul class="list-unstyled">
                        {% for detail in page.details %}
                        <li class="mb-2"><strong>{{ detail.label }}:</strong> {{ detail.value }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>

            {% if page.rating %}
            <div class="mb-3">
                {{ page.rating_stars }} ({{ page.rating }}) | <a href="#">({{ page.review_count }} Reviews)</a>
            </div>
            {% endif %}

            <div class="card mb-3">
                <div class="card-header">
                    <h5 class="mb-0">How to get it</h5>
                </div>
                <div class="card-body">
                    <p><strong>Delivery:</strong> Available</p>
                    <p class="small">Find options at checkout</p>
                    <hr>
                    <p><a href="#" class="text-decoration-none">Check in-store stock</a></p>
                </div>
            </div>

            <button class="btn btn-success btn-lg w-100 mb-3">Add to cart</button>

            <div class="small text-muted">
                <p>Parcel delivery now $5 above $50 spend.</p>
                <p>See your junior delivery as early as today. Find out more!</p>
            </div>
        </div>
    </div>

    <div class="row my-5">
        <div class="col-12">
            <h2>Product Description</h2>
            <div class="my-3">
                {{ content }}
            </div>
            
            {% if page.care_instructions %}
            <h3 class="mt-4">Care Instructions</h3>
            <p>{{ page.care_instructions }}</p>
            {% endif %}
        </div>
    </div>
</div>