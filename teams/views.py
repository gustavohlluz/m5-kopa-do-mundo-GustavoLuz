from django.forms import model_to_dict
from rest_framework.views import APIView, Request, Response, status
from teams.models import Team
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError

class TeamView(APIView):

    def post(self, request: Request) -> Response:
        data = request.data
        try:
            data_processing(data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)

        create_team = Team.objects.create(**data)
        team_dict = model_to_dict(create_team)
        return Response(team_dict, status.HTTP_201_CREATED)


    def get(self, request: Request) -> Response:
        teams = [
            model_to_dict(team) for team in Team.objects.all()
        ]
        return Response(teams, status.HTTP_200_OK)
    


class TeamDetailView(APIView):
    ...



