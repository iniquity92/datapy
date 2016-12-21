import pickle
import statistics

def isolator(aD,gD):
    woD = {}
    for key in aD.keys():
        if key not in gD.keys():
            woD[key] = aD[key]
        else:
            continue
    return woD

def list_builder(woD,gD):
    keys_wo = woD.keys()
    keys_gems = gD.keys()
    woLs = []
    gLs = []
    for key in keys_wo:
        woLs.append(woD[key])

    for key in keys_gems:
        gLs.append(gD[key])

    return (woLs,gLs)

def write_to_file(file_name,L):
    output = open(file_name,'a')
    output.write(','.join(L))
    output.write('\n')
    output.close()

def write_avg_csv_line(brand,woLs,gLs):
       
    n_watches_wo_gems = len(woLs)
    n_watches_w_gems = len(gLs)

    avg_wo_gems = statistics.mean(woLs)
    avg_w_gems = statistics.mean(gLs)
    
    L = [brand,str(avg_wo_gems),str(avg_w_gems),str(n_watches_wo_gems),str(n_watches_w_gems)]
    write_to_file('avg.csv',L)
    
def write_median_csv_line(brand,woLs,gLs):
    median_wo_gems = statistics.median(woLs)
    median_w_gems = statistics.median(gLs)
    
    L = [brand,str(median_wo_gems),str(median_w_gems)]
    write_to_file('median.csv',L)

def write_variance_csv_line(brand,woLs,gLs):
    var_wo_gems = statistics.variance(woLs)
    var_w_gems = statistics.variance(gLs)
    L = [brand,str(var_wo_gems),str(var_w_gems)]
    write_to_file('variance.csv',L)

if __name__=='__main__':
    all_watches = open('all_watch.pkl','rb')
    gem_watches = open('gem_watch.pkl','rb')

    aD = pickle.load(all_watches)
    gD = pickle.load(gem_watches)
    
    all_watches.close()
    gem_watches.close()

    keys = aD.keys()
    
    for key in keys:
        woD = isolator(aD[key],gD[key])        
        woLs,gLs = list_builder(woD,gD[key])
        write_avg_csv_line(key,woLs,gLs)
        write_median_csv_line(key,woLs,gLs)
        write_variance_csv_line(key,woLs,gLs)
