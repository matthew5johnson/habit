from django.shortcuts import render
from .models import Emotion, Color
import random

# # Create your views here.
def home(request):
	hexa = Color.objects.all()
	colorone = Color.objects.get(color='yellow')

	test_list = [1, 2, 3, 4]
	randomnumber = random.sample(test_list, 3)

	emotionsamount = len(Emotion.objects.all())
	test_sample = random.sample(range(1, emotionsamount), 6)

	positive_emotion_pks = random.sample(range(1, len(Emotion.objects.filter(positive=1))), 3)
	positive_emotion_1 = positive_emotion_pks[0]
	# positive_emotion_1 = Emotion.objects.filter(pk=positive_emotions_pks[0])
	positive_emotion_name_1 = Emotion.objects.get(pk=positive_emotion_1)

	positive_emotions_list = []
	for i in range(0,3):
		positive_emotions_list.append(Emotion.objects.get(pk=positive_emotion_pks[i]))

	return render(request, 'app/home.html', {'colors': hexa, 'colorone': colorone, 'randomnumber': randomnumber, 'emotions': emotionsamount, 'test_sample': test_sample, 'positive_emotion_1': positive_emotion_1, 'positive_emotion_name_1': positive_emotion_name_1, 'positive_emotions_list': positive_emotions_list})

def version1(request):
	all_negatives = Emotion.objects.filter(negative=1).values('emotion')
	list_negatives = []
	for i in range(0, len(all_negatives)):
		list_negatives.append(all_negatives[i]['emotion'])

	all_positives = Emotion.objects.filter(positive=1).values('emotion')
	list_positives = []
	for i in range(0, len(all_positives)):
		list_positives.append(all_positives[i]['emotion'])

	take_3_negatives = random.sample(list_negatives, 3)
	take_3_positives = random.sample(list_positives, 3)
	all_6_emotions = take_3_positives + take_3_negatives

	all_colors = Color.objects.all().values('hexa')
	list_colors = []
	for i in range(0, len(all_colors)):
		list_colors.append(all_colors[i]['hexa'])

	take_6_colors = random.sample(list_colors, 6) 



	return render(request, 'app/version1.html', {
		'emotion_one': all_6_emotions[0],
		'emotion_two': all_6_emotions[1],
		'emotion_three': all_6_emotions[2], 
		'emotion_four': all_6_emotions[3], 
		'emotion_five': all_6_emotions[4], 
		'emotion_six': all_6_emotions[5], 
		'color_name_one': take_6_colors[0],
		'color_name_two': take_6_colors[1],
		'color_name_three': take_6_colors[2],
		'color_name_four': take_6_colors[3],
		'color_name_five': take_6_colors[4],
		'color_name_six': take_6_colors[5],
		})

def version2(request):
	all_negatives = Emotion.objects.filter(negative=1).values('emotion')
	list_negatives = []
	for i in range(0, len(all_negatives)):
		list_negatives.append(all_negatives[i]['emotion'])

	all_positives = Emotion.objects.filter(positive=1).values('emotion')
	list_positives = []
	for i in range(0, len(all_positives)):
		list_positives.append(all_positives[i]['emotion'])

	take_3_negatives = random.sample(list_negatives, 3)
	take_3_positives = random.sample(list_positives, 3)
	all_6_emotions = take_3_positives + take_3_negatives

	all_colors = Color.objects.all().values('hexa')
	list_colors = []
	for i in range(0, len(all_colors)):
		list_colors.append(all_colors[i]['hexa'])

	take_6_colors = random.sample(list_colors, 6) 



	return render(request, 'app/version2.html', {
		'emotion_one': all_6_emotions[0],
		'emotion_two': all_6_emotions[1],
		'emotion_three': all_6_emotions[2], 
		'emotion_four': all_6_emotions[3], 
		'emotion_five': all_6_emotions[4], 
		'emotion_six': all_6_emotions[5], 
		'color_name_one': take_6_colors[0],
		'color_name_two': take_6_colors[1],
		'color_name_three': take_6_colors[2],
		'color_name_four': take_6_colors[3],
		'color_name_five': take_6_colors[4],
		'color_name_six': take_6_colors[5],
		})


def emotions(request):
	all_negatives = Emotion.objects.filter(negative=1).values('emotion')
	list_negatives = []
	for i in range(0, len(all_negatives)):
		list_negatives.append(all_negatives[i]['emotion'])

	all_positives = Emotion.objects.filter(positive=1).values('emotion')
	list_positives = []
	for i in range(0, len(all_positives)):
		list_positives.append(all_positives[i]['emotion'])

	take_3_negatives = random.sample(list_negatives, 3)
	take_3_positives = random.sample(list_positives, 3)
	all_6_emotions = take_3_positives + take_3_negatives

	all_colors = Color.objects.all().values('hexa')
	list_colors = []
	for i in range(0, len(all_colors)):
		list_colors.append(all_colors[i]['hexa'])

	take_6_colors = random.sample(list_colors, 6) 



	return render(request, 'app/version2specific.html', {
		'emotion_one': all_6_emotions[0],
		'emotion_two': all_6_emotions[1],
		'emotion_three': all_6_emotions[2], 
		'emotion_four': all_6_emotions[3], 
		'emotion_five': all_6_emotions[4], 
		'emotion_six': all_6_emotions[5], 
		'color_name_one': take_6_colors[0],
		'color_name_two': take_6_colors[1],
		'color_name_three': take_6_colors[2],
		'color_name_four': take_6_colors[3],
		'color_name_five': take_6_colors[4],
		'color_name_six': take_6_colors[5],
		})

def colors(request):
	all_negatives = Emotion.objects.filter(negative=1).values('emotion')
	list_negatives = []
	for i in range(0, len(all_negatives)):
		list_negatives.append(all_negatives[i]['emotion'])

	all_positives = Emotion.objects.filter(positive=1).values('emotion')
	list_positives = []
	for i in range(0, len(all_positives)):
		list_positives.append(all_positives[i]['emotion'])

	take_3_negatives = random.sample(list_negatives, 3)
	take_3_positives = random.sample(list_positives, 3)
	all_6_emotions = take_3_positives + take_3_negatives

	all_colors = Color.objects.all().values('hexa')
	list_colors = []
	for i in range(0, len(all_colors)):
		list_colors.append(all_colors[i]['hexa'])

	take_6_colors = random.sample(list_colors, 6) 



	return render(request, 'app/version2specific.html', {
		'emotion_one': all_6_emotions[0],
		'emotion_two': all_6_emotions[1],
		'emotion_three': all_6_emotions[2], 
		'emotion_four': all_6_emotions[3], 
		'emotion_five': all_6_emotions[4], 
		'emotion_six': all_6_emotions[5], 
		'color_name_one': take_6_colors[0],
		'color_name_two': take_6_colors[1],
		'color_name_three': take_6_colors[2],
		'color_name_four': take_6_colors[3],
		'color_name_five': take_6_colors[4],
		'color_name_six': take_6_colors[5],
		})