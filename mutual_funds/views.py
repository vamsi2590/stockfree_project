from django.shortcuts import render

# Home page view for mutual funds
def index(request):
    return render(request, 'mutual_funds/index.html')  # Correct template path
import requests

# Function to fetch real-time mutual fund data from Alpha Vantage API
def fetch_real_time_data(symbol):
    api_key = 'L5EJBHKBH584U5XH'  # Replace with your actual API key
    base_url = 'https://www.alphavantage.co/query'

    # Endpoint for daily time series data (or other relevant endpoint for mutual funds)
    url = f"{base_url}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if 'Time Series (Daily)' in data:
        return data['Time Series (Daily)']
    else:
        return None
from django.shortcuts import render
from .utils import fetch_real_time_data

def analyze_fund_view(request):
    # Retrieve mutual fund data based on the query parameter (e.g., symbol)
    symbol = request.GET.get('symbol', '')
    if symbol:
        data = fetch_real_time_data(symbol)
    else:
        data = None

    return render(request, 'mutual_funds/analyze.html', {'data': data, 'symbol': symbol})

# views.py
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from django.shortcuts import render

# views.py
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from django.shortcuts import render

def fund_performance_heatmap(request):
    # Get the mutual fund symbol from the URL parameter (e.g., symbol=IXUS)
    symbol = request.GET.get('symbol', 'IXUS')  # Default to IXUS if not provided

    # Fetch the mutual fund data from Yahoo Finance (historical data for 5 days)
    fund = yf.Ticker(symbol)
    data = fund.history(period='5d')  # '5d' for the last 5 days of data

    # Prepare data (open, high, low, close, volume)
    df = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    # Create a heatmap for the data
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.transpose(), annot=True, cmap="YlGnBu", cbar=True, linewidths=0.5)

    # Save the heatmap as an image in a static folder
    heatmap_path = "mutual_funds/static/mutual_funds/heatmap.png"
    plt.title(f"Performance Heat Map for {symbol}")
    plt.savefig(heatmap_path)
    plt.close()

    # Return the heatmap image path to the template
    return render(request, 'mutual_funds/heatmap.html', {'symbol': symbol, 'data': data})

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'mutual_funds/home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')




    return render (request,'mutual_funds/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'mutual_funds/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
