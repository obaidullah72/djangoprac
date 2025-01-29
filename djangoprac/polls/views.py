from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from .models import Question, Choice
from django.db import transaction



# Generic ListView for the index page
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last Ten published questions."""
        return Question.objects.order_by("-pub_date")[:10]


# Generic DetailView for displaying individual question details
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


# Generic DetailView for displaying results of a specific question
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# Vote handling logic

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Check if the user has already voted in the session
    if request.session.get(f"voted_{question_id}", False):
        # The user has already voted, they cannot vote again
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You have already voted.",
            },
        )

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Use atomic transaction to increment votes
        with transaction.atomic():
            selected_choice.votes = F("votes") + 1
            selected_choice.save()

        # Set a flag in the session to indicate the user has voted
        request.session[f"voted_{question_id}"] = True

        # Redirect to the results page
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
