"""Imagine you're building an agent that routes queries. Take a user question as a string. If it contains the
word "math" or "calculate", print "Route: calculator tool". If it contains "search" or "latest", print "Route:
web search tool". If it contains "explain" or "what is", print "Route: LLM direct". Otherwise print "Route:
default".
This is the exact pattern inside every agent router
"""


query = input("enter your query :")

if "math" in query or "calculate" in query:
    print("Route: calculator tool")

elif "search" in query or "latest" in query:
    print("Route: web search tool")

elif "explain" in query or "what is" in query:
    print("Route:LLM direct")

else:
    print("route:default")  