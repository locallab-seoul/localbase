from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Spaces

# Create your views here.
def index(request):
    # all_spaces = Spaces.objects.all().order_by('-id')

    url_parameter = request.GET.get("q", None)  # request에서 query 값을 인식한다는 뜻이다.
    # 중요한 건 여깁니다. “q”는 query의 약자로 사용자가 질문한 값을 여기서 get하겠다는 의미
    if url_parameter:  # 사용자가 입력한 query 값이 있다면,
        results = Spaces.objects.filter(title__contains=url_parameter)
    else:
        results = Spaces.objects.all().order_by('-id')  # 없으면 저장된 객체값을 모두 보여달라는 뜻
    
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  # 요청 자체가 AJAX라면,
        html = render_to_string(  # 결과값을 부분만 보여주는 HTML 렌더링
            "search_result.html", {"spaces": results})
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'index.html', {
        'spaces': results,
    })