{% extends "./base.html" %}
{% block content %}
{% if form %}
<form method='post'>
   {% csrf_token %}
   {{ form.as_p }}
   <input type="submit" value="submit" />
</form>
{% endif %}
{% endblock %}