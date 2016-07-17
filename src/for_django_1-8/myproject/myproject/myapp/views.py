# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
import os,inspect

def list(request):
    txt=str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    txt=txt.replace("/myproject/myapp","/media/")
    txt=txt.replace(" ","")
     
    APIkey="###############################" #Give your HPE Haven on Demand API Key 
 	    
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            docfile=request.FILES['docfile']
            
            txt=txt+str(docfile)
            import requests
            url = 'https://api.havenondemand.com/1/api/async/recognizespeech/v1'.format('recognizespeech')
            files = {'file': open(str(txt),'rb')}
            while True:
              r = requests.post(url,data={"apikey":str(APIkey)}, files=files)
              k= r.json()
              try:
            
               jobID= k["jobID"]
               url1="https://api.havenondemand.com/1/job/result/"+jobID
               while True:
                p=requests.post(url1,data={'apikey':str(APIkey)},files=files)
                res=p.json()

                try:
                  content= res["actions"][0]["result"]["document"][0]["content"]
                  
                  d=str(content)

                  urlS='https://api.havenondemand.com/1/api/async/analyzesentiment/v1'
                  files1={'file':d}
                  a= requests.post(urlS,data={"apikey":str(APIkey)},files=files1)
                  l=a.json()
                  jobIDS=l["jobID"]
                  url1S="https://api.havenondemand.com/1/job/result/"+jobIDS
                  pS=requests.post(url1S,data={'apikey':str(APIkey)},files=files1)
                  res1=pS.json()
                  final=(res1["actions"][0]["result"]["aggregate"]["score"])
                  finalp=str(final*100)
                  result1=res1["actions"][0]["result"]["aggregate"]["sentiment"]
                  
                    
                  from django.contrib.staticfiles.templatetags.staticfiles import static

                  url = static('css/bootstrap.css')
                  url1=static('file.txt')
                  y=str(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
                  y=y.replace("/myproject/myapp","/static_in_pro/our_static/file.txt")
                  y=y.replace(" ","")
                  f=open(str(y),'w+')
                  f.write(content)
                  f.close()
                  ans=str("""
                  <!DOCTYPE html>
                      <html lang="en">
                      <head>
                          <meta charset="utf-8">
                          <meta http-equiv="X-UA-Compatible" content="IE=edge">
                          <meta name="viewport" content="width=device-width, initial-scale=1">
                          <title>Sentilysis</title>

                          <!-- Bootstrap core CSS -->
                          <link href="""+url+""" rel="stylesheet" type="text/css">
                          <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>
                          <script src="https://cdn.rawgit.com/aterrien/jQuery-Knob/master/dist/jquery.knob.min.js"></script>
                          <script type="text/javascript" src="http://yourjavascript.com/36616422911/excanvas.js"></script>
                      </head>
                      <body>
                        <div class="container">
                          <div class="header clearfix">
                            <nav>
                            </nav>
                            <h3 class="text-muted" style="line-height: 40px;">Sentilysis</h3>
                          </div>

                          <div class="jumbotron" style="text-align:center">
                            <div class="row"><h1 style="text-align:center">Sentilysis</h1></div>
                            <div class="row" style="text-align:center">
                                <p style="font-size:20px">Result:"""+result1+"""</p>
                            </div>
                            <div class="row" style="text-align:center">
                                <input type="text" class="dial" value="""+finalp+""" data-min="-100" data-max="100"  ></div> Download the audio file text :<a href="""+url1+""" download="audiotext">
                                <input type="button" value="download" style="margin-top:25px;" ></button></a>
                            </div>
                            <script>
                                $(function() {
                                  $(".dial").knob();
                                });
                            </script>
                            <footer class="footer">
                              <p>&copy; 2016 Deep Red Ink Consulting Pvt. Ltd.</p>
                            </footer>
                          </div> <!-- /container -->
                      </body>
                  </html>""")
                  return HttpResponse(ans)
                  break
                except:
                  continue
              except:
                 continue
            #HPE API
			
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
        else:
            form = DocumentForm()  # A empty, unbound form
        
        # Load documents for the list page
        documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )