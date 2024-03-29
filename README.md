# Simple-React-Flask-App

One paragraph description to go



## Getting Started

Let's set up the environment

### Prerequisites

- Docker
- Access server with local forwarding to port 3000 
- (Optional: Add local forwarding to port 5000 to access flask backend directly)
```
$ ssh USERNAME@"SERVER_IP_ADDRESS" -L localhost:3000:localhost:3000
```

### Setting up the environment
- Build docker image
```
$ git clone https://github.com/jsong0327/Simple-React-Flask-App.git
$ cd Simple-React-Flask-App
$ docker-compose build --no-cache
```

### Run docker environment
- start docker image with container
```
$ CURRENT_UID=$(id -u):$(id -g) docker-compose up
```

- access http://localhost:3000

- start aster container (before start the container, you should remove the existing aster container)
```
$ docker run --runtime=nvidia -it --rm -v "volume path" --network "network name" --name "container name" "aster bin/bash"
```




### Useful commands
- access mongoDB with shell
```
$ docker exec -it simpleflaskapp_mongo_1 mongo
```

- access mongoDB with bash
```
$ docker exec -it simpleflaskapp_mongo_1 bash
```

- View containers
```
$ docker container ls -a
```

- Remove containers
```
$ docker container rm "container_name or id"
```

- View images
```
$ docker images
```


- Remove images
```
$ docker rmi "image_name or id"
```

- Export mongodb data
```
$ mongodump
```

- Import mongodb data
```
$ mongorestore --dir /dump
```


### Permission errors for 'mondoData' folder

- Access root account
```
$ ssh ROOT_USERNAME@"SERVER_IP_ADDRESS"
```
- Locate mongoData folder
```
$ ssh cd /home/USERNAME/SOMEWHERE_IN_YOUR_ACCOUNT
```
- Change folder permission
```
$ sudo chown -R $(id -u USERNAME):$(id -g USERNAME) ./mongoData
```
=======
# ASTER: Attentional Scene Text Recognizer with Flexible Rectification

ASTER is an accurate scene text recognizer with flexible rectification mechanism. The research paper can be found [here](https://ieeexplore.ieee.org/abstract/document/8395027/).

![ASTER Overview](overview.png)

The implementation of ASTER reuses code from [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).

## Correction (10/22/2018)

We have identified a bug we accidentally made in the code that causes only part of SVT images being tested and results in higher results. The bug has been fixed in commit [a7e8613](https://github.com/bgshih/aster/commit/a7e8613d6308e5a7aacb1237dfa0286d73cef342). Below are the corrected numbers on SVT. The results are still state-of-the-art, so the conclusions are not affected.

  - SVT (50) ASTER: 97.4%; ASTER-A: 96.3%; ASTER-B: 96.1%; 
  - SVT (None): ASTER: 89.5%; ASTER-A: 80.2%; ASTER-B: 81.6%


## Prerequisites

ASTER was developed and tested with **TensorFlow r1.4**. Higher versions may not work.

ASTER requires [Protocol Buffers](https://github.com/google/protobuf) (version>=2.6). Besides, in Ubuntu 16.04:
```
sudo apt install cmake libcupti-dev
pip3 install --user protobuf tqdm numpy editdistance
```

## Installation
  1. Go to `c_ops/` and run `build.sh` to build the custom operators
  2. Execute `protoc aster/protos/*.proto --python_out=.` to build the protobuf files
  3. Add `/path/to/aster` to `PYTHONPATH`, or set this variable for every run

## Demo

A demo program is located at `aster/demo.py`, accompanied with pretrained model files available on our [release page](https://github.com/bgshih/aster/releases). Download `model-demo.zip` and extract it under `aster/experiments/demo/` before running the demo.

To run the demo, simply execute:

```
python3 aster/demo.py
```

This will output the recognition result of the demo image and the rectified image.

## Training and on-the-fly evaluation

Data preparation scripts for several popular scene text datasets are located under `aster/tools`. See their source code for usage.

To run the example training, execute

```
python3 aster/train.py \
  --exp_dir experiments/demo \
  --num_clones 2
```

Change the configuration in `experiments/aster/trainval.prototxt` to configure your own training process.

During the training, you can run a separate program to repeatedly evaluates the produced checkpoints.

```
python3 aster/eval.py \
   --exp_dir experiments/demo
```

Evaluation configuration is also in `trainval.prototxt`.

## Citation

If you find this project helpful for your research, please cite the following papers:

```
@article{bshi2018aster,
  author  = {Baoguang Shi and
               Mingkun Yang and
               Xinggang Wang and
               Pengyuan Lyu and
               Cong Yao and
               Xiang Bai},
  title   = {ASTER: An Attentional Scene Text Recognizer with Flexible Rectification},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  volume  = {}, 
  number  = {}, 
  pages   = {1-1},
  year    = {2018}, 
}

@inproceedings{ShiWLYB16,
  author    = {Baoguang Shi and
               Xinggang Wang and
               Pengyuan Lyu and
               Cong Yao and
               Xiang Bai},
  title     = {Robust Scene Text Recognition with Automatic Rectification},
  booktitle = {2016 {IEEE} Conference on Computer Vision and Pattern Recognition,
               {CVPR} 2016, Las Vegas, NV, USA, June 27-30, 2016},
  pages     = {4168--4176},
  year      = {2016}
}
```

IMPORTANT NOTICE: Although this software is licensed under MIT, our intention is to make it free for academic research purposes. If you are going to use it in a product, we suggest you [contact us](xbai@hust.edu.cn) regarding possible patent issues.
>>>>>>> 2af9f671d582cd25104cf69513bb8ca87030a85b
# image_similarity
