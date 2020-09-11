import wolframalpha

input=input("Q: ")
try:
    app_id='GAGHGV-76KGJTLV2L'
    client=wolframalpha.Client(app_id)
    res=client.query(input)
    answer=next(res.results).text
    print(answer)
except:
    print(wikipedia.summary(input))
