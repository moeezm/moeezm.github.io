{% include mathjax.html %}
# Test
## Test

We have an inline equation: \\(f(x) = x^2\\)
and a display equation: \$\$f(x) = x^3\$\$
display: $$$f(x) = x$$$
and another display equation: \\[f(x) = x^4\\]

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{post.title}}</a>
  </li>
  {% endfor %}
</ul>
