from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt

import random
import requests
from myproject.secret import mall_id, client_id
# Create your views here.

topics = [
    {'id': 1, 'title':'rounting','body':'Routing is ..'},
    {'id': 2, 'title':'view','body':'view is ..'},
    {'id': 3, 'title':'Model','body':'model is ..'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id !=None:
        contextUI = f'''
        <li>
            <form action='/delete/' method='post'>
                <input type='hidden' name='id' value={id}>
                <input type='submit' value = 'delete'>
            </form>
        </li>
        <li><a href='/update/{id}'>update</a></li>
        '''
    ol = ''
    for topic in topics:
        ol+= f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href='/create'>create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''
def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django'''
    
    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == id:
            print(topic)
            article = f"<h2>{topic['title']}</h2>{topic['body']}"

    return HttpResponse(HTMLTemplate(article,id))

@csrf_exempt
def create(request):
    if request.method == 'GET':
        article = '''
        <form action='/create/' method='post' >
            <p><input type='text' name='title' placeholder = 'title'></p>
            <p><textarea name = 'body' placeholder='body'></textarea></p>
            <p><input type='submit'></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method =='POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":len(topics)+1,"title": title, "body": body}
        topics.append(newTopic)
        url = '/read/'+str(len(topics))
        print(topics)
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        print('id', id)
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics

        return redirect('/')


@csrf_exempt
def update(request,id):
    global topics
    if request.method =='GET':
        for topic in topics:
            selectedTopic = {
                'title':topic['title'],
                'body':topic['body']
            }
        article = f'''
        <form action='/update/{id}/' method='post' >
            <p><input type='text' name='title' placeholder = 'title' value={selectedTopic['title']}></p>
            <p><textarea name = 'body' placeholder='body'>{selectedTopic['body']}</textarea></p>
            <p><input type='submit'></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method =='POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == id:
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')

def test(request):
    
    url = "https://indians3.cafe24api.com/api/v2/products?brand_code=B000000A&price_min=1000"
    headers = {
        'Content-Type': "application/json",
        'X-Cafe24-Api-Version': "1",
        'X-Cafe24-Client-Id': "indians3"
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)

    return HttpResponse(response.text)