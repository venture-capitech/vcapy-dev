---
layout: default
---

<div class="hero-section text-white text-center py-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <h1 class="display-4 fw-bold">{{ page.hero_title }}</h1>
        <p class="lead">{{ page.hero_subtitle }}</p>
        <a href="{{ page.hero_button_url }}" class="btn btn-success btn-lg px-4 my-3">{{ page.hero_button_text }}</a>
      </div>
    </div>
  </div>
</div>

<div class="container my-5">
  <h2 class="text-center mb-4">{{ page.featured_section_title }}</h2>
  <div class="row g-4">
    {% for product_id in page.featured_products %}
      {% assign product = site.products | where: "slug", product_id | first %}
      {% if product %}
        <div class="col-lg-4 col-md-6">
          {% include product-card.md product=product %}
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>


<div class="container my-5">
  <h2 class="text-center mb-4">{{ page.featured_section_title }}</h2>
  <div class="row g-4">
    {% for product_id in page.featured_productlines %}
      {% assign product = site.products | where: "slug", product_id | first %}
      {% if product %}
        <div class="col-lg-4 col-md-6">
          {% include product-card.md product=product %}
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>

<div class="container my-5">
  <div class="row justify-content-center">
    <div class="col-lg-8">
      <h2 class="text-center mb-4">{{ page.about_title }}</h2>
      <div class="about-content">
        {{ content }}
      </div>
    </div>
  </div>
</div>
