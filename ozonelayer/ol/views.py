from django.shortcuts import render
import json
def index(request):
    return render(request, 'index.html')

def crop(request):
    if request.method=="POST":
        crop = request.POST.get('email', '')
        vegetable_crops = {
            "adhra pradesh": ["Brinjal", "Chillies", "Okra", "Bottle Gourd"],
            "arunachal pradesh": ["Potato", "Tomato", "Maize", "Ginger"],
            "assam": ["Rice", "Mustard", "Sugarcane", "Banana"],
            "bihar": ["Potato", "Onion", "Cauliflower", "Cabbage"],
            "chhattisgarh": ["Rice", "Sorghum", "Maize", "Pulses"],
            "goa": ["Coconut", "Cashew", "Mango", "Pineapple"],
            "gujarat": ["Potato", "Cotton", "Groundnut", "Onion"],
            "haryana": ["Wheat", "Rice", "Sugarcane", "Maize"],
            "himachal Pradesh": ["Apple", "Potato", "Cabbage", "Carrot"],
            "jharkhand": ["Paddy", "Maize", "Sugarcane", "Mango"],
            "karnataka": ["Rice", "Sugarcane", "Banana", "Tomato"],
            "kerala": ["Coconut", "Rubber", "Pepper", "Tapioca"],
            "madhya Pradesh": ["Wheat", "Soybean", "Pulses", "Maize"],
            "maharashtra": ["Sugarcane", "Cotton", "Soybean", "Tomato"],
            "manipur": ["Rice", "Maize", "Pulses", "Potato"],
            "meghalaya": ["Rice", "Maize", "Potato", "Pineapple"],
            "mizoram": ["Rice", "Maize", "Potato", "Ginger"],
            "nagaland": ["Rice", "Maize", "Millets", "Pulses"],
            "odisha": ["Rice", "Pulses", "Groundnut", "Sugarcane"],
            "punjab": ["Wheat", "Rice", "Cotton", "Sugarcane"],
            "rajasthan": ["Wheat", "Barley", "Mustard", "Gram"],
            "sikkim": ["Rice", "Maize", "Potato", "Ginger"],
            "tamil Nadu": ["Rice", "Sugarcane", "Banana", "Coconut"],
            "telangana": ["Rice", "Cotton", "Sorghum", "Red Gram"],
            "tripura": ["Rice", "Jute", "Pulses", "Oilseeds"],
            "uttar pradesh": ["Rice", "Wheat", "Sugarcane", "Potato"],
            "uttarakhand": ["Rice", "Wheat", "Maize", "Millet"],
            "west bengal": ["Rice", "Jute", "Potato", "Sugarcane"],
            # Add more states and corresponding vegetables as needed
        }
        crop.lower()
        vegetable_crops[crop]

            updates.append({'text': vegetable_crops[crop]})
            response = json.dumps([updates], default=str)
            return HttpResponse(response)

    return render(request, 'crop.html')