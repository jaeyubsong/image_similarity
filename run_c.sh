#i! /bin/bash


#docker stop pixel_container
#docker rm pixel_container
#docker run --runtime=nvidia -it -d -v /home/sungjune/Simple-React-Flask-App/flask-backend/docker_models/pixel_link_1/dataset/ICDAR2015/Challenge4/ch4_test_images:/test_images -v /home/sungjune/Simple-Flask-App/flask-backend/docker_models/pixel_out:/pixel_link_workdir/conv3_3/test/icdar2015_test/model.ckpt-38055/cropped_image --name pixel_container simple-react-flask-app_pixel_link

docker run --runtime=nvidia -it --rm -v /home/sungjune/Simple-React-Flask-App/flask-backend/docker_models/pixel_link_1/dataset/ICDAR2015/Challenge4/ch444_test_images:/test_images -v /home/sungjune/Simple-React-Flask-App/flask-backend/docker_models/pixel_out:/pixel_link_workdir/conv3_3/test/icdar2015_test/model.ckpt-38055/cropped_image --name pixel_container simple-react-flask-app_pixel_link



docker run --runtime=nvidia -it --rm -v /home/sungjune/Simple-React-Flask-App/flask-backend/docker_models/pixel_out:/aster_workdir/aster/data/test_images --name aster_container simple-react-flask-app_aster


### Remove the existing pixel_link and aster containers, and make new containers attaching them to simple network to work with other containers.
### Add tsv directory volume to the aster.
### Change pixel_link input data volume.
### /pixel_link_workdir/test_images
### pixel_link에서 len - 1 해주기
