# RaffleMania

### Objective
Create an application that generates ‘Objects’ upon a set of predefined rules. The ‘Objects’ can be from any domain, being creative.

To simplify, I have to create an application takes data from two different services and generates an ‘Object’. I have complete freedom in the application I decide to create.

### Contents
* [Constraints](#contraints)
* [What I plan to create](#what-i-plan-to-create)
* [User Stories, Acceptance Criteria and Story Points](#user-stories-acceptance-criteria-and-story-points)
* [CI Pipeline](#ci-pipeline)
* [Project Management](#project-management)
* [Risk Assessment](#risk-assessment)
* [Frontend](#frontend)
* [Testing](#testing)
* [Jenkins](#jenkins)
* [Improvements](#improvements)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

### Constraints
The constraints in this project are the technologies that need to be used. The following constraints have been set for this project:
* Trello for project management (Kanban Board)
*	Version Control: Git
*	CI Server: Jenkins
*	Configuration Management: Ansible
*	Using GCP as Cloud Provider
*	Containerisation: Docker
*	Orchestration Tool: Docker Swarm
*	Reverse Proxy: NGINX

### What I plan to create
The app I plan to create will be split into 4 services. The frontend will be service 1. This is what the user will see and where the ‘Objects’ are displayed. Service 2 will be a list of letters, just like in a raffle where entrants are given a number for a prize draw. Service 3 will be a list of random prizes. Random numbers and prizes from services 2 & 3 will generate the ‘Object’ shown on the frontend, e.g., letter A wins an iPad. And finally service 4 will also create an ‘Object’ using predefines rules based on the results of service 2 + 3.

| Services | Applied on |
| --- | --- |
| 1 |  Frontend (Where ‘Objects’ will be displayed) |
| 2 |  Half of an object (List of letters) |
| 3 |  Other half of the object (List of prizes) | 
| 4 |  ‘Object’ created from results of service 2 + 3 |

### User Stories, Acceptance Criteria and Story Points

To create a vision as to what the application would look like, I used user stories. Being the sole user, the user stories came from my perspective of a user. To understand what a feature requires, an acceptance criterion is attached to the user stories. Story points are a means of calculating how much work it will take to complete a task. PlanningPoker.com is used to decide the story point assigned to a user story. Each user story was given a number depending on complexity using the Fibonacci sequence to calculate the story point.

* As a product owner, I want to be able to produce a working raffle system, so that entrants and gifts can be chosen at random with a story point of 8. Given the user is on the raffle page, when they refresh the page, they can see the raffle is redrawn.

* As a user, I want to be able to see multiple draws, so that entrants I know the draws are randomised with a story point of 5. Given the user is on the raffle page, when they refresh the page, they can see the draw results are different.

### CI Pipeline

![CIpipeline](https://user-images.githubusercontent.com/101266645/168625591-533c68e6-1865-4743-a3a0-985314a77eb8.png)

| CI Pipeline | What was done in this project |
| --- | --- |
| Project Tracking – Trello | Work is set out and branches/tasks are created on Version Control System. |
| Version Control System – Git & GitHub | Git – Software on computer that takes snapshots of work done. GitHub – Remote destination that snapshots can be pushed to. |
| Source Code - Developer | Pulls down latest version of code. Can push up to main branch. | 
| pytest | Run tests on each route. |
| Jenkins | Loaded onto a VM in the cloud. GitHub repository link attached to Jenkins in order to build tool. |
| Ansible | Used to build and push images along with depolying code. |
| Docker Swarm & NGINX | Used to create a rolling update. |

### Project Management
###### Trello and MVP

![Trello](https://user-images.githubusercontent.com/101266645/168625641-e65017d1-f082-46cf-a5a1-730936bffcc3.png)

The Trello board contains three colours, these represent:

* Red – Must Have (MVP – Minimum Viable Product)
* Orange – Should Have
* Yellow - Could Have

This is because the tasks mentioned only include those that were an essential part of the project and those that would significantly improve the project. There are no tasks for the prioritisation of Won't Have, as the project was completed with tasks that were always to be included. Due to time constraints, the tasks that may have been completed were not completed.

### Risk Assessment

Risk Assessments are used to ensure a project&#39;s success by evaluating scenarios that may impact the project in a negative way. Making note of potential risks informs an individual ensuring they are aware of what may occur prior to undergoing a particular task. By evaluating risks, I am able to mitigate the damage that may be caused to the project and may design the project such that theses risks are less likely to occur.

| Description | Evaluation | Likelihood | Impact Level | Responsibility | Current Control Measures | Proposed Control Measures | Response | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GCP going down | Data will not be able to be accessed | Low | High | Google Cloud Platform | None | Backup files saved on computer | Wait till GCP is back up and running | 28/04/22 |
| Code looking messy | Hard to understand data | High | Med | Mahammed Kassam | Try and understand the code myself | Get a colleague to look over the code and see if they understand it | Make data look presentable | 28/04/22 |
| Application freezing | Unsaved worked will get lost | Med | High | Mahammed Kassam | Constantly pushing to GitHub | Having backups saved | Clone down latest push to GitHub | 28/04/22 |
| Using VMs private IP | Private IP will become public knowledge | High | High | Mahammed Kassam | Ensuring public IP is copied | Constantly checking the public IP is being used | Create an entirely new VM | 28/04/22 |
| Not installing all requirements | Application will not work | High | Low | Mahammed Kassam | When error is thrown up , install all requirements | Have a requirements file, that lists all requirements | Install all requirements from the requirements file | 28/04/22 |
| No relevant firewall rules | There will be no accessing the application | Low | High | Mahammed Kassam | Ensure all firewall rules are in place | Before creating application, know what firewall rules are needed | Add correct firewall rules to VM | 29/04/22 |
| Constantly adding/removing images/containers | Takes a lot of time | High | Low | Mahammed Kassam | Using up arrow, so no need to type enitre code | Using up arrow, so no need to type enitre code | Ensure all code is correct, which will reduce the amount of times needed to add/removes images/containers | 09/05/22 |
| Old PC being used | PC will run really slow | High | High | PC | Only use programs/softwares that are needed | Using a PC with a bigger RAM and a better processor | Keep calm | 09/05/22 |
| File already existing | Jenkins test failing | High | Low | Mahammed Kassam | Rename file | Create a new file | Rename current file | 11/05/22 |
| Unsure how to proceed with a task | Time to complete project will be reduced | High | Low | Mahammed Kassam | Start with documentation to give a layout on how to proceed | Same as current control measures - Start with documentation to give a layout on how to proceed | Ask trainer on what they would recommend | 11/05/22 |
| Tutors unavailable | Time to complete project will be reduced as waiting for help | High | High | Mahammed Kassam | Wait for a tutor to be available | Use resources online for help | Ask before attempting the task, what is required, therefore have an understanding on how to tackle the task | 15/05/22 |

### Frontend
The frontend consists of just one page, consisting of the navigation bar that has just the home page on it. The rest of the page consists of the title, statement with objects from services and a refresh button.

Below are screenshots of the frontend, along with different possible outcomes:

1. If service 2 is either 'A, E, I, O, U' or service 3 starts with an 'A'. Service 4 should return 'Airpods'

![2A](https://user-images.githubusercontent.com/101266645/168625727-609d8914-b54d-4c1c-a52f-cbdaa090e688.png)

![1E](https://user-images.githubusercontent.com/101266645/168625740-1d62f991-e2ca-42c3-84d8-8b443f6658ae.png)

2. If service 2 is NOT either 'A, E, I, O, U' or service 3 DOES NOT start with an 'A'. Service 4 should return 'QA CloudAcademy free demo'

![justQA](https://user-images.githubusercontent.com/101266645/168625797-43896de0-837c-432f-af7c-1d8f5d9053ce.png)

### Testing

When testing the app, each service was tested individually. Along with each service being tested, there was atest for each route. The aim was to get each service test to be above 80%. Below are the test results for each service:

* Results for service 1:

![serv1](https://user-images.githubusercontent.com/101266645/168625846-238a60a1-206e-42e3-b95a-f3bd45627bf6.png)

* Results for service 2:

![serv2](https://user-images.githubusercontent.com/101266645/168625859-decf429f-1800-4c44-b452-7d9a717edbe9.png)

* Results for service 3:

![serv3](https://user-images.githubusercontent.com/101266645/168625869-1b4181d3-aa8f-498e-9585-cda9a39c7cd6.png)

* Results for service 4:

![serv4](https://user-images.githubusercontent.com/101266645/168625877-31de836e-d3bb-47ed-918a-b0f0e267b791.png)

### Jenkins

Docker-compose stage
After being successfully ran once the docker-compose stage of the jenkinsfile would fail. The code for the stage was 'sh "ln -s rafflemania_qa_project_2/docker-compose.yaml building"'. It threw an error because for some reason 'building' has already been used. To counter this the code was changed 'sh "docker-compose build --parallel"', to allow unlimited builds to be successful.

![Jenk0](https://user-images.githubusercontent.com/101266645/168618347-135f381c-880c-46a6-9da8-28c29844f4b9.png)

* Results for service 1:

![Jenk1](https://user-images.githubusercontent.com/101266645/168618368-ad3357ad-b4eb-4b79-88b4-5ede78ee115a.png)

* Results for service 2:

![Jenk2](https://user-images.githubusercontent.com/101266645/168618392-7357307b-4299-4925-a7d2-dd87a13ea2e4.png)

* Results for service 3:

![Jenk3](https://user-images.githubusercontent.com/101266645/168618413-0e112d61-cce7-4cc0-9083-6f430aae07fd.png)

* Results for service 4:

![Jenk4](https://user-images.githubusercontent.com/101266645/168618427-1aa9de15-6f68-462c-bac5-70be33ede87c.png)

Ansible/Deploy stage failure - Host key verification failed.
This error could not be resolved. Shown below is how I created and used the jenkins ssh-keygen.

![ssh](https://user-images.githubusercontent.com/101266645/168624111-35721d7c-6715-424c-a392-244fe788d0e4.png)

In the Jenkins VM I used the sudo su jenkins command to activate the Jenkins user. I attempted to created an ssh-keygen in the .ssh but was unseuccesful, thus created it outside the .ssh folder. This ssh-key's public key would then be inserted into the SSH Key section of both the swarm-manager and swarm worker VM.

In the Jenkinsfile on the main VM, the file route is as follows:

![Jenkinsfilecode](https://user-images.githubusercontent.com/101266645/168619820-a6b56616-f9b9-4e15-9f13-ecf5c6eb0ad3.png)

The same file route would be inserted into the inventory.yaml file:

![Inventoryyamlcode](https://user-images.githubusercontent.com/101266645/168619843-e32c6948-ca17-44c5-8fcc-a8f4b9bf7f7c.png)

Error would still not be fixed, thus resulting in the deployment not being ran and unable to move onto the rolling update.

![AnsPipe](https://user-images.githubusercontent.com/101266645/168619902-74fa962a-b93d-42af-96cf-998277afe0bb.png)

![AnsError](https://user-images.githubusercontent.com/101266645/168619924-52c51359-86ab-4bb9-8f5f-3978b8806e51.png)

To try and combat the error I tried to connect manually first (i.e. ssh into jenkins, switch user to jenkins and then run 'ssh jenkins@swarm-manager') in order to confirm that I definitely want to connect, this failed to connect.

![Fail](https://user-images.githubusercontent.com/101266645/168770105-de5a0cce-9647-4f34-ac6c-c89beb44041f.png)

When i do 'ssh -i ansible_key swarm-manager', this connects but when i build is ran the same error 'Host key verification failed' is shown.

Rolling Update - 
The rolling update was performed however it was done manually. Images for the frontend were uploaded DockerHub with differences. A swarm was then created and initialised, along with creating a Manager node. A stack was then created for the configuration of first image and then deployed.

![updt1](https://user-images.githubusercontent.com/101266645/168693864-8527fc57-5b57-4749-ae8e-ae17bb0f5f47.png)

For the rolling update the docker-compose.yaml file was altered to pull down the new image. This time the frontend will serve a powderblue background. Thereafter updating the service by deploying again.

![updt2](https://user-images.githubusercontent.com/101266645/168693879-c47cf6a5-0dfa-407a-9563-b9bfa3fba203.png)

### Improvements

Story Points - 
A use story has more influence when the users aren't myself. The best/most usual way to use story points is is a collaborative project, because the chosen story points promote discussion, and multiple perspectives may lead to a consensus. Also having more than 2 user stories would help create a better image of what is wanting to be created

Documentation -
The documentation was done throughout the entire project with a little start before the project. If most of the documentation was completed before the start of the project, not only would it speed up the project, but would give a better idea of how the overall project would look.

Frontend - 
The Navigation bar is useless as there is only one webpage for the frontend, it just makes the frontend look presentable. Making the page look presentable without the navbar would have been ideal.

Ansible - 
Having more knowledge on Ansible would have helped in the deployment of the project. Using out of work hours to go through more about ansible would have been extremely beneficial. Also reaching out to more trainers would help resolve issues faced.

Rolling Update - 
Providing I had solved the issue for the error 'Host key verification failed'. The webhook that I had set up would have allowed for a rolling update to be performed automatically.

Other Improvements - 
* Include an input for service two, so instead of a random letter being used, it could have been a name of an entrant.
* Have entrants to be able to select what prize they wanted to go for (making a raffle system per prize).
* Have a database that tracks the prizes given out to specied entrants.

### Authors

Mahammed Kassam

### Acknowledgements

Many thanks go to the trainer, Victoria Sacre, for the help, guidance, and patience. The cohort of 22MarEnable1 deserve to be acknowledged for their support and friendly demeanour. Not forgetting Luke Benson, Harry Volker and Adam Gray for being available to answer question and also Earl Gray for the recodings during weeks 1 through to 5.

Thanks go to getbootstrap for their navbar.
