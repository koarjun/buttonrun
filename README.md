# Run as Python app 
To run application as pure python app, run the following commands
```
pip install -r requirements.txt
```
```
python -m main
```

# Run using docker
To run using docker, build the image and run the image using the following commands
```
docker build -t buttonrun .
```
```
docker run -p 5000:5000 buttonrun
```

# Run using k8s
To run using Kubernetes, use the following
```
kubectl apply -f k8s
```
Access the application at the nodePort given in the button-run-services.yaml file
