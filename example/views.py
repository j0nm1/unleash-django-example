from django.http import HttpResponse
from UnleashClient import UnleashClient

client = UnleashClient("http://unleash:4242/api", "My Program")
client.initialize_client()

def index(request):
    if client.is_enabled("test"):
        return HttpResponse("<h1>Test enabled</h1>")
    return HttpResponse("<h1>Test disabled</h1>")