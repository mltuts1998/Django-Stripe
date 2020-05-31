from django.shortcuts import render, redirect, reverse

# Create your views here.

import stripe as stripes
stripes.api_key = "pk_test_tkj9QAmsgb3rQkJMZH1iommg00WAdK86DL"



def index(request):
	return render(request, 'index.html')


def charge(request, *args, **kwargs):
	amount = 10
	if request.method == 'POST':
		print('Data:', request.POST)
		stripes.Customer.create(
			email=request.POST["email"],
			name=request.POST["name"]
 		)

	return redirect(reverse('strip:success', args=[amount]))

def success(request, args):
	amount = args
	return render(request, "success.html", {"amount":amount})