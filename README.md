# README.md
--------------------

## STEP1 - HMM model build
[hmm_project directory](hmm_project/)

In this directory you'll find the [Jupyter notebook](hmm_project/buildingHMMlogo_workflow.ipynb).

by following the steps you could retrieve the hmm_logo and .hmm file that we'll use, later on.


## STEP2 - Validation and performance of the model 
[val/secondvalidation directory](val/secondvalidation/)

In this directory you'll find a [Jupyter notebook](val/secondvalidation/crossv_opt-Workflow.ipynb) with the steps to perform the validation of [HMM model](hmm_project/kunitz_newlogo.hmm) created in the first step. 

Database file for **not Kunitz** proteins was too big to be uploaded on git, therefore you could download it by using the same query used to retrieved them.

```reviewed:yes NOT database:(type:pfam pf00014)``` results shoud be: ```561772```

Neither the splitting was possible to upload, but it is a plain split in halves done with the python script [split-fasta.py](val/split-fasta.py). Run by the command:

```python split-fasta.py [file_input] 2 [prefix_output]```

Sequences were splitted in: ```280925``` and ```280847``` each. 

### Data preparation

In order to let the [Jupyter notebook](val/secondvalidation/crossv_opt-Workflow.ipynb) run without any problem from the beginning you should have in the same local directory as the notebook this data:

- **all_PF00014.fasta** 
    - downloaded from [UniProt](https://www.uniprot.org/)
- **all_notPF00014.fasta**
    - downloaded as well from [UniProt](https://www.uniprot.org/)
- [**split-fasta.py**](val/split-fasta.py)

The first two data should be splitted in Test and Train with [**split-fasta.py**](val/split-fasta.py).


Other data:
- [HMM model](../../hmm_project/kunitz_newlogo.hmm)
    - which can be retrieved as stated in the first step