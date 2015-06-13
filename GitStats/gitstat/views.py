# External Libraries
import github as gthb
import pandas as pd
import sys

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

# Views
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
        city1 = request.POST["city1"]
        city2 = request.POST["city2"]
        counts1 = []
        counts2 = []

        for lang in languages:
            counts1.append( _number_of_users(gt, location=city1,language=lang))
            counts2.append(_number_of_users(gt, location=city2,language=lang))

        trace1 = Bar(x=languages, y = counts1, name=city1)
        trace2 = Bar(x=languages, y = counts2, name=city2)
        data = Data([trace1, trace2])       
        layout = Layout(title="Language Popularity",barmode='group')
        fig = Figure(data=data, layout=layout)
        
        plot_url = py.plot(fig, file_name='barchart', auto_open=False)
        embed_url = plot_url + ".embed?height=400&width=550"
        return HttpResponse(embed_url)

# Plot 2 url: /line/
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
    	start_year = int(request.POST["year"])
        city = request.POST["city"]
        obj = request.POST["object"]
        
        date_list = ["January","February","March","April","May","June","July","August",
                      "September","October","November", "December"]
        
        y = []

        for j in range(1,13):
            _init_created = str(start_year) + str("-0"+str(j) if j<10 else "-"+ str(j)) + "-01"
            _created = _init_created + ".." + _init_created[:-2] + "28"

            try:
            	if obj=="Users":
            	    y.append(_number_of_users_joined(gt, location=city, created=_created))

                elif obj=="Repositories":
                    y.append(_number_of_repo_added(gt, location=city, created=_created))

                else:
                    y.append(_number_of_issues_added(gt, location=city, created=_created))

            except:
            	print sys.exc_info()
                break    

        l = len(y)
        trace1 = Scatter(
        	      x=date_list[:l],
                  y=y,
                  mode='lines',
                  name=obj
                )
        
        data = Data([trace1])       
        layout = Layout(
                        title='New ' + obj + ' Added on Github',
                        xaxis=XAxis(
                           title='Month'
                        ),
                        yaxis=YAxis(
                        title='Number of ' + obj
                        )
                    )

        fig = Figure(data=data, layout=layout)
        
        plot_url = py.plot(fig, file_name='linechart', auto_open=False)
        embed_url = plot_url + ".embed?height=400&width=550"
        return HttpResponse(embed_url)

def _number_of_users(gthb_object, location="Gurgaon", language="Python"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} language:{_language}".format(_location=location, _language=language)
     result = gthb_object.search_users(query)
     print result.totalCount
     return result.totalCount

def _number_of_users_joined(gthb_object, location="Gurgaon", created="2012-01-01"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} created:{_created}".format(_location=location, _created=created)
     result = gthb_object.search_users(query)
     count = result.totalCount
     print count
     return count

def _number_of_repo_added(gthb_object, location="Gurgaon", created="2012-01-01"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} created:{_created}".format(_location=location, _created=created)
     print "query"
     print query
     result = gthb_object.search_repositories(query)
     count = result.totalCount
     print count
     return count

def _number_of_issues_added(gthb_object, location="Gurgaon", created="2012-01-01"):
     """
     Search for users for a particular language in a particular region.
     Returns count for the same
     """
     query="location:{_location} created:{_created} is:open".format(_location=location, _created=created)
     print "query"
     print query
     result = gthb_object.search_issues(query)
     print "result:"
     count = result.totalCount
     print count
     return count


