from disqusapi import DisqusAPI

print(DisqusAPI)

disqus = DisqusAPI(secret_key='anoAm8odSyHKdcrDlnRZWsfPpof4MKBwbY3XwLwMktYWyQOmgq7hwLumcJ7h4nCx',
                    public_key='nl55taKAfLJah7i8EaglOrFEoifCONO9SwOno5DiNanv0FPXwlxufjQ7DIP3drhc')

for result in disqus.get('trends.listThreads', method="GET"):
    print (result)