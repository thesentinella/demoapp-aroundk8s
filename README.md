# Kubernetes Demo App - Portainer + Sidero Omni Workshop  

Aplicación de demostración para desplegar en Kubernetes durante el workshop de **Portainer + Sidero Omni**.  
Demo presentada en [AroundK8s](https://aroundk8s.com) el **26 de marzo de 2025**.  

Descarga los slides del workshop [aquí](https://storage.googleapis.com/sentinella-assets/aroundk8s-portainer-talos.pdf)

## 📌 Descripción  

Esta aplicación web sencilla, construida con **Flask (Python)**, se ejecuta en **Kubernetes** y está diseñada para demostrar despliegues gestionados con **Portainer** y **Sidero Omni**.  

Incluye:  
- Código fuente en **Python (Flask)**.  
- `Dockerfile` para construir la imagen del contenedor.  
- Manifiestos de **Kubernetes** (`Deployment`, `Service`).  
- Configuración opcional para **Ingress**.  

## 🚀 Despliegue en Kubernetes  

### 1️⃣ Construcción de la imagen  

```sh
docker build -t your-dockerhub-username/k8s-web-demo:latest .
docker push your-dockerhub-username/k8s-web-demo:latest
```

### 2️⃣ Despliegue en Kubernetes

```sh
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 3️⃣ Acceder a la aplicación
Usamos el port-forwarding
```sh
kubectl port-forward svc/k8s-web-demo-service 8080:80
```

Luego, accede desde el navegador: http://127.0.0.1:8080
### 📡 Presentación
Los slides del workhop están disponibles [aquí](slides/aroundk8s-portainer-talos.pdf)
