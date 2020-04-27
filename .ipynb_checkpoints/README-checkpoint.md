# README
--------------------

# HMM model build


## Validation and performance of the model [val/secondvalidation directory]()

In this directory you'll find a [Jupyter notebook](crossv_opt-Workflow.ipnb) with the steps to perform the validation of the created [HMM model](../../hmm_project/kunitz_newlogo.hmm). 

Database file for **not Kunitz** proteins was too big to be uploaded on git, therefore you could download it by using the same query used to retrieved them.

```reviewed:yes NOT database:(type:pfam pf00014)``` results shoud be: ```561772```

Neither the splitting was possible to upload, but it is a plain split in halves done with the python script [split-fasta.py](../split-fasta.py). Run by the command:

```python split-fasta.py [file_input] 2 [prefix_output]```

Sequences were splitted in: ```280925``` and ```280847``` each. 

### Data preparation

In order to let the [Jupyter notebook](crossv_opt-Workflow.ipnb) run without any problem from the beginning you should have in the same local directory this data:

- **all_PF00014.fasta** 
    - downloaded from [UniProt](https://www.uniprot.org/)
- **all_notPF00014.fasta**
    - downloaded as well from [UniProt](https://www.uniprot.org/)
- [**split-fasta.py**](../split-fasta.py)

Other data that should not be in your local directory is:
- [HMM model](../../hmm_project/kunitz_newlogo.hmm)
    - which can be retrieved as stated in 