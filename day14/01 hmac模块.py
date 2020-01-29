import hmac #和hashilib差不多
h=hmac.new()   #secret_key,你想要加密的bytes
密文=h.digest()   #进行摘要
hmac.compare_digest()  #对比 密文 和 另外一个密文
