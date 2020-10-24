
def auto_asset(node):
    ret = salt.remote_grains_execution_sigle(node)
    asset_info={}
    asset_info['os']= ret[node]['oscodename']
    asset_info['kernelrelease']= ret[node]['kernelrelease']
    asset_info['cpu_model']= ret[node]['cpu_model']
    asset_info['dns']= ','.join(ret[node]['dns']['ip4_nameservers'])
    asset_info['serialnumber'] =  ret[node]['serialnumber']
    asset_info['virtual'] =  ret[node]['virtual']
    asset_info['localhost'] = ret[node]['localhost']
    asset_info['mem_total'] =  ret[node]['mem_total']
    asset_info['num_cpus'] =  ret[node]['num_cpus']
    asset_info['ip4_interfaces'] = " ".join(ret[node]['ip4_interfaces']['eth0'])
    asset_info['hwaddr_interfaces'] = ret[node]['hwaddr_interfaces']['eth0']
    return asset_info

import threading


class MyThread(threading.Thread):

    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

ass =Asset.objects.all()
ids_list =[ i.inner_ip for i in ass]
files = range(len(ids_list))
t_list = []
t_data = []
for i in files:
    t = MyThread(auto_asset, (ids_list[i],))
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()  # 一定要join，不然主线程比子线程跑的快，会拿不到结果
    t_data.append(t.get_result())
    print(t.get_result())
