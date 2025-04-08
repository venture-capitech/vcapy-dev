<!-- _includes/footer.md -->
<footer class="bg-light text-center text-lg-start mt-5">
    <div class="container p-4">
        <div class="row">
            <div class="col-lg-4 col-md-12 mb-4 mb-md-0">
                <h5 class="text-uppercase">{{ site.title }}</h5>
                <p>
                    Custom 3D printed products with innovative designs and quality materials.
                </p>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 mb-md-0">
                <h5 class="text-uppercase">Links</h5>
                <ul class="list-unstyled mb-0">
                    {% for item in site.data.navigation %}
                    <li>
                        <a href="{{ item.url | relative_url }}" class="text-dark">{{ item.title }}</a>
                    </li>
                    {% endfor %}
                    <li>
                        <a href="/privacy" class="text-dark">Privacy Policy</a>
                    </li>
                    <li>
                        <a href="/terms" class="text-dark">Terms of Service</a>
                    </li>
                </ul>
            </div>
            <div class="col-lg-4 col-md-6 mb-4 mb-md-0">
                <h5 class="text-uppercase">Contact</h5>
                <ul class="list-unstyled mb-0">
                    <li>
                        <a href="mailto:{{ site.contact_email }}" class="text-dark">
                            <i class="fas fa-envelope me-2"></i>{{ site.contact_email }}
                        </a>
                    </li>
                    <li>
                        <a href="https://instagram.com/{{ site.instagram_handle | remove: "@" }}" class="text-dark">
                            <i class="fab fa-instagram me-2"></i>{{ site.instagram_handle }}
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.05);">
        © 2025 {{ site.title }}. All rights reserved.
    </div>
</footer>