echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
docker tag patient-record-service $DOCKER_USERNAME/patient-record-service
docker tag appointment-scheduling-service $DOCKER_USERNAME/appointment-scheduling-service
docker tag notification-service $DOCKER_USERNAME/notification-service
docker tag aggregator-service $DOCKER_USERNAME/aggregator-service
docker push $DOCKER_USERNAME/patient-record-service
docker push $DOCKER_USERNAME/appointment-scheduling-service
docker push $DOCKER_USERNAME/notification-service
docker push $DOCKER_USERNAME/aggregator-service
