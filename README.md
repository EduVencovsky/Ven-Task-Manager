# Ven-Task-Manager
Ven Task Manager

## Methods

### `ven init` 
Starts ven task manager
    1.  Check if ven.json already exists in current folder
        *  *Error message* if already exists
    2.  Ask config questions
        *  user name
        *  user email
        *  money per hour (optional)
    3.  Creates `ven.json` file


## Data 

### `ven.json` structure

{
    'username': ...string ,
    'useremail': ...string ,
    'days' [
        '*task_id*': {
            'isCompleted': *true/false*
            'time': [*begin_time*, *pause_time*, ...dataTime ]
        },
        ...dict
    ],
    'money': ...0.2float
}

## TODO 

### Functionalities

#### :x: Create `ven_installer.exe`
#### :x: Create `ven.exe`
    `ven.py` code recompiled to `ven.exe`
#### :x: Association with `git`

### Methods

|   Methods   |   Progress  |    Docs     |
| :---------: | :---------: | :---------: |
| init        | [_________] | [#########] |
| username    | not started | not started |
| useremail   | not started | not started |
| start       | not started | not started |
| pause       | not started | not started |
| resume      | not started | not started |
| end         | not started | not started |
| today       | not started | not started |
| status      | not started | not started |
| export      | not started | not started |

