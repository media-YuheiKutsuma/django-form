from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm # 追加

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"
    success_url = reverse_lazy('contact_result')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "NEXTGATE LiSMOtech"        
        context["form"] = ContactForm() # 追加
        return context

    def post(self, request, *args, **kwargs):
        context = {
            'message': "送信OK",
            'name': request.POST['name'],
            'email': request.POST['email']
        }
        return render(request, 'confirmation.html', context)
    
    # 初期変数定義
    # def __init__(self):
    #     self.params = {"Message":"情報を入力してください。",
    #                    "form":forms.Contact_Form(),
    #                    }

    # GET時の処理を記載
    #def get(self,request):
    #    return render(request, "App_Folder_HTML/formpage.html",context=self.params)

    # POST時の処理を記載
    # def post(self,request):
    #     if request.method == "POST":
    #         self.params["form"] = forms.Contact_Form(request.POST)
            
    #         # フォーム入力が有効な場合
    #         if self.params["form"].is_valid():
    #             self.params["Message"] = "入力情報が送信されました。"

    #     return render(request, "App_Folder_HTML/formpage.html",context=self.params)    