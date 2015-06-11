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

def homepage(request):
    """
    Renders the template at homepage!
    """
    global city_list
    return render_to_response('index.html',{"city_list":city_list},
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
    if request.method == "GET":
    	return HttpResponse("HEYA")

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
def scatter(request):
     """
     Creates a pie chart of popularity of languages in a region
     and returns an iframe of the graph
     plotted for the same, plotted using plotly.
     """
     if request.method == "POST":
         iframe = '<iframe></iframe>'
         return HttpResponse(iframe)


# Plot 3 TOTHINK
# Plot 4 TOTHINK
   
def _number_of_users(gthb_object, location="Gurgaon", language="Python"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} language:{_language}".format(_location=location, _language=language)
     result = gthb_object.search_users(query)
     return result.totalCount



