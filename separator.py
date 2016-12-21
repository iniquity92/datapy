import re
import pickle 

def return_watch_brand_price_list(tow,brand):
    tiny_dict = {};
    keys = ''
    df = open(tow+'/'+brand+'/dict.pkl','rb')
    d = pickle.load(df)
    D = d[brand][0]
    keys = D.keys()
    for key in keys:
        tiny_dict[D[key]['id']] = D[key]['price']
    
    df.close() 
    return tiny_dict   
        
    
if __name__=='__main__':
    all_watch = {}
    gem_watch = {}

    folders = open('folders.txt','r')

    for folder in folders:
        tow,brand = re.findall(r'^(\w+)\/(\w+)',folder)[0]
        if tow=='watches':
            all_watch[brand]=return_watch_brand_price_list(tow,brand)
        elif tow=='pstones':
            gem_watch[brand]=return_watch_brand_price_list(tow,brand)

    
    aw = open('all_watch.pkl','wb')    
    pickle.dump(all_watch,aw)
    aw.close()
    gw = open('gem_watch.pkl','wb')
    pickle.dump(gem_watch,gw)
    gw.close()
 
		
