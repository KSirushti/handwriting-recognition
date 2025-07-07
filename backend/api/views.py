import os
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from inference_sdk import InferenceHTTPClient
from .serializers import CorrectionSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Initialize Roboflow client
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="km1lBlePpnFiHGkxqpRq"
)

@api_view(['POST'])
@parser_classes([MultiPartParser])
def predict_character(request):
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No image file provided'}, status=400)

    image = request.FILES['image']

    # Save the uploaded image temporarily
    temp_path = f"temp_{image.name}"
    with open(temp_path, 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    try:
        # Run prediction
        result = client.run_workflow(
            workspace_name="siru",              # 👈 Use your actual workspace
            workflow_id="active-learning",     # 👈 Use your actual workflow ID
            images={"image": temp_path},
            use_cache=True
        )

        # Clean up temp file
        os.remove(temp_path)

        # Return predictions
        return JsonResponse(result)

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def submit_correction(request):
    serializer = CorrectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Correction saved'}, status=201)
    return JsonResponse(serializer.errors, status=400)

