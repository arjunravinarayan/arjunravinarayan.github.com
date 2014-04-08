---
layout: page
group: navigation
---

<h3><a href="{{ site.url}}/archive/">Recent Posts</a></h3>
<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
