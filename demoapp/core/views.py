import os
import time
import jwt
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from .models import Contact

def index(request):
    contacts = Contact.objects.order_by("-created_at")[:50]
    return render(request, "core/index.html", {"contacts": contacts})

def submit_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/success.html")
    else:
        form = ContactForm()
    return render(request, "core/index.html", {"form": form, "contacts": Contact.objects.order_by("-created_at")[:50]})

# --- Metabase Embedding helper ---
def generate_metabase_signed_url(resource, params=None, expiration_seconds=60*5):
    """
    resource: dict like {"dashboard": 3} or {"card": 12}
    params: dict of params to pass to Metabase
    """
    METABASE_SITE_URL = os.getenv("METABASE_SITE_URL")
    METABASE_SECRET = os.getenv("METABASE_SECRET_KEY")
    if not (METABASE_SITE_URL and METABASE_SECRET):
        raise RuntimeError("Metabase settings not configured (METABASE_SITE_URL, METABASE_SECRET_KEY)")

    payload = {
        "resource": resource,
        "params": params or {},
        "exp": int(time.time()) + expiration_seconds,
        "iat": int(time.time()),
    }
    token = jwt.encode(payload, METABASE_SECRET, algorithm="HS256")
    # Construct the embed URL
    # Example: https://metabase.example.com/embed/dashboard/<token>#bordered=true&titled=true
    embed_path = ""
    if "dashboard" in resource:
        embed_path = f"/embed/dashboard/{token}"
    elif "card" in resource:
        embed_path = f"/embed/card/{token}"
    else:
        raise ValueError("Resource must be 'dashboard' or 'card'")

    return METABASE_SITE_URL.rstrip("/") + embed_path

def metabase_view(request):
    # Example: embed dashboard id 2
    try:
        embed_url = generate_metabase_signed_url({"dashboard": int(os.getenv("METABASE_DASHBOARD_ID", "2"))})
    except Exception as e:
        embed_url = None
        error = str(e)
    else:
        error = None
    return render(request, "core/metabase_embed.html", {"embed_url": embed_url, "error": error})
