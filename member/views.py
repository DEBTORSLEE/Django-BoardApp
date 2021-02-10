from django.shortcuts import render,get_object_or_404
from member.models import Member
# Create your views here.
def index(request):
    member_list = Member.objects.all().order_by('-wdate')[:5]
    context = {'member_list':member_list}
    return render(request,'member/index.html',context)
    
def detail(request, id):
    member = get_object_or_404(Member,pk=id)
    context = {'member':member}
    return render(request,'member/detail.html',{'member':member})