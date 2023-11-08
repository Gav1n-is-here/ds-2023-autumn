# import numpy as np

# # 生成随机音频信号
# audio_signal = np.random.random(1024)

# # 对音频信号进行FFT
# fft_result = np.fft.fft(audio_signal)

# # 输出FFT结果
# print(audio_signal)
# print(fft_result)


import pyaudio
import numpy as np

# 初始化PyAudio
p = pyaudio.PyAudio()

# 打开音频文件
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024)

# 读取音频数据
data = stream.read(1024)

# 将音频数据转换为NumPy数组
numpy_array = np.frombuffer(data, dtype=np.float32)

# 关闭音频流
stream.stop_stream()
stream.close()
p.terminate()

# 输出NumPy数组
print(numpy_array)