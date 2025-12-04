from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.paginator import Paginator
from api.models import Feedback


class FeedBackView(APIView):
    def get(self,request):
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))

        # Step 2: Query your data
        records = Feedback.objects.all().order_by('-created_at').values(
                'id', 'name', 'email', 'feedback', 'rating', 'created_at'
            )
        formatted = [self.format_feedback(item) for item in records]

        # Step 3: Apply pagination
        paginator = Paginator(formatted, page_size)
        page_obj = paginator.get_page(page)

        # Step 4: Prepare JSON response
        return JsonResponse({
            "data": list(page_obj),  # Important: convert to list
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            }
        }, status=200)
    def post(self,request):
        print(request)
        return JsonResponse({'message':"Successfully created"},status =200)
    

    def format_feedback(self,item):
        return {
            **item,
            "created_at": item['created_at'].strftime("%d-%m-%Y")
        }