import json
import requests

posts = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")

comments = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")

posts_response = posts.json()
comments_response = comments.json()


def combine_comment(comments,posts):
    l=[]
    for i in posts:
        k =0
        a ={}
        b =[]
        comment = []
        for j in comments:
            if i.get('id') == j.get('postId'):
                k += 1
                a['id'] = i.get('id')
                a['title'] = i.get('title')
                b.append({'id':j.get('id'),'body':j.get('body')})
            else:
                a['id'] = i.get('id')
                a['title'] = i.get('title')
            if b:
                a['comment'] = b
        l.append(a)
    return json.dumps(l)
    
result = combine_comment(comments=comments_response,posts=posts_response)

print(result)












