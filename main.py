import tkinter as tk
from tkinter import messagebox
import requests
import concurrent.futures

# DoH 服务提供商的 URL
doh_providers = {
    "Cloudflare": "https://1.1.1.1/dns-query",
    "Google": "https://dns.google/resolve?",
    "360": "https://doh.360.cn/dns-query	",
    "Tencent Cloud": "https://1.12.12.12/dns-query",
    "OpenDNS": "https://208.67.222.222/dns-query"
}

# 要查询的域名
domain = "taobao.com"

def check_doh_availability():
    results = {provider: None for provider in doh_providers}

    def query(provider, url):
        try:
            print(f"查询 {provider} 的 DoH 服务...")
            # 发起 GET 请求，并指定查询的域名
            response = requests.get(
                url,
                headers={'Accept': 'application/dns-json'},
                params={'name': domain, 'type': 'A'},
                timeout=5
            )
            if response.status_code == 200:
                print(f"{provider} 查询成功: {response.json()}")
                return provider, True
            else:
                print(f"{provider} 查询失败，状态码: {response.status_code}")
                return provider, False
        except Exception as e:
            print(f"{provider} 查询时发生异常: {e}")
            return provider, False

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_provider = {executor.submit(query, provider, url): provider for provider, url in doh_providers.items()}
        for future in concurrent.futures.as_completed(future_to_provider):
            provider, success = future.result()
            results[provider] = success

    # 打印所有查询结果
    print("查询结果:", results)

    # 判断 DoH 访问结果
    successful_providers = [provider for provider, success in results.items() if success]

    if successful_providers:
        messagebox.showinfo("结果", f"以下DoH提供商可用：{', '.join(successful_providers)}")
    else:
        messagebox.showwarning("结果", "当前网络环境不支持DoH访问，请检查路由器/防火墙是否允许DoH流量通行。\n如果您的网络环境是校园网或者公司网络，请联系您的管理员以开启DoH访问权")

def start_monitoring():
    if messagebox.askyesno("确认", "您是否要开始DoH可用性环境监测？"):
        check_doh_availability()

# 创建 GUI 窗口
root = tk.Tk()
root.title("DoH可用性环境监测")
root.geometry("300x200")

start_button = tk.Button(root, text="开始监测", command=start_monitoring)
start_button.pack(pady=20)

root.mainloop()
