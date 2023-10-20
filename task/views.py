from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def team_list(request) -> Response | None:
    #  Get all teams
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #  Create team
    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"OK": "Team has been successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, team_id) -> Response | None:
    try:

        # Get team by id
        team = Team.objects.get(pk=team_id)
        if request.method == 'GET':
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # if team by id is not exist
    except Team.DoesNotExist:
        return Response({"error": f"Team by id {team_id} is not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Update team by id
    if request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"OK": f"Team by id {team_id} is updated"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete team by id
    elif request.method == 'DELETE':
        team.delete()
        return Response({"OK": f"Team by id {team_id} is deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def people_list(request) -> Response | None:
    #  Get all people
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #  Create person
    elif request.method == 'POST':

        try:
            Team.objects.get(pk=request.data['team'])
        except Team.DoesNotExist:
            return Response(
                {"error": f"Team by id {request.data['team']} is not exist"},
                status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"OK": "Person has been successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def people_detail(request, person_id) -> Response | None:

    try:
        person: Person = Person.objects.get(pk=person_id)
    # if person by id is not exist
    except Person.DoesNotExist:
        return Response({"error": f"Team by id {person_id} is not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Get person by id
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    # Update person by id
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"OK": f"Team by id {person_id} is updated"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete team by id
    elif request.method == 'DELETE':
        person.delete()
        return Response({"OK": f"Person by id {person_id} is deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def team_people_list(request, team_id) -> Response | None:
    # Get all the people on the team id
    if request.method == 'GET':
        people = Person.objects.filter(team_id=team_id)
        if people:
            serializer = PersonSerializer(people, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Error": f"No people found for team with id {team_id}"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', 'POST'])
def team_people(request, person_id, team_id) -> Response | None:
    try:

        # Get team by id
        team = Team.objects.get(pk=team_id)
        if request.method == 'GET':
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # if team by id is not exist
    except Team.DoesNotExist:
        return Response({"error": f"Team by id {team_id} is not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id=person_id, team_id=team_id)
            person.team_id = None
            person.save()
            return Response(
                {"OK": f"Team by id {team_id} has been deleted from person with id {person_id}."},
                status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response(
                {"error": f"Person with id {person_id} in team {team_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        try:
            person = Person.objects.get(id=person_id)
            person.team_id = team_id
            person.save()
            return Response(
                {"OK": f"Team by id {team_id} has been successfully added to person by id {person_id}"},
                status=status.HTTP_201_CREATED)
        except Person.DoesNotExist:
            return Response(
                {"error": f"Person with id {person_id} in team {team_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND)
