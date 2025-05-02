from django.shortcuts import render
from django.shortcuts import get_object_or_404

from clubs.models import Club
from faculty.models import Faculty
from faculty.scholar_api import get_or_cache_best_papers


def home(request):
    return render(request, 'home.html')

def faculty(request):
    facultys = Faculty.objects.all().order_by('sl')
    return render(request, 'faculty/faculty.html', {
        'facultys' : facultys
    })

def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    papers = get_or_cache_best_papers(faculty.google_scholar_url)
    return render(request, 'faculty/faculty_detail.html', {'faculty_profile': faculty, 'papers':papers})

def undergraduate(request):
    return render(request, 'hard_html/undergraduate.html')

def graduate(request):
    return render(request, 'hard_html/graduate.html')

def tuition(request):
    return render(request, 'hard_html/tuition.html')

def why_cse(request):
    return render(request, 'hard_html/why_cse.html')

def host(request):
    return render(request, 'hard_html/icpc_host.html')

def clubs(request):
    clubs = Club.objects.all()
    return render(request, 'hard_html/clubs.html', {"clubs": clubs})

def club_detail(request):
    return render(request, 'club_detail.html')

def gallery(request):
    return render(request, 'hard_html/gallery.html')

def error(request):
    return render(request, 'hard_html/errorPage.html')

def tester(request):
    return render(request, 'tester.html')

def research(request):
    facultys = Faculty.objects.all()  # Adjust this to match your model
    data = []
    for faculty in facultys:
        papers = get_or_cache_best_papers(faculty.google_scholar_url)
        data.append({
            'faculty': faculty,
            'papers': papers
        })
    return render(request, 'research.html', {'faculty_data': data})

