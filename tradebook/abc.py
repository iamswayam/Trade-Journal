# from nsetools import Nse

# index = ("nifty 50")
        
# mData = Nse().get_index_quote(index)
        
# name = mData['name']
# prc = mData['lastPrice']
# change = mData['change']
# pchange = mData['pChange']
# chart = mData['imgFileName']
        
# context = {'name': name, 'prc': prc, 'change':change, 'pchange': pchange, 'chart': chart}
        
# print(context['name'], ':-' , context['prc'])

x = []

i = "nifty bank"

x.append(i)

y = tuple(x)

print(y)






#home.html....
# <h1>Add Stock...</h1>
# <br/>

# <form action="{% url 'home' %}" class="form-inline my-2 my-lg-0" method="POST">
# 		{% csrf_token %}
#       <input class="form-control mr-sm-2" type="search" placeholder="Add To Portfolio" aria-label="Search" name="ticker">
#       <button class="btn btn-outline-secondary my-2 my-sm-0" type="submit">Add Stock</button>
#     </form>

# <br/><br/>

# <table class="table table-striped table-bordered table-hover">
#   <thead class="thead-dark">
#     <tr>
#       <th scope="col">Company Name</th>
#       <th scope="col">Stock Price</th>
#       <th scope="col">Previous Close</th>
#       <th scope="col">Market Cap</th>
#       <th scope="col">YTD Change</th>
#       <th scope="col">52Wk High</th>
#       <th scope="col">52Wk Low</th>
            
#     </tr>
#   </thead>
#   <tbody>
# {% if ticker %}

#   			{% for list_item in output %}
#   				<tr>
# 					<th scope="row">{{ list_item.companyName }}</th>
# 					<td>${{ list_item.lastPrice }}</td>
# 					<!-- <td>${{ list_item.previousClose }}</td>
# 					<td>${{ list_item.marketCap }}</td>
# 					<td>{{ list_item.ytdChange }}%</td>
# 					<td>${{ list_item.week52High }}</td>
# 					<td>${{ list_item.week52Low }}</td> -->
# 				</tr>
# 			{% endfor %}
			
#   </tbody>
# </table>
# {% endif %}

# <br/><br/>