# MediFinder

**MediFinder** is a simple and handy web application that helps users find medical services quickly. It’s built with Python (Flask) and packed inside a Docker container so it can run easily anywhere — your laptop, a server, or in the cloud.

---

## What’s inside this project?

- `app/` — The main Python Flask app code and HTML templates  
- `.env` — Environment configuration (like secrets, keys, ports)  
- `requirements.txt` — Python packages the app needs  
- `Dockerfile` — Instructions to create the Docker image  
- `README.md` — This file, explaining how to use everything  
- `venv/` — A Python virtual environment (not required if you use Docker)

---

## Why use Docker?

Docker packages your app and all its dependencies into one neat container. That means:

- No worries about installing Python or packages on your machine  
- Runs the same way on any machine or server  
- Makes deployment easier and consistent  

---

## Quick Start: Run MediFinder locally with Docker

You don’t need to install anything besides Docker!

### Step 1: Clone the project

Open your terminal or command prompt and run:

```bash
git clone https://github.com/Timothee-U/Medifinder.git
cd Medifinder
```

### Step 2: Build the Docker image

This step packages your app inside a Docker container:

```bash
docker build -t medifinder-app .
```

### Step 3: Run the Docker container

Start the app with:

```bash
docker run -d -p 8080:8080 medifinder-app
```

- `-d` runs the container in the background  
- `-p 8080:8080` maps your computer’s port 8080 to the app’s port 8080

### Step 4: Open the app in your browser

Go to: `http://localhost:8080` — you should see the MediFinder homepage!

---

## How to stop the app

If you want to stop the running app container, run:

```bash
docker stop $(docker ps -q)
```

This stops all running Docker containers.

---

## Environment variables

The `.env` file contains configuration like API keys or settings. You can customize it if needed. The Docker container reads this file when it starts.

---

## Deploying MediFinder on multiple servers

For bigger setups, you can:

- Deploy the Docker container on multiple servers (like `web01`, `web02`)  
- Use a load balancer (NGINX, HAProxy, or cloud-based) to distribute traffic evenly  
- This improves reliability and can handle more users  

---

## What if you don’t want to use Docker?

You can also run MediFinder directly if you have Python 3.11 installed:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app/app.py
```

Then open `http://localhost:8080`.

---

## Troubleshooting tips

- If Docker commands don’t work, check if Docker Desktop is running  
- Make sure port 8080 is free on your machine  
- Check the logs with `docker logs <container_id>` if the app doesn’t start  
- Make sure `.env` file exists and is configured properly  

---

## Summary of useful commands

 Purpose                   Command                                          
 Clone project             `git clone https://github.com/Timothee-U/Medifinder.git` 
 Build Docker image        `docker build -t medifinder-app .`                
 Run Docker container      `docker run -d -p 8080:8080 medifinder-app`       
 Stop all Docker containers `docker stop $(docker ps -q)`                     
 Run app without Docker   See instructions above                             

---

## Thanks for checking out MediFinder!

This project was made to be simple to run and deploy, whether you’re just trying it locally or planning to run it on real servers. I am open to reviews and ideas how how make it a better project.
