import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print(f"A velocidade de download é: {down}")
print(f"A velocidade de upload é: {upload}")