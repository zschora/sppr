from django.shortcuts import render, redirect
from django.views.generic.base import View
import numpy as np
import pandas as pd
from .models import User, Artist
from scipy import sparse
from sklearn.preprocessing import normalize

# Create your views here.
class RandomArtistView(View):
  def get(self, request):
    artists = Artist.objects.order_by("?")[:10]
    return render(request, 'rate/rate.html', {'artist_list': artists})

class ResultView(View):
  def get(self, request):
    id_list = request.GET.getlist('id')
    artists = Artist.objects.filter(id__in=id_list)
    print(artists)
    return render(request, 'result/result.html', {'artist_list': artists})

class PredictView(View):
  def post(self, request):
    form = request.POST.dict()
    del form['csrfmiddlewaretoken']
    p = [(int(key), int(value)) for key, value in form.items()]
   
    interactions_df = pd.DataFrame(list(User.objects.all().values('User_id', 'Artist_id', 'Scrobbles')))
    title_dict = Artist.objects.all()
    new_i = max(interactions_df['User_id']) + 1
    for i, score in p:
      interactions_df.loc[len(interactions_df.index)] = [new_i, i, score*500]
    rows, r_pos = np.unique(interactions_df.values[:,0], return_inverse=True)
    cols, c_pos = np.unique(interactions_df.values[:,1], return_inverse=True)
    artists_sparse = sparse.csr_matrix((interactions_df.values[:,2], (r_pos, c_pos)))
    Pui = normalize(artists_sparse, norm='l2',axis=1)
    artists_sparse_transposed = artists_sparse.transpose(copy=True)
    Piu = normalize(artists_sparse_transposed, norm='l2', axis=1)
    similarity = Pui * Piu * Pui
    prev = [title_dict[i+1] for i in np.nonzero(artists_sparse[new_i-1])[1].tolist()]
    usim = [title_dict[i+1] for i in similarity[new_i-1].toarray().argsort()[0][-20:].tolist()]
    result = set(usim) - set(prev)
    url = '/result/?'
    for artist in result:
      url += f'id={artist.id}&'
    return redirect(url[:-1])