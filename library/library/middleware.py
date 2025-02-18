# 记录每个 API 请求的参数和耗时
import time
from django.utils.deprecation import MiddlewareMixin

class ApiTimeLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            print(f"API请求耗时：{duration}秒")
            with open('api_log.log', 'a', encoding='utf-8') as f:
                f.write(f"{request.path} 请求耗时：{duration}秒\n")
        return response