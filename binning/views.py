from django.shortcuts import render
import pandas as pd
import time
# Create your views here.
def index(request):
    df = pd.DataFrame([[1, 2], [3, 4]], columns = ["a", "b"])
    context = {"df": df}
    return render(request, "index.html", context)


def binning(request):
    time.sleep(5)
    print(request.GET["channel_id"])
    df = pd.DataFrame([[1, 2], [3, 4]], columns = ["c", "d"])
    context = {"df": df}
    return render(request, "df.html", context)

def vintage(request):
    df = pd.DataFrame([[1, 2], [3, 4]], columns = ["c", "d"])
    context = {"df": df}
    return render(request, "df.html", context)

def test_crontab():
    print("gg")
