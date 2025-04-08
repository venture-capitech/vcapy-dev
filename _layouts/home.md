<!-- _layouts/home.html -->
---
layout: default
---

<div class="hero-section">
  <div class="hero-content">
    <h1>{{ page.hero_title }}</h1>
    <p>{{ page.hero_subtitle }}</p>
    <a href="{{ page.hero_button_url }}" class="cta-button">{{ page.hero_button_text }}</a>
  </div>
</div>

<div class="featured-products">
  <h2>{{ page.featured_section_title }}</h2>
  <div class="products-grid">
    {% for product_id in page.featured_products %}
      {% assign product = site.products | where: "slug", product_id | first %}
      {% if product %}
        {% include product-card.md product=product %}
      {% endif %}
    {% endfor %}
  </div>
</div>

<div class="about-section">
  <h2>{{ page.about_title }}</h2>
  <div class="about-content">
    {{ content }}
  </div>
</div>

{% if page.show_testimonials %}
<div class="testimonials-section">
  <h2>{{ page.testimonials_title }}</h2>
  <div class="testimonials-grid">
    {% for testimonial in site.data.testimonials limit:page.testimonials_count %}
      {% include testimonial-card.md testimonial=testimonial %}
    {% endfor %}
  </div>
</div>
{% endif %}