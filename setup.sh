#!/bin/bash
sudo apt-get install python3-pip
pip3 install quandl
pip3 install sklearn
pip3 install pandas
pip3 install matplotlib

wget http://apache.claz.org/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz
mkdir zookeeper/
tar -zxvf zookeeper-3.4.14.tar.gz -C ./zookeeper/

cd ./zookeeper/zookeeper*
cp ./conf/zoo_sample.cfg ./conf/zoo.cfg
./bin/zkServer.sh start

cd ../..

wget http://apache.cs.utah.edu/kafka/2.3.0/kafka_2.12-2.3.0.tgz
mkdir kafka
tar -zxvf kafka_2.12-2.3.0.tgz -C ./kafka/

cd kafka
cd kafka*
