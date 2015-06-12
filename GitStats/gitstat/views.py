# External Libraries
import github as gthb
import pandas as pd

# Django imports
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

#plotly for plotting..
import plotly.plotly as py
from plotly.graph_objs import *

# Add city list and languages here. It will be reflected in the dashboard
city_list = ["Gurgaon", "Bangalore", "California", "Los Angeles","Montreal"]
languages = ['python','dotnet','javascript','scala','java']
years = [i for i in range(2008,2015)] #Years from 2000 to 2014
def homepage(request):
    """
    Renders the template at homepage!
    """
    global city_list, years, languages
    return render_to_response('index.html',{"city_list":city_list,
    	                                    "years":years,"languages":languages},
                                  context_instance=RequestContext(request))


# Plot 1 url: /bargraph/
@csrf_exempt
def bargraph(request):
    """
     Creates a plot for number of users in a particular region
     for a particular language, and returns an iframe of the graph
     plotted for the same, plotted using plotly. 
     It is a vertical bar graph.
    """
    

    if request.method == "POST":
    	global languages
    	gt = gthb.Github()       
    	print "1"
        city1 = request.POST["city1"]
        city2 = request.POST["city2"]
        counts1 = []
        counts2 = []
        print "2"
        for lang in languages:
            counts1.append( _number_of_users(gt, location=city1,language=lang))
            counts2.append(_number_of_users(gt, location=city2,language=lang))
        print "3"
        trace1 = Bar(x=languages, y = counts1, name=city1)
        trace2 = Bar(x=languages, y = counts2, name=city2)
        data = Data([trace1, trace2])       
        layout = Layout(barmode='group')
        print "4"
        fig = Figure(data=data, layout=layout)
        
        plot_url = py.plot(fig, file_name='barchart', auto_open=False)
        embed_url = plot_url + ".embed?height=400&width=550"
        print "5"
        return HttpResponse(embed_url)

# Plot 2 url: /scatter/
@csrf_exempt
def line(request):
    """
     Creates a pie chart of popularity of languages in a region
     and returns an iframe of the graph
     plotted for the same, plotted using plotly.
    """
    if request.method == "POST":
    	global years
    	global city_list
    	gt = gthb.Github()       
    	print "1"
        start_year = int(request.POST["year"])
        city = request.POST["city"]
        counts1 = []
        counts2 = []
        print "2"
        date_list = ["January","February","March","April","May","June","July","August",
                      "September","October","November", "December"]
        users_joined = []
        
        for j in range(1,13):
            _init_created = str(start_year) + str("-0"+str(j) if j<10 else "-"+ str(j)) + "-01"
            _created = _init_created + ".." + _init_created[:-2] + "28"
            print "created"
            print _created
            try:
                users_joined.append(_number_of_users_joined(gt, location=city, created=_created))
            except:
                break    
        l = len(users_joined)    
        print "3"
        trace = Scatter(
        	      x=date_list[:l],
                  y=users_joined,
                  mode='lines'
                )
        data = Data([trace])       
        layout = Layout(
                        title='Number of Users by create month',
                        xaxis=XAxis(
                           title='Month'
                        ),
                        yaxis=YAxis(
                        title='Number of users'
                        )
                    )

        print "4"
        fig = Figure(data=data, layout=layout)
        
        plot_url = py.plot(fig, file_name='linechart', auto_open=False)
        embed_url = plot_url + ".embed?height=400&width=550"
        print "5"
        return HttpResponse(embed_url)


# Plot 3 TOTHINK

def _number_of_users(gthb_object, location="Gurgaon", language="Python"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} language:{_language}".format(_location=location, _language=language)
     result = gthb_object.search_users(query)
     return result.totalCount

def _number_of_users_joined(gthb_object, location="Gurgaon", created="2012-01-01"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} created:{_created}".format(_location=location, _created=created)
     result = gthb_object.search_users(query)
     return result.totalCount


