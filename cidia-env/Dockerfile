FROM vrex141/qt5.12_cpp17
# MAINTAINER frostasm <frostasm@gmail.com>

USER root
ENV HOME /home/user

RUN apt-get update && \
	apt-get install -y wget && \
	apt-get install -y libssl-dev && \
	apt-get install -y ffmpeg

#CMAKE
ARG CMAKE_VERSION=3.17
ARG CMAKE_BUILD=1
ENV DEBIAN_FRONTEND=noninteractive
RUN cd /opt && \
	wget https://cmake.org/files/v$CMAKE_VERSION/cmake-$CMAKE_VERSION.$CMAKE_BUILD.tar.gz && \
	tar -xzvf cmake-$CMAKE_VERSION.$CMAKE_BUILD.tar.gz && \
	cd cmake-$CMAKE_VERSION.$CMAKE_BUILD/ && \ 
	./bootstrap && \ 
	make -j$(nproc) && \ 
	make install

#MITK
RUN git clone https://github.com/MITK/MITK.git /opt/MITK && cd /opt/MITK && git checkout c0f884b289 && \ 
	mkdir /opt/MITK-build && \ 
	cd /opt/MITK-build && \
	cmake ../MITK && \
	make -j1
	# make -j$(nproc)

ENV MITK_BUILD_PATH=/opt/MITK-build
ENV QT_ROOT_PATH=/opt/Qt/5.12.4
ENV DEBIAN_FRONTEND=noninteractive
#COPY TEMPORAL FILES PHNN, MODELS, IMAGES -> MAKE TO SHARED DIRECTORY
RUN git clone https://github.com/noamlr/pipeline-app-3.git /opt/pipeline && \
	git clone https://github.com/noamlr/video-maker-mitk.git /opt/video-maker-mitk && \
	git clone https://github.com/noamlr/screenshot-axis-views.git /opt/screenshot-axis-views && \
	git clone https://github.com/noamlr/vglrun-support /opt/vglrun-support && \	
	# mkdir /opt/resnet101/ && mkdir /opt/data/ && \
	# mkdir /opt/data/dicom-original && mkdir /opt/data/dicom-original/exame-pulmao && \
	# mkdir /opt/data/nii-original && mkdir /opt/data/nii-original/exame-pulmao && \
	# mkdir /opt/data/nii-segmented && mkdir /opt/data/nii-segmented/exame-pulmao && \
	# mkdir /opt/data/slices2d && mkdir /opt/data/slices2d/exame-pulmao && \
	# mkdir /opt/data/videos && \
	cd /opt/screenshot-axis-views && rm -r build && cmake -B build -S . && cd build && make && \
	cd /opt/video-maker-mitk && cmake -B build -S . && cd build && make 
COPY p-hnn/ /opt/p-hnn/
# COPY model/ /opt/resnet101/model/
# COPY legend/ /opt/resnet101/legend/
# COPY N185/ /opt/data/dicom-original/exame-pulmao/N185/
COPY variables.py /opt/pipeline/variables.py


# VirtualGL
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y lightdm && \
	# echo "\n[Install]\nWantedBy=multi-user.target" > /etc/systemd/system/display-manager.service && \
	systemctl enable lightdm && \
	cd /opt/vglrun-support && \
	dpkg -i virtualgl_*.deb && \
	# /opt/VirtualGL/bin/vglserver_config && \ 
	# 1 n n Y X
	# touch /root/.Xauthority && \
	dpkg -i turbovnc_*.deb && \
	# /opt/TurboVNC/bin/vncserver && \
	# password 2 times n
	# /opt/TurboVNC/bin/vncserver -list
	sed -i 's/$host:/unix:/g' /opt/TurboVNC/bin/vncserver

ENV PATH ${PATH}:/opt/VirtualGL/bin:/opt/TurboVNC/bin
ENV DISPLAY :0

#CONDA
ARG ANACONDA_VERSION=2020.11
RUN wget https://repo.continuum.io/archive/Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh -O anaconda.sh && \
	chmod +x anaconda.sh && \
	./anaconda.sh -b -p /opt/conda && \
	rm anaconda.sh && \
	ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
	ln -s /opt/conda/bin/conda /usr/bin/conda

ENV PATH /opt/conda/envs/env/bin:$PATH
SHELL ["/bin/bash", "-c"] 
COPY script.sh /opt/script.sh
COPY cidia_env.sh /opt/cidia19_env.sh
RUN conda init bash && \
	chmod +x /opt/script.sh  && \
	/opt/script.sh && \
	conda create -n cidia19 python=3.6 && \
	echo "conda activate cidia19" > ~/.bashrc && \
	echo "conda activate cidia19" > /root/.bashrc && \
	chmod +x /opt/cidia19_env.sh  && \ 
	/opt/cidia19_env.sh


# Reconfigure locale
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales


# Add group & user + sudo
# RUN groupadd -r user && useradd --create-home --gid user user && echo 'user ALL=NOPASSWD: ALL' > /etc/sudoers.d/user

# USER user
# WORKDIR /home/user
EXPOSE 5000
WORKDIR /opt/pipeline
CMD [ "/opt/conda/envs/cidia19/bin/python", "wsgi.py" ]
