# Data Science Toolbox

This is a microservice application which runs different useful data science applications on containers with docker
![alt text](https://imgur.com/KZfOIXL)
## Dependencies
Make sure you have [Docker](https://docs.docker.com/get-docker/) installed
## Installation

Clone this repository to your local files

```git
git clone https://github.com/amcgaw07/CS1660_DSToolbox
```

## Usage
Navigate to the location of the copied files in whichever CLI you choose and run docker-compose in detached mode
```bash
docker-compose up -d
```
## Applications Included:
### Main Toolbox
* Flask application with easy access to all other applications in the toolbox, simply select which program you'd like to use and it will run.
### RStudio
* RStudio is an integrated development environment for R, a programming language for statistical computing and graphics.
* Choosing this option opens up an RStudio Server
### Spyder
* Unimplemented
### IBM SAS
* Toolbox redirects to the IBM SAS cloud service. 
* SAS is a statistical software suite developed by SAS Institute for data management, advanced analytics, multivariate analysis, business intelligence, criminal investigation, and predictive analytics.
* IBM SAS is a paid software, so it may not be useful for everyone.
### Git
* Utilizing the [Wetty](https://hub.docker.com/r/krishnasrinivas/wetty/) terminal on a docker container with Git installed, you can access Git through  the toolbox on your localhost
* Simply cd back twice until you see the code directory, store files in the  directory where you cloned the repo to see them on the Wetty terminal and be able to upload them to git.
### Jupyter Notebook
* The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.
* Choosing this option opens up a Jupyter Notebook server
### Orange
* Unimplemented
### Visual Studio Code IDE
* Unimplemented
### Apache Hadoop
* Unimplemented
### Apache Spark
* Unimplemented
### Tableau
* Toolbox redirects to Tableau cloud service.
* Tableau is a paid software so it may not be useful for everyone
### SonarQube and SonarScanner
* SonarQube is an open-source platform developed by SonarSource for continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs, code smells, and security vulnerabilities on 20+ programming languages.
* Both SonarQube and SonarScanner are available through the toolbox to test code
### Tensorflow
* TensorFlow is a free and open-source software library for machine learning.
* Toolbox redirects to a Jupyter Notebook server with Tensorflow pre-installed
* Also comes packed with TensorFlow tutorial documents
### Markdown
* Markdown editor server
* Edit on the left and see live changes to your markdown styling on the right of the screen
### Notepad++
* Unimplemented
