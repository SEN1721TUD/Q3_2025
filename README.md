# SEN1721- Travel Behaviour Research 2025
## *Latent Class discrete choice models*


## 1. Introduction

Welcome to the *Latent class model* section of the SEN1721 course repository. In this repository, you will find Jupyter notebooks for the in-class assignments, step-by-step instructions for setting up your Python environment, and a discussion forum where you can ask questions related to the course content.
   

## 2. Course description

Mathematical models of choice behaviour –henceforth referred to as "Discrete Choice Models" (DCMs)– are widely used to study the decision-making behaviour of individuals across numerous domains, including transportation, marketing, and health. DCMs are used to infer preferences over attributes and alternatives and predict the impact of new policies.

This section aims to equip students in the socio-technical domain with a comprehensive understanding of latent class models. You will learn the theoretical underpinnings of choice models and gain practical hands-on experience in estimating and applying these models to solve real-world problems.  

## In-class assignments
In-class assignments are offered in the form of Jupyter notebooks and aim to demonstrate and reinforce knowledge about Latent class choice models, the underlying assumptions, estimation techniques, and how to interpret outcomes. They provide **hands-on** experience with the method, which is essential to master it. There are two in-class assignments, which comprise a series of **exercises**.

For the in-class assignments, we use Python notebooks (aka Jupyter Notebooks). You have three options to work with them. 
A. Anaconda (local)
B. Pip (local)
For each option, **instructions** to set up your Python environment are given at the **end of this page**.

If you are **unfamiliar with Python**, we recommend completing [Lab session 0 from SEN122A](https://github.com/SEN1221TUD/Q2_2024/tree/main/Lab_sessions/Lab_session_00), which provides the necessary tools to conduct the in-class assignments. It covers topics such as data structures, utilising external libraries, data exploration, visualisation, etc. 

## Tutorials
Tutorials are supplementary materials, offered to help you deepen your understanding of key concepts in choice modelling. These ([tutorials](https://github.com/SEN1221TUD/Tutorials)) aim to reinforce your understanding of the topics covered. They do not contain exercises.<br>

Here, you will find tutorials. Tutorials aim to explain concepts that are important to choice modelling. The current list of topics is:

[Tutorial 1](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial1/tutorial1_DGP_and_bias.ipynb): The data generating process and bias <br>
[Tutorial 2](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial2/tutorial2_The_loglikelihood_function.ipynb): The loglikelihood function<br>
[Tutorial 3](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial3/tutorial3_concave_likelihood_MNL.ipynb): The concave likelihood function of the linear-additive RUM-MNL model<br>
[Tutorial 4](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial4/tutorial4_Local_vs_global_maxima.ipynb): Local versus global maxima<br>
[Tutorial 5](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial5/tutorial5_Ignoring_panel_structure.ipynb): The impact of ignoring the panel structure of choice data<br>
[Tutorial 6](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial6/tutorial6_Expected_max_utility.ipynb): The expected maximum utility and the LogSum formula<br>

The list of tutorials may be further extended in the future.

## 4. Q&A forum

We use the [Issues](https://github.com/SEN1721TUD/Q3_2025/issues) section as the Q&A platform of this part of the course (Latent class discrete choice modes). This is where you can post questions related to lecture content or technical issues with Python. Before you create a new issue, please make sure that the same question hasn’t already been raised by one of your peers. You can also contribute to ongoing discussions by commenting on existing issues to continue the conversation or provide additional insights. As an example, we have already created the first issue; see [Issues](https://github.com/SEN1721TUD/Q3_2025/issues/1).

To create a new issue (question or problem) in the course repository, follow these steps:

1. Go to the "Issues" section of the course repository.
2. Click on "New issue" in the green button located at the upper right corner of your screen.
3. Add an informative title to your question or problem (e.g., "logit model of BIOGEME does not import in my notebook").
4. Describe your issue clearly and concisely. 
5. Add a topic label from the right-hand side. Click on the gear icon next to "Labels" and choose the label based on the topic of your question. 
6. Click on "Submit new issue" in the green button below the text description.

After that, the lecturer or teaching assistant will reply to your question. Also, you are encouraged to reply to questions posted by your fellow students! If you know how to help your fellow student with an issue, share your thoughts!

## 5. Instructions to set up your Python environment

In this section, we will guide you through the configuration of your Python environment for the Latent Class choice modelling part of the course. You have three options for setting up your environment: Anaconda, PIP or Google Colab. We recommend using Anaconda.

### A. Setting up with Anaconda

Anaconda is a popular platform for managing Python environments. If you’re using Anaconda, it’s recommended to use Python version **3.12.7, 3.11.10, or 3.10.15** to avoid compatibility issues. Other versions, such as **3.9 or  older**, are known to give problems.

Step-by-Step Instructions:


#### Instruction 1: Creating your Python environment in Anaconda
0. **Download and set up the course materials:** Download the SEN1721 course repository from GitHub. Unzip the file into a working directory of your choice. Inside, you’ll find Jupyter notebooks, a requirements.txt file, and datasets. Keep in mind the location of the folder. 

1. **Install Anaconda**: 

   * Go to the [Anaconda download page](https://docs.anaconda.com/anaconda/install/).
   * Choose the appropriate version and click Download.
   * Run the installer and follow the  instructions.

2. **Open Anaconda Navigator**: Go to the “Environments” tab on the left sidebar of the Anaconda Navigator.
   ![img1](./Assets/Anaconda_1.png)

3. **Create a new environment:** Click on the "Create" button at the bottom of the window.

    ![img2](./Assets/Anaconda_2.png)
   
4. **Name your environment and choose Python version**: Enter a name for your new environment (e.g., SEN1721) and select Python version 3.12.7 from the drop-down menu.

    ![img3](./Assets/Anaconda_3_2024.png)
   
5. **Open a terminal using the new environment:** Go to the “Environments” tab in Anaconda Navigator, locate your newly created environment. Then, click the green play button next to it and select Open Terminal.  From this terminal, you can install dependencies
 
   ![img13](./Assets/Anaconda_13.png)

6. **Verify Python version:** You can run `python --version` in the terminal.

   ![img14](./Assets/Anaconda_14.png)

7. **Navigate to the project folder:** Use the `cd` command to navigate to the project folder, for example, `cd …/…/…/Q2_2024`.

   ![img15](./Assets/Anaconda_15.png)

8. **Install requirements file:** Now, you can install the `requirements.txt` file within the activated environment using the following command: `pip install -r requirements.txt`

   ![img16](./Assets/Anaconda_16.png)


9. **Launch JupyterNotebook or JupyterLab and find your workspace**: You will see the notebook, the `requirements.txt` file, and the `data` folder.


   ![img5](./Assets/Anaconda_5.png)
 
   ![img6](./Assets/Anaconda_6.png)

11. **Import all packages:** Run the cells to import all required packages. 
 
   ![img8](./Assets/Anaconda_8.png)
   
   If some packages fail to install, restart the kernel and repeat steps: 7 and 8
 
   ![img9](./Assets/Anaconda_9.png)

12. **Run the notebook**: Once the setup is complete, you’re ready to run your code. The required packages will be installed, and you can proceed with the in-class assignment.
   
#### Instruction 2: Using the existing SEN1221A environment.

If you prefer using the SEN1221A environment, you need to install seaborn to successfully run all the labs.

1.	Open Anaconda Terminal: Click the green play button next to your environment name in the “Environments” tab to open a terminal.

      ![img10](./Assets/Anaconda_10.png)

2. **Create a new environment:** Click on the "Create" button at the bottom of the window.

   ![img11](./Assets/Anaconda_11.png)

3. **Configure the new environment:** Enter a name for your new environment, e.g., "SEN1721," and choose the Python version == “3.12.7" from the drop-down menu.

   ![img12](./Assets/Anaconda_3_2024.png)

4. **Activate the environment:** Click on the green "Play" button on the right side of the environment name to open a terminal where the environment is activated.

   ![img13](./Assets/Anaconda_13.png)

5. **Verify Python version:** You can run `python --version` in the terminal.

   ![img14](./Assets/Anaconda_14.png)

6. **Install Seaborn**: Run the following command in the terminal to install seaborn:

   ``pip install seaborn``

8. **Install and launch JupyterNotebook/JupyterLab**

   ![img17](./Assets/Anaconda_17.png)
   
9. **Import all packages**

   ![img18](./Assets/Anaconda_18.png)

10. **Run the notebook**: Once the setup is complete, you’re ready to run your code. The required packages will be installed, and you can proceed with the in-class assignment.

### B. Setting up with PIP (Python Package Manager)

If you’re not using Anaconda, you can set up your environment using PIP, which is the default package manager for Python.

Step-by-Step Instructions:

1. **Ensure you have Python 3.10 or higher:** Confirm you have Python installed on your system (version 3.10 to 3.12 is recommended). You can check your Python version by running python --version in your terminal. Additionally, ensure you have set up an IPython environment on your computer (Jupyter, VSCode, or any alternatives). 

2. **Clone or download the repository:** Download the course repository from GitHub. Unzip it into a working folder.
3. **Install requirements:**  Install dependencies separate from your current Python version
   
    * Open your terminal and navigate to the course folder.     
    * Create a new "virtual environment" (a separate workspace for this course):
        * Open your command prompt or terminal.
        * Navigate to the directory where you want to create the environment.
        * Type: python -m venv myenv (Replace myenv with a name you choose for your environment).
        * Activate the environment (on Windows, type: myenv\Scripts\activate, on MacOS/Linux, type: source myenv/bin/activate).
        * Install requirements from a File. With your environment activated, navigate to the folder containing the requirements.txt file and run: pip install -r requirements.txt.
    * Install the required packages listed in the requirements.txt file within this environment.
        

4. **Open the notebook**: Launch Jupyther Notebook, JupyterLab, or another IPython tool (e.g., VSCode), and make sure you’re running the notebook inside the newly created virtual environment.

   

