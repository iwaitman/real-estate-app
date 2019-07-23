from django.shortcuts import render
from listings.models import listing

# # Create your views here.


def index(request):
	homes = listing.objects.order_by('-list_date').filter(is_published=True)
	context = {
		'listings': homes
	}
	return render(request, 'listings/listings.html', context)


def listing_detail(request, id):
	return render(request, 'listings/listing.html')


def search(request):
	return render(request, 'listings/search.html')
	