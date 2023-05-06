import aiohttp, asyncio, requests
from django.shortcuts import render
from django.http import JsonResponse
from fpl import FPL

# Create your views here.
class Fpl():
    async def main():
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            
            player = await fpl.get_player(player_id=275, return_json=True)
            return player

    def sessions():
        with requests.Session() as session:
            fpl = FPL(session)
            fpl.login(email="adeyusuf580@gmail.com", password="8LQCFwi$VXb%7.k")
            return fpl

def index(request):
    return render(request, "football/index.html")

def teams(request):
    fpl = Fpl.sessions()
    fpl.get_player(player_id=277, return_json=True)
    return JsonResponse(asyncio.run(Fpl.main()), safe=False)
