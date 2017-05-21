# ItemizedPy
This is the Python 3 version of Itemized. The program adds items to inventory and then prints out how many items you have. You can specify how many items to add by passing a number as an argument. If you don't specify any items, you will receive one item. 

Yes, it's very simple. That's the idea.

## Example

```
$> python itemize.py
You have:
  An item
$> python itemize.py 4
You have:
  Four items
$> python itemize.py 42
You have: 
  42 items
```

## Prerequisites
- Python 3.6.1

## Setup
    python3 -m venv venv
    . ./venv/bin/activate
    
## Running
    python src/itemize.py
