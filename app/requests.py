import urllib.request,json
from .models import Quote

# Getting the quote base url
source_base_url = None

def configure_request(app):
  global source_base_url
  
  source_base_url = app.config['QUOTE_API_BASE_URL']
  
def get_random_quote():
  '''
  Function that gets the json response to the url request
  '''
  get_quote_source_url = source_base_url.format()
  
  with urllib.request.urlopen(get_quote_source_url) as url:
    get_quote_source_data = url.read()
    get_quote_source_response = json.loads(get_quote_source_data)
    
    quote_source_results = None
    
    if get_quote_source_response['id']:
      quote_result_list = get_quote_source_response
      quote_source_results = process_source_results(quote_result_list)
      
  return quote_source_results

def process_source_results(quote_list):
  '''
  Function that processes the quote source results and transforms them into a list of objects.
  Args:
    quote_list: A list of quote objects
  Returns:
    quote_source_results: A list of quote objects
  '''
  quote_source_results = []

  id = quote_list.get('id')
  author = quote_list.get('author')
  quote = quote_list.get('quote')
    
  if id:
    quote_object = Quote(id, author, quote)
    quote_source_results.append(quote_object)
  
  return quote_source_results