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

## Testing

    python -m unittest discover -s tests

## Notes
I think this is about as Pythonic as I can make it. I don't like having multiple classes in one file, but that seems to make Python the happiest. Putting them into sub-modules and importing them was punished by repeating myself over and over again repeatiously, e.g. `from app.models.Item import Item`.
