import requests
url = "https://www.amazon.cn/dp/B09BCZKHQ5/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=ZSA2V41W5VF1FS7VJXRG&pf_rd_t=101&pf_rd_p=55e99dfe-8fe8-420c-a666-0e2aece0b1f5&pf_rd_i=116169071"
kv = {'User-Agent': 'Mozilla/5.0'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[5000:6000])
except:
    print("爬取失败")