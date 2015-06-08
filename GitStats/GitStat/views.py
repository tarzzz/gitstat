# External Libraries
import PyGithub as gthb
import pandas as pd

# Django imports
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def homepage():
  pass


# Plot 1 url: /bargraph/
def users_region_language_plot(request):
   """
   Creates a plot for number of users in a particular region
   for a particular language, and returns an iframe of the graph
   plotted for the same, plotted using plotly. 
   It is a vertical bar graph.
   """
   if request.method == "POST":
   # Get request params, two cities
   # Get data using gthb
   # Plot data, create iframe and return iframe as HttpResponse.
       iframe = '<iframe></iframe>'
       return HttpResponse(iframe)

# Plot 2 url: /piechart/
def region_language_plot(request):
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
   query="location: {_location} language:{_language}".format(_location=location, _language=language)
   result = gthb_object.users_search(query)
   return result.count



