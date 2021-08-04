FROM paddlepaddle/paddle-benchmark:cuda10.1-cudnn7-runtime-ubuntu16.04-gcc82

ADD PaddleClas /PaddleClas

WORKDIR /PaddleClas

RUN pip install --upgrade -r requirements.txt -i https://mirror.baidu.com/pypi/simple

ENV FLAGS_fraction_of_gpu_memory_to_use=0.8
ENV FLAGS_cudnn_batchnorm_spatial_persistent=1
ENV FLAGS_max_inplace_grad_add=8

CMD ["python", "-m", "paddle.distributed.launch", "./tools/static/train.py", "-c", "./config/ResNet50_1gpu_fp32_bs96.yaml", ">", "/data/log/paddle_gpu1_fp32_bs96.txt", "2>&1"]
