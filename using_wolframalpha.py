import wolframalpha

input=input("Q: ")
try:
    app_id='your app-id'
    client=wolframalpha.Client(app_id)
    res=client.query(input)
    answer=next(res.results).text
    print(answer)
except:
    print(wikipedia.summary(input))
