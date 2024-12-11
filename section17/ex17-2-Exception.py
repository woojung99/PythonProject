import traceback

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print(f'발생 예외 메세지 {e}')
    traceback.print_exc() # 에러 내용에 대해 자세히 보고 싶은 경우

    
