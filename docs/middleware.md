# 中间件

## 请求中间件
通过在视图函数处理请求前调用用户自定义处理函数，以修改请求对象。
```
@app.before_request
def process_request(request):
    return request
```

## 响应中间件
通过在视图函数处理请求后调用用户自定义处理函数，以修改响应对象。
```
@app.after_request
def process_request(request):
    return request
```