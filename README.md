# plcGatherInfo
hello world.

## Ping

不使用Scapy发送Ping包，真实Ping TTL值比Scapy小，Scapy不够准确。

## Struct unpack

* unpack(fmt, )

raw_iph = packet[0:20]  # 尚未解析的IP数据报头部固定部分
# unpack(fmt, buffer) - 根据指定的格式化字符串来拆解给定的buffer
# B 单字节的整型
# H 双字节的整型
# s bytes，前加数字表示取4字节的bytes
iph = unpack("!BBHHHBBH4s4s", raw_iph)

