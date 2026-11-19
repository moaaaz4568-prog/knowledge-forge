---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DLSvtWwS4vT.txt"
words: 510
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DLSvtWwS4vT

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DLSvtWwS4vT.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DLSvtWwS4vT

---

Hello guys, in this video we are going to learn about Elastic Container Service. What is Elastic Container Service? Why do we use it? Now when you log into your AWS account, the process of creating an account, I have already explained in my previous video. Once you log in, you will see this kind of interface. On the left side, you can see recently visited services, you can navigate directly from here, like using a shortcut. To access other services, you can use the search bar. In the search bar, type Elastic Container Service, which is also known as AWS ECS. In ECS, we create a task definition. In this task, we run a Docker image. If you don't know the process to create a Docker image, don't worry, we'll cover that in our next video. For now, you can use a public Docker image hosted on Docker Hub. You can use the image created by the NGINX team. It is great for testing and demonstration purposes. You can see a flow diagram on the screen. You have to follow this flow in order to create everything and access the Docker image over a publicly accessible URL. You will see many fields during the initialization process. Don't worry if you don't understand any field yet. We are going to learn everything one by one, so no need to worry. Step one, create an ECS cluster. An ECS cluster is a logical group of infrastructure resources. These can be EC2 instances or Fargate capacity. This is where your containerized tasks will run. Think of it as the environment that manages and hosts your services and tasks. Step two, create a task definition. A task definition is like a blueprint for your application. It includes the Docker image to use, required CPU and memory, ports to expose, and environment variables. ECS uses this definition to run your application inside containers. Step three, create an application load balancer. The ALB distributes incoming traffic to your ECS tasks. It supports host-based routing, which routes traffic by domain name. It also supports path-based routing, which routes traffic by URL path. This lets you run multiple services behind a single load balancer. Step four, create an ECS service. An ECS service ensures that a specific number of task instances are always running. It restarts tasks automatically if they fail. It also registers them with the ALB so they can receive traffic. Step five, edit inbound rules in the security group. Finally, modify the inbound rules in the security group. Allow traffic from any IP address. This is useful for testing and development. In production, always restrict access to known IP addresses for better security. Configure everything just like I have shown in the video so that you get the idea. In the next few videos, I will teach you everything step by step. Also, don't forget to tell your friends to subscribe. If they also want to gain knowledge and get big placement offers in the future, this is a required skill in many companies.