\documentclass[twocolumn]{article}
\usepackage[utf8]{inputenc}
\usepackage{placeins}
\usepackage{colortbl}     
\usepackage{pgf}           
\usepackage{tabularx}
\usepackage[english]{babel}
\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}
\usepackage{pgf}
\usepackage{caption}  % for \captionof
\usepackage{booktabs} % if you want nicer rules
\usepackage{cuted}     % provides the strip environment
\usepackage{cuted}
\usepackage{colortbl,xcolor}
\usepackage{adjustbox}
\usepackage{tabularx}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{listings}
\usepackage[colorlinks=true, allcolors=blue]{hyperref}
\usepackage{authblk}
\usepackage{enumitem}
\usepackage{multicol}
\usepackage{subfig}
\usepackage{booktabs}
\usepackage{float}
\usepackage{rotating}
\usepackage[backend=bibtex, style=numeric]{biblatex}
\addbibresource{sample.bib}
\graphicspath{ {./images/} }
\usepackage{graphicx}
\usepackage[skip=4pt]{caption} 
\setlength{\abovecaptionskip}{4pt}  % space between float and caption
\setlength{\belowcaptionskip}{4pt}
\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
\setlength{\textfloatsep}{4pt plus 1pt minus 1pt}
\setlength{\floatsep}{4pt plus 1pt minus 1pt}
\setlength{\intextsep}{4pt plus 1pt minus 1pt}
\setlength{\dbltextfloatsep}{4pt plus 1pt minus 1pt}
\setlength{\dblfloatsep}{4pt plus 1pt minus 1pt}
\usepackage[utf8]{inputenc}
\usepackage{booktabs}   % for \toprule, \midrule, \bottomrule
\usepackage{caption}    % for nice captions

\title{Optimizing Cognitive Performance Models: A Comparative Study of Bio‑Inspired Hyperparameter Search}
\author[1]{Ivan Nikolov}
\author[1]{Prof. Ilinka Ivanovska}
\affil[1]{Ss. Cyril and Methodius University in Skopje, Faculty of Computer Science and Engineering, Skopje, Macedonia}

\begin{document}
\maketitle

\begin{abstract}
In this paper, we explore how certain environmental variables, such as hours of sleep, type of diet, and frequency of exercises, among others, impact the cognitive performance of an individual. Our goal is to see what kind of correlation we can find between these variables and the score that we have from previously made cognitive function tests, which we can later use to train some sort of machine learning model that can predict the score of individuals without needing to undergo the test. We will examine multiple types of machine learning models, along with multiple types of optimizer functions, to see with which we will have the best performance. The paper will have a focus on the implementation of these biologically inspired optimization algorithms and what kind of effect they have on the final result.\newline  
\end{abstract}

\section{Introduction}
 Cognitive performance—the capacity to process information, solve problems, and remember details—plays a central role in nearly every aspect of human life, from daily decision‐making and workplace productivity to long‐term health outcomes. As lifestyles evolve under the influence of technology, diet, exercise habits, and sleep patterns, understanding how these environmental factors interact to shape cognitive function has become increasingly important. While traditional cognitive assessments provide valuable snapshots of an individual’s abilities, they are time-consuming, resource-intensive, and often impractical for large-scale or continuous monitoring. Consequently, there is growing interest in developing predictive models that can estimate cognitive performance without requiring an in‐person test, using readily available data on personal habits and physiological measures.

Recent advances in machine learning have demonstrated promising results across fields as diverse as medical diagnostics, personalized recommendations, and population‐scale health analytics. However, many standard optimization routines—such as gradient descent or its variants—can become trapped in local minima, especially when the underlying objective landscape is complex or multimodal. Inspired by processes observed in nature, “biological programming” or bio-inspired optimization algorithms (for example, genetic algorithms, particle swarm optimization, and artificial bee colony methods) offer alternative strategies that explore candidate solutions more broadly, potentially yielding better global optima and improved generalization. By embedding these biologically inspired optimizers within standard supervised learning frameworks, one can harness the exploratory power of natural phenomena to fine-tune model parameters, select relevant features, or even guide neural network architectures toward more efficient representations of cognitive data.

\subsection{Related work regarding cognitive function}
One of the newest concerns that the world has is the rapidly aging population  and the onslaught of new diseases that show up with age.  In Murman et al \cite{Murman2015-cw} they discuss about the types of cognitive abilities and how they are affected by age. The common way the abilities are divided is 
\begin{itemize}
    \item  Crystallized abilities are the cumulative skills
and memories that result from cognitive processing that occurred in the past, typically in the form of acquired knowledge. Tests of general
knowledge (e.g., reading comprehension, math,
science), historical information, and vocabulary
would reflect crystallized abilities.
\item Fluid abilities require cognitive processing at the time of
assessment and reflect manipulation and transformation of information to complete the test. 
\end{itemize}
Tests of fluid abilities require the subject to
attend to one’s environment and process new
information quickly to solve problems. Multiple
cross-sectional studies have shown that there is
an improvement in crystallized abilities until
approximately age 60 followed by a plateau until
age 80, and there is steady decline in fluid
abilities from age 20 to age 80.
For example, there is a nearly linear decline in
processing speed, a fluid ability, with a -0.02
standard deviation decline per year in one very
large study. \newline\newline
Cognitive abilities can be also divided into
several specific cognitive domains \cite{lezak2012neuropsychological} including
attention, memory, executive cognitive function, 
language, and visuospatial abilities. Each
of these domains has measurable declines with
age. For each of these domains, a subject must
first perceive the stimulus, process the information, and then respond. Both sensory perception and processing speed decline with age, thus
impacting test performance in many cognitive
domains.
\newline\newline
In addition to these
change in sensory perception, there is a clear
decline in processing speed in advancing age
with older adults performing these activities more slowly than younger adults.\cite{Salthouse2010-uy}This slowing
of processing speed causes worse test performance on many types of tasks that involve a
timed response. \newline\newlinee 

In the Whitehall II study, Jane E Ferreri et al \cite{Ferrie2011-ah} experiment and document the cognitive changes that happen when the sleep duration changes. They noticed that there is an on average a 3 to 8 year increase in age of the participant regarding the cognitive test that they make in comparison to the regular 6-7-8 hour interval of sleep. The severity of the age increase in the cognitive function depends on several factors. Some of them are the socio-economic background of the individual, the levels of stress and depression, the job that the individual has. Also another interesting observation that they had made is that if there is an increase in sleep from 7 or 8 hours per night, it is associated with poorer cognitive function scores for all tests in comparison to having a reduced number of hours slept.\newline\newline
Sleep duration has been found to be associated with a wide
range of quality of life measures, such as social functioning,
health outcomes, such as poor mental health, obesity, type 2
diabetes, cardiovascular disease and early death. \cite{Baldwin2001-vw} \cite{Groeger2004-xn} 
All of these factors are interconnected, forming a feedback loop with negatively effect cognitive functioning.

Obesity as we all know is on an upward trend around the world. There is compelling evidence that obese adults
perform worse than normal weight counterparts on
measures of learning and memory . In a large
sample of otherwise healthy individuals Gunstad
and colleagues \cite{Gunstad2006-sf} found lower verbal list-learning,
delayed recall, and recognition scores for participants
with a body mass index (BMI) above 30 kg/m2 compared to normal weight counterparts.
There is substantial evidence linking obesity in
adulthood with elevated dementia risk in later life. Whitmer  et al \cite{Whitmer2008-ib}
study found that abdominally obese adults exhibit up
to 3 times greater risk for Alzheimer’s disease and up
to 5 times greater risk for vascular dementia. 
This type of cognitive decline is somewhat reversible with the help of weight loss and regular exercise, since it activates more parts of the brain and makes the person more disciplined.\cite{Colcombe2003-ti} Regular exercise also helps with regulating  blood pressure which has a positive effect on cognitive functions. \cite{Smith2010-zz} \cite{Brinkworth2009-bb}.

Ruxton in his paper, The impact of caffeine on mood, cognitive function, performance and hydration: a review of benefits and risks\cite{Ruxton2008-caffeine} concludes that moderate caffeine consumption (approximately 200--400 mg per day) can enhance alertness, vigilance, working memory, and physical performance, particularly under conditions of fatigue or sleep deprivation. Caffeine also contributes positively to mood, reducing fatigue and improving general well-being. Contrary to common concerns, the review finds no evidence that moderate caffeine intake leads to dehydration, even during physical exertion. However, excessive consumption may lead to side effects such as anxiety, restlessness, disrupted sleep, and dependence-related withdrawal symptoms. Individual responses to caffeine can vary significantly due to genetic and physiological differences. Overall, the paper suggests that when consumed in moderation, caffeine offers notable cognitive and physical benefits with minimal risk.

The consequences excessive screen time may pose on learning and memory may directly affect academic performance in children, adolescents, and young adults \cite{Madigan2019-gh}.  In our dataset we do have individuals which will be effected by this but this is more of a problem that is in the process of making and hasn't reached its maturity yet, as it takes time for it to effect a large part of the population. Studies exploring the relationship between excessive screen time (e.g., social media) and
mental health problems strongly indicated time spent on digital media was associated with increased symptoms of psychopathologies, specifically those of anxiety, depression, and attention deficit disorders Montagni et al. \cite{Montagni2016-jt}.
In their paper,  Reime Jamal Shalash et al \cite{Shalash31122025} write about the cognitive decline that is present in remote workers that were exposed to long hours of screen time, that started during the pandemic. They had lower cognitive scores in the information speed processing, working memory, calculation, and attention domains.
\subsection{Related work regarding machine learning models for cognitive function}
In their paper \cite{rykov2024predicting} , the authors analyzed data from a clinical trial involving 30 individuals aged 50–70 diagnosed with mild cognitive impairment (MCI). During the intervention, partici-
pants were provided with Empatica-E4, a medical-grade
sensor-equipped wrist device that collects physiological
signals, and instructed to wear it as much as possible, as per trial protocpl participants were not required to wear
it around the clock. All participants were given cognitive assessments at two time points, one at baseline a week before the intervention began and a week after the intervention began. The Neuropsychological Test Battery (NTB) was used to assess  the cognitive function.

They trained the models using 3 datasets:They used the age and the sex alone for the training and used this models results as a baseline; They combined the digital biomarkers + age and sex;Just the digital biomarkers.
They used 3 different ML algorithms, including ElasticNet regression, RandomForest regression and XGBoost regression. OUt of all of the models, the best results were from the Random Forestu using 15 features, with a Pearson r coeficient of 0.77 for predicting intra-individual changes in NTB scores.

 Shreya Verma et al \cite{VERMA20252144} in their study aimed to predict cognitive performance, measured by reaction time in a modified Eriksen flanker task, using a wide range of health and behavioral indicators in a diverse sample of 374 adults aged 19–82. Researchers employed several machine learning models—including decision trees, random forest, AdaBoost, XGBoost, gradient boosting, and regularized regressions—with extensive hyperparameter tuning and cross-validation. Input features spanned demographics, body metrics, dietary indices (e.g., HEI, DASH, Mediterranean, MIND), physical activity, and blood pressure measurements. Model performance was evaluated using mean absolute error (MAE) and mean squared error (MSE).

The random forest model outperformed all others, achieving the lowest prediction errors (testing MAE: 0.78 ms). Feature importance analysis revealed that age was the most influential predictor, followed by diastolic and systolic blood pressure, BMI, and diet quality (particularly Healthy Eating Index). In contrast, demographic factors like sex and ethnicity had negligible predictive power. These findings suggest that simple, routinely collected health metrics—especially cardiovascular and metabolic indicators—can effectively inform machine learning models for cognitive performance prediction, opening the door for scalable, personalized strategies in cognitive health monitoring and early intervention.

    




\section{Materials and Methods}
\subsection{Dataset and data analysis}
First and foremost, we wish to talk about the dataset that we will be using. It can be found on Kaggle, under the name Human Cognitive Performance Analysis. It consists of more than 80 000 entries with a wide range of individuals for examination. The dataset has been constructed in a way that the information has been sampled from multiple cognitive performance surveys, so there shouldn't be much of an intrinsic bias to the information. There are 11 columns. The columns of interest are the following (their subsequent plots,distributions and more detailed analysis are in the appendix for clarity):
\begin{itemize}
    \item \textbf{Age} – 18 to 59 years old, average 38.5; evenly distributed with no significant outliers.
    \item \textbf{Sleep Duration} – Average 7.01 hours; ranges from 4 to 10 hours.
    \item \textbf{Stress Level} – Average 5.49; fairly symmetric across the 1–10 scale.
    \item \textbf{Screen Time} – Average 6.5 hours/day; includes both leisure and work use.
    \item \textbf{Caffeine Intake} – Average intake equals about 2.6 cups of coffee per day.
    \item \textbf{Reaction Time} – Average around 400 ms; reflects age distribution, no outliers.
    \item \textbf{Memory Score} – Scored 0–100; well-distributed, ideal for modeling.
    \item \textbf{Gender} – Balanced: 48\% male, 48\% female, 4 other.
    \item \textbf{Diet Type} – ~60\% non-vegetarian, ~30\% vegetarian, ~10\% vegan.
    \item \textbf{Exercise Frequency} – ~40\% low, ~40\% medium, ~20\% high.
    \item \textbf{Prediction Scores} – Model trained on real score; AI prediction used for comparison, with an average error of 2.4.
\end{itemize}



\subsection{Feature extraction}

Based on the correlation matrix provided in the appendix, most variables show little to no correlation with each other. However, several variables do exhibit a notable association with the Cognitive Score:

\begin{itemize}
    \item \textbf{Positive correlations:}
    \begin{itemize}
        \item Sleep Duration: $\rho = 0.151$
        \item Memory Test Score: $\rho = 0.364$
    \end{itemize}

    \item \textbf{Negative correlations:}
    \begin{itemize}
        \item Caffeine Intake: $\rho = -0.123$
        \item Daily Screen Time: $\rho = -0.199$
        \item Stress Level: $\rho = -0.228$
        \item Reaction Time: $\rho = -0.818$
    \end{itemize}
\end{itemize}

In addition to correlation analysis, we applied Ridge Regression, Decision Tree and Mutual Information models to assess feature importance. From these models, the most influential variables in predicting the cognitive score (in descending order) were: Reaction Time; Memory Test Score; Exercise Frequency; Stress Level; Daily Screen Time; Sleep Duration; Caffeine Intake; Diet Type; Age; Gender.


Regarding Principal Component Analysis (PCA), the results showed that each PCA component contributed almost equally to the overall variance, with lower expressiveness at the 8th,9th and 10th PCA. The noticable knee was at the 7th PCA, where there was an exmplained  cumulative variance ratio above 90%.
In light of the analysis that we have done, we will test out the algorithms while using 5 ,7 and 10 variables. \newline 

\subsection{Experiments}
In our experiments, we used several machine learning algorithms, including Random Forest Regressors, Extra Trees, XGBoost, and fully connected multi-layered neural networks. On all of these machine learning algorithms, we used cross-validation during the training process and had a withheld test dataset for a final evaluation of the trained model . For the optimization  algorithms we used Grid Search, Random Search, Bayes Search, Hill Climbing,Simulated Annealing, Genetic Algorithms, Particle Swarm Optimization, Artifical Bee Colony and Optuna . The specific hyper-parameters that were being tuned were specific for each model and discused in the relative section. The time for training and evaluating varied, ranging from couple of minutes to a couple of hours. Each model was trained three times using each  data set. All of the experiments were done using locally on  Lenovo LOQ-15IRH8, using a  13th Gen Intel(R) Core(TM) i7-13620H processor with 20 threads.
\subsection{Hyperparameter search spaces}
As we have previously stated, we will be training 4 machine learning models, with the list of optimization algorithms. The hyperparameter spaces for each model are the following.
\begin{table}[h!]
\centering
\begin{tabular}{|l|l|}
\hline
\textbf{Hyperparameter}       & \textbf{Search Space} \\ \hline
\texttt{max\_depth}           & $[5,\,10]$            \\ \hline
\texttt{min\_samples\_leaf}   & $[5,\,15]$            \\ \hline
\texttt{n\_estimators}        & $[50,\,300]$          \\ \hline
\texttt{min\_samples\_split}  & $[2,\,20]$            \\ \hline
\end{tabular}
\caption{Hyperparameter search space for Extra Trees and Random Forest Models}
\label{tab:extra_trees_hyperparams}
\end{table}



\begin{table}[h!]
\centering
\begin{tabular}{|l|l|}
\hline
\textbf{Hyperparameter}   & \textbf{Search Space}  \\ \hline
\texttt{n\_estimators}     & $[100,\,300]$          \\ \hline
\texttt{max\_depth}        & $[3,\,12]$             \\ \hline
\texttt{learning\_rate}    & $[0.01,\,0.30]$        \\ \hline
\texttt{subsample}         & $[0.50,\,1.00]$        \\ \hline
\end{tabular}
\caption{Hyperparameter Search Space for the MLP Model}
\label{tab:param_space}
\end{table}
\begin{table}[H]
\centering
\begin{tabular}{|l|l|}
\hline
\textbf{Hyperparameter}         & \textbf{Search Space}                                      \\ \hline
Number of layers                & $[2,6]$                                            \\ \hline
Units per layer                 & $[16,\,128]$                                              \\ \hline
Learning rate\,init             & $[1\times10^{-4},\,1\times10^{-2}]$     \\ \hline
Batch size                      & $[16,128]$                                         \\ \hline
\end{tabular}
\caption{Hyperparameter search space for the MLP model.}
\label{tab:mlp_hyperparams}
\end{table}
\onecolumn
\section{Results}
\subsection{Tables}
%extra trees
\begin{table}[H]
  \centering
  \captionof{table}{Summary of Extra Trees Tuning Results using 5 features }
  \label{tab:xgb_results_5features_extratrees}
    \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                             &    23.58              & 0.9494                      & 0.9494           & 26.8628            \\
    \hline
    Random                           &    93.89              & 0.9498                      & \textbf{0.9498}         & 26.6465            \\
    \hline
    Bayes                            &   175.09              & 0.9494                      & 0.9494           & 26.8628            \\
    \hline
    Hill Climbing                    &   172.63              & 0.9432                      & 0.9412           & 31.1831            \\
    
    \hline
    Simulated Anealing               &  1190.59              & 0.9431                      & 0.9429           & 30.2914            \\
    \hline
    Particle Swarm Optimization      &    42.62              & 0.9495                      & 0.9486           & 27.2911            \\
    \hline
    Artificial Bee Colony            &  1899.90              & \textbf{0.9527}             & 0.9495           & 26.7811            \\
    \hline
    Genetic Algorithms               &  1125.50              & 0.9503                      & 0.9496           & 26.7374   \\
    \hline
    
    Optuna                           &   687.95              & 0.9502                      & \textbf{0.9498}  & \textbf{26.6378}            \\
    \hline
                                     & 5412.05              & ABC                         & Random..  & Optuna       \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of Extra Trees Tuning Results using 7 features}
  \label{tab:xgb_results_extratrees_all}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross-validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                             &      6.76             & 0.9602                      & 0.9597           & 21.3941            \\
    \hline
    Random                           &     86.67             & 0.9604                      & 0.9602           & 21.0923            \\
    \hline
    Bayes                            &    157.66             & 0.9603                      & 0.9598           & 21.3455            \\
    \hline
    Hill Climbing                    &    151.21             & 0.9497                      & 0.9484           & 27.3707            \\
    \hline
    Simulated Anealing               &   1976.85             & 0.9495                      & 0.9461           & 28.6007            \\
    \hline
    
    
    Artificial Bee Colony            &   2397.58             & \textbf{0.9629}             & 0.9598           & 21.3402      
    \\ 
    \hline
    Particle Swarm Optimization      &     50.30             & 0.9607                      & 0.9591           & 21.6779            \\
    \hline
    Genetic Algorithms               &   1281.88             & 0.9609                      & \textbf{0.9605}  & \textbf{20.9399}  \\ \hline  
    Optuna                           &    554.42             & 0.9608                      & 0.9603           & 21.0422       \\    
    \hline
    
                                    &  6522.12            & ABC                         & GA               & \textbf{GA}        \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of Extra Trees Tuning Results using 10 features}
  \label{tab:xgb_results_extratrees_10f}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                             &     8.87           & 0.9599                   & 0.9600          & 21.2286           \\
    \hline
    Random                           &     60.45          & 0.9602                     & 0.9603         & 21.0712          \\
    \hline
    Bayes                            &     55.48          & 0.9600                     &  0.9600          & 21.2006          \\
    \hline
    Hill Climbing                    &     65.31           & 0.9480                   &  0.9476           & 27.7984            \\
    \hline
    Simulated Anealing               &     2052.96            & 0.9493                   & 0.9476           & 27.8042           \\
     \hline
   
    Artificial Bee Colony            &     2716.94            & 0.9635             & 0.9602          & 21.1414            \\
    \hline
     Particle Swarm Optimization             &     62.34183           & 0.9604                 & 0.9589 &  21.8163   \\
    \hline
    Genetic Algorithms               &     1543.94            & 0.9608                    & \textbf{0.9606}  & \textbf{20.9258}   \\
    
    \hline
    Optuna              &     1415.35           & \textbf{0.9609}                   & 0.9605  &  20.9331   \\
    
    \hline
                                     &    7981.57           & Optuna                         & GA               & GA        \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
% random forest
\begin{table}[H]
  \centering
  \captionof{table}{Summary of RandomForest Tuning Results using 5 features}
  \label{tab:xgb_results_3features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}           & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                    &   17.57               & 0.9509                      & \textbf{0.9497}           & 26.6998            \\
    \hline
    Random                  &   93.46               & 0.9508                      & \textbf{0.9497}           & 26.7014            \\
    \hline
    Bayes                   &  206.01               & 0.9509                      & \textbf{0.9497}           & 26.6998            \\
    \hline
    
    Hill Climbing                    &  464.99               & 0.9440                      & 0.9422           & 30.6704            \\
    \hline
    Simulated Anealing                       & 3597.11               & 0.9435                      & 0.9422           & 30.6544            \\
    
    \hline
    
    
    Artificial Bee Colony                     & 5665.02               & \textbf{0.9595}                      & \textbf{0.9497}           & \textbf{26.6859}           \\
    \hline
    Particle Swarm Optimization                      &  318.39               & 0.9505                      & \textbf{0.9497}           & 26.6967            \\
    
    \hline
    Genetic Algorithms                       & 1312.07               & 0.9509                      & \textbf{0.9497}           & \textbf{26.6859}           \\
    
    \hline
    Optuna                 &  141.36               & 0.9506                      & \textbf{0.9497}           & 26.6986            \\
    \hline
    
                            & 11815.98             & ABC                         & Grid..  &  ABC..       \\
    \hline
                            & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of RandomForest Tuning Results using 7 features}
  \label{tab:xgb_results_5features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                             &   22.05               & 0.9678                      & \textbf{0.9659}           & 18.1182            \\
    \hline
    Random                           &  127.49               & 0.9676                      & \textbf{0.9659}           & \textbf{18.1130}            \\
    \hline
    Bayes                            &  240.48               & 0.9678                      & \textbf{0.9659}           & 18.1182            \\
    \hline
    
    Hill Climbing                    &  693.66               & 0.9555                      & 0.9528           & 25.0352            \\
    \hline
    Simulated Annealing              & 5166.85               & 0.9547                      & \textbf{0.9659}           & 24.9977            \\
   
   
    \hline
    Artificial Bee Colony            & 8643.85               & \textbf{0.9744}                      & \textbf{0.9659}           & 18.1182            \\
    
     \hline
    Particle Swarm Optimization      &  544.97               & 0.9674                      & \textbf{0.9659}           & 18.1132            \\
    \hline
    Genetic Algorithms               & 1777.13               & 0.9678                      & \textbf{0.9659}           & 18.1182            \\
    \hline
    Optuna                           &  791.45               & 0.9674                      & 0.9658           & 18.1380            \\
    \hline
                                     & 18007.93              & ABC                         & ABC ...             & Random            \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of RandomForest Tuning Results using 10 features}
  \label{tab:xgb_results_4features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                             &   25.98               & 0.9677                      & \textbf{0.9658}           & 18.1251            \\
    \hline
    Random                           &  146.64               & 0.9676                      & \textbf{0.9658}           & \textbf{18.1218}            \\
    \hline
    Bayes                            &  269.29               & 0.9677                      & \textbf{0.9658}           & 18.1251            \\
    
    \hline
    Hill Climbing                    &  757.69               & 0.9557                      & 0.9529           & 24.9800            \\
    \hline
    Simulated Annealing              & 6077.53               & 0.9545                      & 0.9529           & 25.0051            \\
    
    \hline
    Artificial Bee Colony            & 9420.29               & \textbf{0.9744}                     & \textbf{0.9658}          & 18.1251            \\
    \hline
    Particle Swarm Optimization      &  596.53               & 0.9674                      & \textbf{0.9658}           & \textbf{18.1218}                 \\
    \hline
    Genetic Algorithms               & 2042.45               & 0.9677                      & \textbf{0.9658}          & 18.1251            \\
    \hline
    Optuna                           &  867.60               & 0.9673                      & 0\textbf{0.9658}          & 18.1406            \\
    \hline
                                     & 20 204              & ABC                         & ABC ...         &  PSO...           \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}

% XGboost
\begin{table}[H]
  \centering
  \captionof{table}{Summary of XGBoost Tuning Results using 5 features}
  \label{tab:xgb_results_5features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}           & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                    &   29.08               & 0.9603                      & 0.9601           & 21.1609            \\
    \hline
    Random                 &   19.17               & 0.9615                      & 0.9613           & 20.5219            \\
    \hline
    Bayes                  &   52.42               & 0.9608                      & 0.9608           & 20.8080            \\
    \hline
    
    Hill Climbing                    &  157.14               & 0.9607                      & 0.9608           & 20.8027            \\
    \hline
    Simulated Anealing                     & 1266.54               & \textbf{0.9617}                      & 0.9613           & 20.5172            \\
    \hline
    
    
    
    Artificial Bee Colony                     &  179.00               & 0.9615                      & \textbf{0.9615}           & \textbf{20.4140}            \\
    \hline
    Particle Swarm Optimization                   &   32.40               & 0.9607                      & 0.9610           & 20.7177            \\
    \hline
    Genetic Algorithms                      & 1227.75               & 0.9616                      & 0.9614           & 20.4653            \\
    
    \hline
    Optuna                 &  122.74               & 0.9616                      & 0.9614           & 20.4988            \\
    \hline                        & 3086.24               & SA                          & ABC              & ABC                \\
    \hline
                            & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of XGBoost Tuning Results using 7 features}
  \label{tab:xgb_results_7features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}           & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                    &   81.94                & 0.9961                      & 0.9964           & 1.9008             \\
    \hline
    Random                  &   93.07                & 0.9962                      & 0.9970           & 1.6064             \\
    \hline
    Bayes                   &  105.75                & 0.9961                      & 0.9965           & 1.8515             \\
    \hline
    Hill Climbing           &  210.77                & 0.9964                      & 0.9968           & 1.6849             \\
    \hline
    Simulated Anealing      & 2752.56                & 0.9971                      & 0.9975           & 1.3412             \\
    \hline
    Artificial Bee Colony   &  170.27                & 0.9977                      & 0.9981           & 1.0014             \\
    \hline
    Particle Swarm Optimization & 80.68              & 0.9970                      & 0.9975           & 1.3329             \\
    \hline
    Genetic Algorithms      & 1284.91                & 0.9972                      & 0.9976           & 1.2958             \\
    \hline
    Optuna                  &  215.65                & \textbf{0.9980}                      & \textbf{0.9983}           & \textbf{0.9251}             \\
    \hline
                            & 4995.6                & Optuna     & Optuna           & Optuna             \\
    \hline
                            & \textbf{Total (s)}     & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of XGBoost Tuning Results using 10 features}
  \label{tab:xgb_results}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}           & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                    &   79.43           & 0.9967                      & 0.9967           & 1.7259             \\
    \hline
    Random                  &  298.04           & \textbf{0.9979}                      & 0.9982           & 0.9495             \\
    \hline
    Bayes                   &  462.65           & 0.9977                      & 0.9981           & 1.0015             \\ \hline
    Hill Climbing           &  209.63           & 0.9963                      & 0.9968           & 1.6990             \\
    \hline
    Simulated Anealing                       & 2359.03           & 0.9971                      & 0.9974           & 1.3761             \\
    \hline
    Artificial Bee Colony                     &  193.29           & 0.9974                      & 0.9979           & 1.0883             \\
    \hline
    Particle Swarm Optimization                     &  356.53           & 0.9978                      & 0.9982           & 0.9377             \\
    \hline
    Genetic Algorithms                      & 1483.29           & 0.9971                      & 0.9976           & 1.2484             \\
    \hline
    Optuna                  &  129.84           & \textbf{0.9979}                      & \textbf{0.9983}           & \textbf{0.9047}             \\
    \hline
    
                             & 5571,73                  &    Optuna ...                         &  Optuna                &   Optuna                 \\
    \hline
                             & \textbf{Total (s)}    & \textbf{Best}              & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
% MLP



\begin{table}[H]
  \centering
  \captionof{table}{Summary of MLP Tuning Results using 5 features}
  \label{tab:xgb_results_2features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\ \hline
    Grid                             &   201.06              & 0.9630                      & 0.9624           & 19.9249            \\ \hline
    Random                           &  1175.24              & 0.9631                      & \textbf{0.9627}           & \textbf{19.7659 }           \\ \hline
    Bayes                            &   569.75              & 0.9620                      & 0.9626           & 19.8274            \\ \hline
    Hill Climbing                    &  1467.71              & 0.9629                      & 0.9624           & 19.9254            \\ \hline
    Simulated Annealing  &    13200.83      &  \textbf{0.9999 }                      & 0.9620          & 20.1739           \\ \hline
    Particle Swarm Optimization      &  1478.72              & 0.9627                      & 0.9622           & 20.0617            \\ \hline
     Artificial Bee Colony            & 10481.43              & 0.9628                      & 0.9615           & 20.4177            \\ \hline
    Genetic Algorithms               &  4699.91              & 0.9632                      & \textbf{0.9627 }          & 19.7829            \\ \hline
   Optuna               &  9720.23              & 0.9996                      & 0.9624         & 19.9286           \\ \hline
    
    
    \multicolumn{1}{|r|}{}           & 42994.89   &  SA             & GA &  Random\\ \hline
    \multicolumn{1}{|r|}{}           & \textbf{Total (s)}    & \textbf{Best}         & \textbf{Best}     & \textbf{Best} \\ \hline
  \end{tabular}
\end{table}
\begin{table}[H]
  \centering
  \captionof{table}{Summary of MLP Tuning Results using 7 features}
  \label{tab:xgb_results_2features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\ \hline
    Grid                             &   153.58              & \textbf{1.0000}                    &\textbf{1.0000}          & 0.0030             \\
    
    \hline
    Random                           &   640.41              & \textbf{1.0000}                     & \textbf{1.0000}          & 0.0016             \\
    \hline
    Bayes                            &   287.40              & 0.9834                      & \textbf{1.0000}           & 0.0133             \\ \hline
     Hill Climbing                    &  1508.04              & 0.9629                      & \textbf{1.0000}           & 0.0171             \\
      \hline
     Simulated Annealing                   &  5583.23                &  0.9999                    & \textbf{1.0000}         & 0.0171             \\
    \hline
    Particle Swarm Optimization      &  1242.15              & \textbf{1.0000}              & 0.9999           & 0.0445             \\
    \hline
     Artificial Bee Colony            &  3417.23              & \textbf{1.0000}                     & 0.9998           & 0.0915             \\
    \hline
    Genetic Algorithms               &  7088.91              & \textbf{1.0000}                     & \textbf{1.0000}         & \textbf{0.0011 }            \\
    \hline
   
    
    Optuna                           &  1079.93              & \textbf{1.0000}                     & \textbf{1.0000}           & 0.0163             \\
    \hline
    

                                     & 21 000,88             & Grid... & Grid...   & GA        \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}

\begin{table}[H]
  \centering
  \captionof{table}{Summary of MLP Tuning Results using 10 features}
  \label{tab:xgb_results_3features}
  \begin{tabular}{|l|r|r|r|r|}
    \hline
    \textbf{Algorithm}                    & \textbf{Duration (s)} & \textbf{Cross‑validated R\textsuperscript{2}} & \textbf{Test R\textsuperscript{2}} & \textbf{Test RMSE} \\
    \hline
    Grid                             &   143.92              & \textbf{1.0000}                      & \textbf{1.0000}           & 0.0016             \\
    \hline
   
    Random                           &   502.31              & \textbf{1.0000}                      & \textbf{1.0000}           & 0.0059             \\
    \hline
    Bayes                            &   610.26              & 0.9983                     & 0.9998           & 0.0853             \\
    \hline
    Hill Climbing                    &  3543.07              & 0.9628                      & \textbf{1.0000}           & 0.0157             \\

    \hline
    Simulated Annealing & 6371.00 & \textbf{1.0000} &  0.9999 & 0.0041 \\ 
    \hline
    Artificial Bee Colony            &  3411.09              & \textbf{1.0000}                    & 0.9994           & 0.2949             \\
    \hline

    Particle Swarm Optimization      &   911.35              & 0.9999                      & \textbf{1.0000}           & 0.0104             \\
    \hline
    
    
    Genetic Algorithms               &  6755.86              & \textbf{1.0000}                      & \textbf{1.0000}          & \textbf{0.0011 }            \\
    \hline
    Optuna                           &  1911.02              & \textbf{1.0000}                      & \textbf{1.0000}          & 0.0097             \\
    \hline
                                     &24 159.88             & Grid...  & Grid..   & GA        \\
    \hline
                                     & \textbf{Total (s)}    & \textbf{Best}               & \textbf{Best}    & \textbf{Best}      \\
    \hline
  \end{tabular}
\end{table}
\twocolumn
\subsection{Analysis}
In this section we have all of the tables regarding the results of the experiments. In total we trained 108 different models using the different combinations possible.\newline\newline  We searched the hyper parameter space for  171752.87 seconds, or 2862.54 minutes or 47.71 hours or  almost 2 days straight. This time only includes the models that returned some sort of result, it does not count the failed searches. Also it is important that sometimes the dataset was split in to smaller datasets regarding the algorithm, for example Hill Climbing required a new starting point each time it started and it had the dataset divided by the number of times the algorithm started over from a new random point or used some certain mechanisms for early stopping since there was no longer any significant improvement.\newline
\newline
From all of the tables we can conclude that all of the models that have been trained do provide desirable results, but some are better than others.\newline 
\begin{table}[H]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Average Metric} & \textbf{Value} \\
\hline
Cross (5) & 0.9486 \\
Test (5) & 0.9478 \\
RMSE (5)  & 27.6993 \\
\hline
Cross (7) &  0.9584 \\
Test (7) &  0.9571 \\
Rmse (7) &  22.7559 \\
\hline
Cross (10) &   0.9581 \\
Test (10) & 0.9573 \\
Rmse (10)  & 22.6577 \\
\hline
Avg Cross & 0.9550\\
Avg Test & 0.9541\\
Avg RMSE & 24.3710\\
\hline
\end{tabular}
\caption{Evaluation Metrics for Extra Trees}
\label{tab:evaluation_metrics}
\end{table}
The ET models ran 5.53 hours or 0.2 days. The RF models 13.9 hours or 0.57 days. The XGBoost models ran for 
3.79 hours or 0.16 days. The MLP models ran for 24.5 hours and 1.02 days.\newline 

The ET models performed the poorest out of all of the models, with an average test R\textsuperscript{2} score of 0.9541.
After the ET models, come the RF models with 0.9584 ,XGB models with  0.9854  and the MLP models with  0.9874. As the models grow in complexity so do the results and their respective run times.


From the results we can notice a major jump that is present in all of the models, but it gets bigger the more complex the model is. The jump is the number of features. The models that trained on just 5 under perform, where as the 7 and 10 feature models give similar or almost identical results. So from our analysis we were correct to assume that the 7 feature PCA is enough for the model to give us the best results.
\begin{table}[h!]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Average Metric} & \textbf{Value} \\
\hline
Cross (5) & 0.9502 \\
Test (5) & 0.9480 \\
RMSE (5)  & 27.5770 \\
\hline
Cross (7) &  0.9656 \\
Test (7) &  0.9644 \\
Rmse (7) &  19.6522 \\
\hline
Cross (10) &   0.9656 \\
Test (10) & 0.9629 \\
Rmse (10)  & 19.6522 \\
\hline
Avg Cross & 0.9605\\
Avg Test & 0.9584\\
Avg RMSE & 22.2938\\
\hline
\end{tabular}
\caption{Evaluation Metrics for Random Forest}
\label{tab:evaluation_metrics}
\end{table}
\begin{table}[h!]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Average Metric} & \textbf{Value} \\
\hline
Cross (5) & 0.9612 \\
Test (5) & 0.9611 \\
RMSE (5)  & 20.6563 \\
\hline
Cross (7) &  0.9969 \\
Test (7) &  0.9973 \\
Rmse (7) &  1.4378 \\
\hline
Cross (10) &   0.9973 \\
Test (10) & 0.9977 \\
Rmse (10)  & 1.2146 \\
\hline
Avg Cross & 0.9851\\
Avg Test & 0.9854\\
Avg RMSE & 7.7695\\
\hline
\end{tabular}
\caption{Evaluation Metrics for XGBoost}
\label{tab:evaluation_metrics}
\end{table}
\begin{table}[h!]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Average Metric} & \textbf{Value} \\
\hline
Cross (5) & 0.9710 \\
Test (5) & 0.9623 \\
RMSE (5)  & 19.9787 \\
\hline
Cross (7) &  0.9940 \\
Test (7) &  1.0000\\
Rmse (7) &  0.0228 \\
\hline
Cross (10) &   0.9957 \\
Test (10) & 0.9999 \\
Rmse (10)  & 0.0476 \\
\hline
Avg Cross & 0.9869\\
Avg Test & 0.9874\\
Avg RMSE & 6.682733333\\
\hline
\end{tabular}
\caption{Evaluation Metrics for MLP}
\label{tab:evaluation_metrics}
\end{table}
From the results we can also notice that there is overfitting present on the dataset and it is more noticeable when we look at the MLP models. Alot of the algorithms converge and return almost perfect results i.e cross validation and test results with 0.999 or 1 R\textsuperscript{2} score and RMSE below 0. Out of all of the models the best one to be used in practical purpouses should be the XGBoost models, regardless of feature sizes, because they give the best time and result training ratio for all practical and research purposes. 

From all of the optimizer algorithms, the algorithms that gave the best results in each category are:
\begin{table}[H]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Best algo.} & \textbf{Count}\\ 
\hline
ABC & 7\\
\hline
GA & 8\\
\hline
GA & 5\\
\hline
\end{tabular}
\caption{The best algorithms for the CV score, the Test Score and the Test RMSE.}
\label{tab:evaluation_metrics}
\end{table}
From the previous table we can conclude that the best algorithm for the trainnig of these models is the GA, which consistently yielded the best results from all of the others. An honorable mention is Optuna, which was second in every category and with its faster results and early stopping should be taken in to consideration. \newline
\section{Conclusion}
Summarizing over 108 trained models and nearly 48 hours of cumulative hyperparameter search, our results demonstrate a clear hierarchy of algorithmic efficiency and predictive power. Extra Trees delivered the fastest runtimes (~5.5 h total) but lagged in accuracy (average Test R² ≈ 0.9541), while Multilayer Perceptrons achieved perfect in-sample fits (R² ≈ 1.0000) at the expense of severe overfitting and the longest tuning time (~24.5 h). Random Forest occupied the mid‑ground (Test R² ≈ 0.9584, ~13.9 h), and XGBoost struck the optimal balance—achieving Test R² \textgreater{} 0.985 in under 4 h.  

Genetic Algorithms emerged as the most consistent optimizer in 2 categories, followed closely followed by Artificial Bee Colony. Optuna should not be forgotten since it was second‑place in every category with a drastic reduction in run time and almost the same end results as t he previous two algorithms. Notably, the 7‑feature PCA projection sufficed to capture the bulk of the signal, with negligible gains when expanding to 10 features.  

Collectively, these findings suggest that an XGBoost model—tuned via Genetic Algorithms or Optuna on a 7‑dimensional feature set—offers the best trade‑off of speed, robustness, and generalization for cognitive‑state prediction.

\paragraph{Limitations}
The reliance on self-reported lifestyle data may introduce recall bias and subjectivity, witch changes with how people few their selves and their habits. Models were evaluated on a static dataset; their performance over time remains to be assessed.

\paragraph{Future Work}
Future studies should explore additional bio-inspired and hybrid optimization strategies and validate against longitudinal or external cohorts. Integrating real-time physiological signals (e.g., heart rate variability) may further enhance predictive accuracy.

\paragraph{Practical Implications}
\begin{itemize}
\item \textbf{Mobile Health Apps:} A cross-platform application can collect user and wearable data to compute a daily cognitive health score with personalized recommendations.
\item \textbf{Corporate Wellness:} Embedding these models into employee wellness programs can produce dashboards and guide group interventions, such as stress-reduction workshops.
\item \textbf{Clinical Decision Support:} Integration within electronic health records can alert clinicians to early cognitive decline, prompting timely referrals.
\end{itemize}

By combining robust hyperparameter optimization with practical deployment pathways, our approach establishes a scalable framework for data-driven cognitive health monitoring and personalized intervention strategies.





\printbibliography
\onecolumn
\appendix
\section{Appendix}
\addcontentsline{toc}{section}{Appendix}
\subsection{Correlation Matrix}
\definecolor{myyellow}{RGB}{255, 255, 0}
\definecolor{mypurple}{RGB}{128, 0, 128}

\newcommand{\colorCell}[1]{%
  \pgfmathsetmacro{\val}{#1}%
  \pgfmathsetmacro{\absval}{abs(\val)}%
  \pgfmathsetmacro{\colorpct}{min(\absval,1)*100}%
  \ifdim \val pt < 0 pt
    \edef\tempcolor{\noexpand\cellcolor{myyellow!\colorpct!white}}%
  \else
    \edef\tempcolor{\noexpand\cellcolor{mypurple!\colorpct!white}}%
  \fi
  \tempcolor%
  \pgfmathprintnumberto[fixed, precision=3]{\val}{\rounded}%
  \rounded%
}
\begin{table}[htbp]
\centering
\caption{Correlation Matrix}
\tiny
\begin{adjustbox}{\textwidth}
\begin{tabular}{l*{11}{r}}
\toprule
 & \rotatebox{90}{Age} & 
\rotatebox{90}{Gender} & 
\rotatebox{90}{\shortstack{Sleep\\Duration}} & 
\rotatebox{90}{\shortstack{Stress\\Level}} & 
\rotatebox{90}{\shortstack{Diet\\Type}} & 
\rotatebox{90}{\shortstack{Daily\\Screen Time}} & 
\rotatebox{90}{\shortstack{Exercise\\Frequency}} & 
\rotatebox{90}{\shortstack{Caffeine\\Intake}} & 
\rotatebox{90}{\shortstack{Reaction\\Time}} & 
\rotatebox{90}{\shortstack{Memory\\Test Score}} & 
\rotatebox{90}{\shortstack{Cognitive\\Score}} \\
\midrule
Age & \colorCell{1.000000} & \colorCell{0.001276} & \colorCell{0.000691} & \colorCell{-0.000114} & \colorCell{-0.002655} & \colorCell{-0.002442} & \colorCell{-0.000812} & \colorCell{-0.004267} & \colorCell{0.004668} & \colorCell{-0.002198} & \colorCell{-0.005976} \\
Gender & \colorCell{0.001276} & \colorCell{1.000000} & \colorCell{-0.001585} & \colorCell{-0.004761} & \colorCell{-0.004360} & \colorCell{0.003817} & \colorCell{0.006187} & \colorCell{-0.000149} & \colorCell{0.000852} & \colorCell{-0.000886} & \colorCell{-0.000905} \\
Sleep  Duration & \colorCell{0.000691} & \colorCell{-0.001585} & \colorCell{1.000000} & \colorCell{0.004940} & \colorCell{-0.003541} & \colorCell{-0.000376} & \colorCell{-0.000471} & \colorCell{-0.002482} & \colorCell{-0.009699} & \colorCell{-0.001525} & \colorCell{0.150595} \\
Stress Level & \colorCell{-0.000114} & \colorCell{-0.004761} & \colorCell{0.004940} & \colorCell{1.000000} & \colorCell{0.003974} & \colorCell{-0.004818} & \colorCell{0.003923} & \colorCell{0.001048} & \colorCell{-0.011374} & \colorCell{0.000852} & \colorCell{-0.227639} \\
Diet Type & \colorCell{-0.002655} & \colorCell{-0.004360} & \colorCell{-0.003541} & \colorCell{0.003974} & \colorCell{1.000000} & \colorCell{0.002465} & \colorCell{0.004792} & \colorCell{0.005027} & \colorCell{0.005591} & \colorCell{0.004156} & \colorCell{-0.003799} \\
Daily Screen Time & \colorCell{-0.002442} & \colorCell{0.003817} & \colorCell{-0.000376} & \colorCell{-0.004818} & \colorCell{0.002465} & \colorCell{1.000000} & \colorCell{-0.002102} & \colorCell{-0.003295} & \colorCell{0.000094} & \colorCell{0.000315} & \colorCell{-0.198515} \\
Exercise Frequency & \colorCell{-0.000812} & \colorCell{0.006187} & \colorCell{-0.000471} & \colorCell{0.003923} & \colorCell{0.004792} & \colorCell{-0.002102} & \colorCell{1.000000} & \colorCell{0.000904} & \colorCell{-0.001313} & \colorCell{-0.001278} & \colorCell{-0.021184} \\
Caffeine Intake & \colorCell{-0.004267} & \colorCell{-0.000149} & \colorCell{-0.002482} & \colorCell{0.001048} & \colorCell{0.005027} & \colorCell{-0.003295} & \colorCell{0.000904} & \colorCell{1.000000} & \colorCell{0.005546} & \colorCell{0.002529} & \colorCell{-0.122862} \\
Reaction Time & \colorCell{0.004668} & \colorCell{0.000852} & \colorCell{-0.009699} & \colorCell{-0.011374} & \colorCell{0.005591} & \colorCell{0.000094} & \colorCell{-0.001313} & \colorCell{0.005546} & \colorCell{1.000000} & \colorCell{-0.002262} & \colorCell{-0.818470} \\
Memory Test Score & \colorCell{-0.002198} & \colorCell{-0.000886} & \colorCell{-0.001525} & \colorCell{0.000852} & \colorCell{0.004156} & \colorCell{0.000315} & \colorCell{-0.001278} & \colorCell{0.002529} & \colorCell{-0.002262} & \colorCell{1.000000} & \colorCell{0.363894} \\
Cognitive Score & \colorCell{-0.005976} & \colorCell{-0.000905} & \colorCell{0.150595} & \colorCell{-0.227639} & \colorCell{-0.003799} & \colorCell{-0.198515} & \colorCell{-0.021184} & \colorCell{-0.122862} & \colorCell{-0.818470} & \colorCell{0.363894} & \colorCell{1.000000} \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{table}
From the correlation matrix we can see that there are some individual variables that have a bigger effect on the end score. The variables like sleep duration and memory test score positively effect the cognitive score, where as the variables like stress level, daily screen time, caffeine intake and reaction time negatively effect it. The results have been rounded up to the 3 decimal digit.
The Ai predicted score has been removed from the matrix because it had similar results to the the prediciton score and to reduce space.
\subsection{Principal Component Analysis}
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{PC} & \textbf{Explained Variance Ratio} & \textbf{Cumulative Variance Ratio} & \textbf{Jump from Previous} \\
\hline
PC1  & 0.117427 & 0.117427 & 0.117427 \\
PC2  & 0.115749 & 0.233177 & 0.115750 \\
PC3  & 0.115453 & 0.348630 & 0.115453 \\
PC4  & 0.114882 & 0.463511 & 0.114882 \\
PC5  & 0.114118 & 0.577629 & 0.114118 \\
PC6  & 0.113853 & 0.691482 & 0.113853 \\
PC7  & 0.112966 & 0.804448 & 0.112966 \\
PC8  & 0.093347 & 0.897795 & 0.093347 \\
PC9  & 0.064517 & 0.962312 & 0.064517 \\
PC10 & 0.037689 & 1.000000 & 0.037689 \\
\hline
\end{tabular}
\caption{Explained Variance, Cumulative Variance, and Incremental “Jump” for Each Principal Component}
\label{tab:pca_variance_updated}
\end{table}

From Table~\ref{tab:pca_variance_updated} it is clear that no single principal component overwhelmingly dominates the variance. Instead, the information is spread relatively evenly across the first seven components, with a noticeable drop (“jump”) in explained variance only after PC7. This suggests that multiple axes contribute meaningfully to the dataset’s structure rather than one or two principal directions.

\subsection{T-SNE}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\linewidth]{tsne.png}
    \caption{T-SNE, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
From this picture we can see that there are 3 different and distinct groups of people that show up, which in their selves have high levels of variety regarding the cognitive scores.The color variation within and between clusters suggests that even people with similar lifestyle patterns can have different cognitive outcomes, which can be influenced by some of the factors.
\subsection{Mutual Information}
\begin{table}[H]
\centering
\caption{Mutual Information Scores regarding Cognitive cores}
\begin{tabular}{lr}
\toprule
\textbf{Feature} & \textbf{Mutual Information Score} \\
\midrule
Diet Type             & 0.5387 \\
Exercise Frequency    & 0.0804 \\
Memory Test Score     & 0.0357 \\
Daily Screen Time     & 0.0341 \\
Reaction Time         & 0.0207 \\
Stress Level          & 0.0151 \\
Gender                & 0.0081 \\
Age                   & 0.0006 \\
Sleep Duration        & 0.0000 \\
Caffeine Intake       & 0.0000 \\
\bottomrule
\end{tabular}
\label{tab:mutual_info}
\end{table}

\subsection{Analysis of Age distribution}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\linewidth]{Detailed_age.png}
    \caption{Age distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[ht]
    \centering
    \begin{tabular}{|l|l|}
    \hline
    \textbf{Statistic} & \textbf{Value} \\
    \hline
    Mean & 38.525525 \\
    Standard Deviation & 12.101876 \\
    Minimum & 18.000000 \\
    Maximum & 59.000000 \\
    25\% Percentile & 28.000000 \\
    50\% Percentile & 39.000000 \\
    75\% Percentile & 49.000000 \\
    Skewness & -0.003621854422145677 \\
    Kurtosis & -1.1967270989742835 \\
    \hline
    \end{tabular}
    
\caption{Summary Statistics for the Age}
\end{table}
The age of each individual ranges from 18 to 59 (mean ≈ 38.5 years, median = 39), reflecting a balanced sample of younger and middle‐aged adults with no extreme outliers. The standard deviation is about 12.1 years, and the interquartile range spans 21 years (Q1 = 28, Q3 = 49), indicating moderate variability concentrated around the center. Skewness (–0.0036) and kurtosis (–1.20) are both near zero, confirming a nearly symmetric, platykurtic distribution—flatter than normal—with ages evenly distributed. This uniform spread ensures that age‐related trends (e.g., slower reaction times with increasing age) can be modeled reliably without undue bias from extreme values.


\subsection{Analysis of Sleep Duration distribution}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Image_sleep.png}
    \caption{Sleep duration distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}

\begin{itemize}[noitemsep]
        Sleep spans from 4 to 10 hours (mean ≈ 7.01 h, median = 7 h), indicating most participants obtain a moderate, adult‐recommended amount. With a standard deviation of about 1.73 h, there is noticeable variability: the first quartile is 5.5 h and the third quartile is 8.5 h (IQR = 3 h), showing that the middle 50 \% of individuals sleep between 5.5 and 8.5 hours. Skewness (≈ –0.0036) and kurtosis (≈ –1.20) both lie near zero, revealing an almost perfectly symmetric, platykurtic distribution (flatter than normal) with few extreme outliers. This uniform spread suggests that while most people sleep within healthy bounds, a minority of short (≤ 5.5 h) or long (≥ 8.5 h) sleepers may exhibit sleep patterns potentially impacting cognitive performance.\newline
\end{itemize}

\FloatBarrier
\vspace{-0.5cm}
\begin{table}[H]
\centering
\begin{tabular}{|l|l|}
\hline
\textbf{Statistic} & \textbf{Sleep Duration} \\
\hline
Mean & 7.01 \\
Standard Deviation & 1.73 \\
Minimum & 4 \\
Maximum & 10 \\
25\% Percentile & 5.50 \\
50\% Percentile & 7.00 \\
75\% Percentile & 8.50 \\
Skewness & -0.0036 \\
Kurtosis & -1.20 \\
\hline
\end{tabular}
\caption{Summary Statistics for Sleep Duration}
\end{table}

\FloatBarrier
\subsection{Analysis of Self Reported Stress Levels distribution}
\begin{figure}[t]  % allow it to float more naturally
    \centering
    \includegraphics[width=0.6\linewidth]{Stress_img.png}
    \caption{Stress levels distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}


\begin{table}[ht]
\centering
\begin{tabular}{|l|l|}
\hline
\textbf{Statistic} & \textbf{Stress Level} \\
\hline
Mean & 5.49 \\
Standard Deviation & 2.87 \\
Minimum & 1 \\
Maximum & 10 \\
25\% Percentile & 3 \\
50\% Percentile (Median) & 5 \\
75\% Percentile & 8 \\
Skewness & 0.0035 \\
Kurtosis & -1.22 \\
\hline
\end{tabular}

\caption{Summary Statistics for Self-Reported Stress Levels}
\label{tab:stress_level_stats}
\end{table}

 Self reported stress values span from 1 (minimal stress) to 10 (maximal stress), with a mean of approximately 5.49 and a median of 5, indicating a generally moderate, balanced stress experience. The standard deviation is about 2.87, reflecting substantial variability in how individuals perceive stress. The first quartile (Q1) is 3 and the third quartile (Q3) is 8 (IQR = 5), showing that the middle 50 \% of participants report stress levels between 3 and 8. Skewness (~ 0.0035) and kurtosis (~ –1.22) are both near zero, revealing an almost perfectly symmetric, platykurtic distribution with relatively few people at the extremes. This even spread suggests that the dataset captures a wide spectrum of stress—from low to high—without strong clustering at one end.

\subsection{Analysis of Hours of Screentime distribution}
Screen time in the dataset ranges from 1 to 12 hours (mean ≈ 6.50 h, median = 6.50 h), reflecting modern lifestyles where work, leisure, and social activities all involve screens. While 6.5 h may initially seem high, this total includes both occupational (e.g., computer use) and recreational (e.g., smartphones) screen exposure. The standard deviation of approximately 3.17 h indicates moderate variability: 25 \% of individuals spend ≤ 3.8 h in front of screens (Q1), and 75 \% spend ≤ 9.2 h (Q3), so the interquartile range (IQR) is 5.4 h. Skewness (~ –0.0024) and kurtosis (~ –1.19) are both near zero, showing an almost perfectly symmetric, platykurtic distribution—most screen times cluster around the center with few extreme outliers. Because “screen time” here aggregates different types (recreational vs. work, passive vs. active), we note that finer categorization could better reveal how specific screen‐use patterns affect cognitive performance.
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Image_screntime.png}
    \caption{Screentime hours distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Statistic} & \textbf{Value} \\
\hline
Mean & 6.504646 \\
Standard Deviation & 3.167072 \\
Minimum & 1.000000 \\
Maximum & 12.000000 \\
25th Percentile  & 3.800000 \\
50th Percentile (Median) & 6.500000 \\
75th Percentile & 9.200000 \\
Skewness & -0.0024133040531494955 \\
Kurtosis & -1.1933176931534968 \\
\hline
\end{tabular}
\caption{ Summary Statistics for Screen Time}
\end{table}
\FloatBarrier
\subsection{Analysis of Caffeine Intake distribution}
Caffeine Intake (mg)  ranges from 0 to 499 mg per day (mean ≈ 249 mg, median = 249 mg), corresponding to roughly 0 to 5½ cups of coffee (average ≈ 2.6 cups). The standard deviation is about 144.5 mg, indicating wide variability in consumption habits. The first quartile is 123 mg (25 \% of participants consume ≤ 123 mg) and the third quartile is 375 mg (75 \% consume ≤ 375 mg), yielding an IQR of 252 mg. Skewness (~ 0.0008) and kurtosis (~ –1.21) are both near zero, reflecting an almost perfectly symmetric, platykurtic distribution (flatter than normal) with few extreme outliers. These statistics suggest most individuals consume moderate caffeine amounts, but a notable minority drink very little or very large quantities, which could influence cognitive performance differently.
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Detailed_caffeine.png}
    \caption{Caffeine grams inatake distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Statistic} & \textbf{Value} \\
\hline
Mean & 248.988213 \\
Standard Deviation (std) & 144.541990 \\
Minimum & 0.000000 \\
Maximum  & 499.000000 \\
25th Percentile & 123.000000 \\
Median (50\%) & 249.000000 \\
75th Percentile & 375.000000 \\
Skewness & 0.0007968618749813822 \\
Kurtosis & -1.2056316888797205 \\
\hline
\end{tabular}
\caption{Summary Statistics for Caffeine Intake}
\end{table}


\subsection{Analysis of Reaction Time distribution}
Reaction times range from 200 to 599.99 ms (mean ≈ 399.97 ms, median ≈ 400.36 ms), reflecting a sample aged 18–59 where slower responses are expected. The standard deviation is about 115.37 ms, indicating moderate variability: the first quartile is 300.15 ms and the third quartile is 499.25 ms (IQR ≈ 199.10 ms), so the central 50\% of participants respond between roughly 300 and 500 ms. Skewness (~ 0.0020) and kurtosis (~ –1.1952) are both near zero, showing an almost perfectly symmetric, platykurtic distribution with relatively few extreme outliers. This even spread suggests no age subgroup or outlier group dominates reaction times, allowing reliable modeling of age‐related processing speed differences.

\begin{figure}[H]
    \centering 
    \includegraphics[width=0.6\linewidth]{Detailed_reactiontime.png}
    \caption{Reaction time distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}

\begin{table}[H]
\centering
\begin{tabular}{|l|l|}
\hline
\textbf{Statistic} & \textbf{Value} \\
\hline
Mean & 399.973579 \\
Standard Deviation (std) & 115.369329 \\
Minimum & 200.000000 \\
25th Percentile (25\%) & 300.150000 \\
Median (50\%) & 400.360000 \\
75th Percentile (75\%) & 499.250000 \\
Maximum & 599.990000 \\
Skewness & 0.002032159172294202 \\
Kurtosis & -1.1952298915324233 \\
\hline
\end{tabular}
\caption{Summary Statistics for Reaction Time}
\end{table}
\FloatBarrier

\subsection{Analysis of Memory Test Score distribution}
Memory score -The score is calculated from 0 to 100 and is derived from a test, which is not specified in the dataset which one. Test scores appear reliably centered, symmetrical, and free of major outliers, making the dataset ideal for statistical modeling or comparison. The consistency across central tendency and dispersion metrics indicates a well-behaved variable, suitable for inferential statistics or group-wise analysis. 
\begin{figure}[H]
    \centering 
    \includegraphics[width=0.6\linewidth]{Memory_score_Detailed.png}
    \caption{Memory test score  distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Statistic} & \textbf{Value} \\
\hline
Mean & 69.498350 \\
Standard Deviation (std) & 17.305659 \\
Minimum & 40.000000 \\
Maximum & 99.000000 \\
25\%  Percentile& 55.000000 \\
50\% Percentile & 70.000000 \\
75\% Percentile & 85.000000 \\
Skewness & 0.0032658425823375 \\
Kurtosis & -1.202883982524206 \\
\hline
\end{tabular}
\FloatBarrier
\caption{Summary Statistics for Memory Test Score}
\end{table}
\subsection{Analysis of Gender distribution}
Regarding the gender distribution, the dataset is roughly balanced between females and males, with a smaller but not insignificant number of respondents identifying as "Other". The counts are 48, 48, and 4 respectively.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Genders.png}
    \caption{Gender distribution, visualized.}
    \label{fig:gender_distribution}
\end{figure}

\begin{table}[H]
\centering
\begin{tabular}{|l|r|r|}
\hline
\textbf{Gender} & \textbf{Count} & \textbf{Percentage (\%)} \\
\hline
Female & 38,404 & 48.00 \\
Male & 38,322 & 47.90 \\
Other & 3,274 & 4.09 \\
\hline
\end{tabular}
\caption{Gender Distribution in the Dataset.}
\label{tab:gender_distribution}
\end{table}
\FloatBarrier

\subsection{Analysis of Diet Type distribution} 
    \item Diet Type -  The diet type distribution is one of our least balanced variables in the dataset, which is to be expected because it is a different type of life style and eating behaviour all together. The distribution of the values is the following, the regular non-vegetarian diet is 59.98 \% of the dataset, vegetarians are 30.17 \% and vegans are 9.85 \%. 
    This is good since a lot of our variables have the a similar distribution and this will add some noise to the models to avoid overfitting.
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Diet_type.png}
    \caption{Diet Type distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[h!]
\centering
\begin{tabular}{|l|r|r|}
\hline
\textbf{Diet Type} & \textbf{Count} & \textbf{Percentage (\%)} \\
\hline
Non-Vegetarian & 47,986 & 59.98 \\
Vegetarian     & 24,136 & 30.17 \\
Vegan          & 7,878  & 9.85 \\
\hline
\end{tabular}
\caption{Distribution of Diet Types in the Dataset}
\end{table}
\subsection{Analysis of Exercise Frequency distribution}
Exercise frequency - Exercise frequency is yet another variable which has different levels of representation for each value. The people who who exercise low and medium times a week are almost identical. They are 39.99 \% and 39.97 \% respectively, whereas the high frequency athletes are 20.14 \% of the dataset. 
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Exercise_Frequency.png}
    \caption{Exercise Frequency distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[h!]
\centering
\begin{tabular}{|l|r|r|}
\hline
\textbf{Exercise Frequency} & \textbf{Count} & \textbf{Percentage (\%)} \\
\hline
Medium & 31,990 & 39.99 \\
Low    & 31,896 & 39.87 \\
High   & 16,114 & 20.14 \\
\hline
\end{tabular}
\caption{Distribution of Exercise Frequency Levels in the Dataset}
\end{table}

\subsection{Analysis of Prediction Scores distribution}
 Here in the dataset we have 2 variables which we can use as target variables, but one is of value. We will train our model on the actual prediction score and we can use the AI prediction score for that value as a reference and compare it. In general the average mistake that the AI model that was trained by the person who provided the dataset is 2.4, where the minimum and maximum are 0 and 5 respectively. 
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{scores.png}
    \caption{Comparison of the scores distribution, visualized.}
    \label{fig:appendix_residuals}
\end{figure}
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Statistic} & \textbf{Value} \\
\hline
Count & 80,000 \\
Mean & 2.448780 \\
Standard Deviation (std) & 1.468794 \\
Minimum & 0.000000 \\
Maximum & 5.000000 \\
25th Percentile & 1.180000 \\
Median (50\%) & 2.450000 \\
75th Percentile & 3.720000 \\
\hline
Pearson Correlation & 0.9924 \\
Spearman Correlation & 0.9926 \\
\hline
\end{tabular}
\caption{Summary Statistics and Correlation Metrics}
\end{table}


\end{document}
