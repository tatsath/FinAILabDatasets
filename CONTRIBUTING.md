## Contributing to FinAILAb-Datasets

If you are interested in contributing to FinAILAb-Datasets, your contributions will fall
into two categories:
1. You want to propose a new Data source and include it in the documentation
    - Create an python code about your intended data set and include the details under the "Data sources" and link the items to whichever section is good. 
2. You want to implement a new item:
    - Look at the roadmap here: https://github.com/tatsath/FinAILabDatasets/projects/2
    - Pick a to do list or in progress list and comment on the task that you want to work on this feature.
    
Once you finish implementing a additional items, please send a Pull Request to
https://github.com/tatsath/FinAILabDatasets/


If you are not familiar with creating a Pull Request, here are some guides:
- http://stackoverflow.com/questions/14680711/how-to-do-a-github-pull-request
- https://help.github.com/articles/creating-a-pull-request/


## Developing FinAILAb-Datasets

To develop FinAILAb-Datasets on your machine, here are some tips:

1. Clone a copy of FinAILAb-Datasets from source:

```bash
git clone https://github.com/tatsath/FinAILabDatasets
cd https://github.com/tatsath/FinAILabDatasets
```

2. Install Stable-Baselines in develop mode, with support for building the docs and running tests:

```bash
pip install -e .[docs,tests]
```

## Codestyle

Please document each function/method and [type](https://google.github.io/pytype/user_guide.html) them using the following template:

```python

def my_function(arg1: type1, arg2: type2) -> returntype:
    """
    Short description of the function.

    :param arg1: (type1) describe what is arg1
    :param arg2: (type2) describe what is arg2
    :return: (returntype) describe what is returned
    """
    ...
    return my_variable
```


