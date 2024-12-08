# Deployment Guide for HealthSync

This document outlines the steps required to deploy the HealthSync platform, including microservices, Kubernetes configurations, and AWS integrations.

---

## **1. Prerequisites**
- Docker installed locally.
- Kubernetes cluster set up (e.g., Minikube, AWS EKS, or GKE).
- kubectl configured to communicate with your cluster.
- AWS account with access to S3, Redshift, and QuickSight.

---

## **2. Build Docker Images**
Run the following commands to build Docker images for each microservice:

```bash
docker build -t patient-record-service ./patient-record-service
docker build -t appointment-scheduling-service ./appointment-scheduling-service
docker build -t notification-service ./notification-service
docker build -t aggregator-service ./aggregator-service
