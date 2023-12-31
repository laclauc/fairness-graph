# Fairness for Machine Learning on Graphs : a Survey

This repository contains additional elements for the survey paper on fairness
for Machine Learning, including :

- `benchmarks.md` provide links to download the benchmark graphs listed in the
article
- `sota.md` contains links to the github repositories with state-of-the-art
models implementation.
- `data`is a folder that contains links to the benchmark datasets mentioned in the survey.
- `synthetic` is a folder that contains the code to generate the synthetic
graphs G1--G6 and the script to produce the visualisation presented in the survey.
Three files can be found in this folder:
  - `generate_graph.py` contains the required functions to generate the 6 use-cases presented in the survey
  - `script_visualisation.py` allows to generate and visualise the graphs
  - `save_graph.py` allows to generate the graph and save it

**Example to visualise and save g1**
  ```
    python script_visualisation.py g1
    python save_graph.py g1 graphs
  ```

**If your paper does not appear in this survey, but seems relevant to its contents, please let us know, and we will try to include it in
the revised versions.**  

### Citation

The paper can be found [[http://arxiv.org/abs/2205.05396]] (arxiv link).

If you plan on using some of our ressources or the paper itself, please cite our work as follows

@article{choudhary2022,   
title = {A Survey on Fairness for Machine Learning on Graphs},  
authors = {Choudhary, Manvi and Laclau, Charlotte and Largeron, Christine},  
journal = {CoRR},  
year = {2022}  
}
