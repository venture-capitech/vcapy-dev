<!-- _includes/navigation.md -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{{ '/' | relative_url }}">{{ site.title }}</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                {% for item in site.data.navigation %}
                <li class="nav-item">
                    <a class="nav-link" href="{{ item.url | relative_url }}">{{ item.title }}</a>
                </li>
                {% endfor %}
            </ul>
        </div>
    </div>
</nav>