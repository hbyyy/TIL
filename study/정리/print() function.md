### print() function



```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

* print 함수에는 여러 인자가 들어갈 수 있다.  출력할 객체들(여러 개 가능) 외에는 키워드 인자를 사용하여 인자를 전달할 수 있다.
  1. sep
     - 기본값은 '  '(공백)이며, `object` 가 여러개 전달될 때 object 사이에 올 값을 정해준다
  2. end
     - 기본값은 '\n'(개행문자)이며, `object`의 끝에 들어갈 값을 정해준다.

